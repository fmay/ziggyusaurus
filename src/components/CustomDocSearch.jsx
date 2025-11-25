import React from 'react';
import { DocSearch } from '@docsearch/react';
import '@docsearch/css';

export default function CustomDocSearch() {
  return (
    <DocSearch
      appId="XPMSD22TBN"
      apiKey="d306c3a1645bb47380811310974fed3b"
      indices={["Ziggy Docs"]}
      askAi="PjYYE8bjFKvA"
    />
  );
}
