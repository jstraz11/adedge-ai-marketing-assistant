export const API_BASE =
  (import.meta.env && import.meta.env.VITE_API_BASE) ||
  (typeof window !== 'undefined' && window.__API_BASE__) ||
  'http://localhost:8000';

async function getJSON(path) {
  const res = await fetch(API_BASE + path);
  if (!res.ok) throw new Error('Request failed: ' + res.status);
  return res.json();
}

export const getReport = () => getJSON('/report');
export const getBudget = () => getJSON('/recommendations/budget');
export const getAudiences = () => getJSON('/audiences');
export const getCreatives = () => getJSON('/creatives');

export async function uploadCsv(file) {
  const fd = new FormData();
  fd.append('file', file);
  const res = await fetch(API_BASE + '/upload/csv', { method: 'POST', body: fd });
  if (!res.ok) throw new Error('Upload failed');
  return res.json();
}
