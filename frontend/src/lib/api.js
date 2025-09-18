export const API_BASE = 'http://localhost:8000'

async function getJSON(path) {
  const res = await fetch(API_BASE + path)
  return res.json()
}

export const getReport = () => getJSON('/report')
export const getBudget = () => getJSON('/recommendations/budget')
export const getAudiences = () => getJSON('/audiences')
export const getCreatives = () => getJSON('/creatives')

export async function uploadCsv(file) {
  const fd = new FormData();
  fd.append('file', file);
  const res = await fetch(API_BASE + '/upload/csv', { method: 'POST', body: fd })
  return res.json()
}
