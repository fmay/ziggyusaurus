import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';

export default function Root({ children }) {
  const location = useLocation();
  useEffect(() => {
    // Override the document title to always show "Ziggy Docs"
    const observer = new MutationObserver(() => {
      if (document.title !== 'Ziggy Docs') {
        document.title = 'Ziggy Docs';
      }
    });

    observer.observe(document.querySelector('title'), {
      childList: true,
      subtree: true,
    });

    // Set initial title
    document.title = 'Ziggy Docs';

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    // Fix anchor scrolling when page loads with hash or route changes
    const hash = location.hash;
    if (!hash) return;

    // Wait for images to load before scrolling to anchor
    const images = document.querySelectorAll('img');
    const imagePromises = Array.from(images).map(img => {
      if (img.complete) return Promise.resolve();
      return new Promise(resolve => {
        img.addEventListener('load', resolve);
        img.addEventListener('error', resolve); // Resolve even on error
      });
    });

    Promise.all(imagePromises).then(() => {
      // Small delay to ensure layout is stable
      setTimeout(() => {
        const element = document.querySelector(hash);
        if (element) {
          element.scrollIntoView({ behavior: 'auto', block: 'start' });
        }
      }, 100);
    });
  }, [location]);

  return <>{children}</>;
}