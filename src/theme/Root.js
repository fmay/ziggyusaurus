import React, { useEffect } from 'react';

export default function Root({ children }) {
  useEffect(() => {
    // Override the document title to always show "Docs"
    const observer = new MutationObserver(() => {
      if (document.title !== 'Docs') {
        document.title = 'Docs';
      }
    });

    observer.observe(document.querySelector('title'), {
      childList: true,
      subtree: true,
    });

    // Set initial title
    document.title = 'Docs';

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    // Fix anchor scrolling when page loads with hash
    const handleAnchorScroll = () => {
      const hash = window.location.hash;
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
            element.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }, 100);
      });
    };

    // Run on initial load
    handleAnchorScroll();

    // Also run when hash changes (clicking anchor links)
    window.addEventListener('hashchange', handleAnchorScroll);

    return () => {
      window.removeEventListener('hashchange', handleAnchorScroll);
    };
  }, []);

  return <>{children}</>;
}