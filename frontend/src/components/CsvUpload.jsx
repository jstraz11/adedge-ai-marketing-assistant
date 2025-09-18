import React, {useState} from 'react'
import { uploadCsv } from '../lib/api.js'

export default function CsvUpload({onUploaded}) {
  const [file, setFile] = useState(null)
  const [busy, setBusy] = useState(false)
  const [msg, setMsg] = useState('')

  const onSubmit = async (e) => {
    e.preventDefault()
    setBusy(true); setMsg('Uploading...')
    try {
      const res = await uploadCsv(file)
      setMsg('Uploaded ' + (res.inserted || 0) + ' rows');
      onUploaded && onUploaded()
    } catch (e) {
      setMsg('Upload failed. Make sure CSV has columns: Platform, Impressions, Clicks, Conversions, Cost, (optional Date).')
    } finally {
      setBusy(false)
    }
  }

  return (
    <form onSubmit={onSubmit} style={{border:'1px solid #eee',borderRadius:12,padding:16,boxShadow:'0 1px 3px rgba(0,0,0,0.05)'}}>
      <input type='file' accept='.csv' onChange={(e)=>setFile(e.target.files?.[0]||null)} />
      <button type='submit' disabled={busy} style={{marginLeft:8,padding:'6px 10px',border:'1px solid #ddd',borderRadius:8,background:'#fff',cursor:'pointer'}}>
        {busy ? 'Uploading…' : 'Upload CSV'}
      </button>
      {msg && <div style={{marginTop:8,fontSize:12,color:'#555'}}>{msg}</div>}
    </form>
  )
}
