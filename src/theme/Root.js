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

  return <>{children}</>;
}