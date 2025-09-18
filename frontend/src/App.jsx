import React, { useEffect, useState } from 'react'
import { getReport, getBudget, getAudiences, getCreatives, uploadCsv } from './lib/api.js'
import KPICards from './components/KPICards.jsx'
import AudienceTable from './components/AudienceTable.jsx'
import CreativeTable from './components/CreativeTable.jsx'
import BudgetPanel from './components/BudgetPanel.jsx'
import CsvUpload from './components/CsvUpload.jsx'

export default function App() {
  const [report, setReport] = useState(null)
  const [recs, setRecs] = useState([])
  const [audiences, setAudiences] = useState([])
  const [creatives, setCreatives] = useState([])
  const [loading, setLoading] = useState(true)
  const [msg, setMsg] = useState('')

  const loadAll = async () => {
    setLoading(true)
    try {
      const [r, b, a, c] = await Promise.all([
        getReport(),
        getBudget(),
        getAudiences(),
        getCreatives()
      ])
      setReport(r)
      setRecs(b.recommendations || b)
      setAudiences(a)
      setCreatives(c)
      setMsg('')
    } catch (e) {
      setMsg('Failed to load data. Is the backend running on http://localhost:8000 ?')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { loadAll() }, [])

  const onUploaded = async () => {
    setMsg('CSV uploaded. Refreshing recommendations...')
    await loadAll()
    setMsg('Refreshed after upload.')
  }

  return (
    <div style={{fontFamily:'system-ui,Segoe UI,Arial', padding:'20px', maxWidth: '1100px', margin:'0 auto'}}>
      <h1 style={{marginBottom:'10px'}}>AI Marketing Assistant</h1>
      <p style={{marginTop:0,color:'#555'}}>Backend: http://localhost:8000 • Frontend dev: http://localhost:5173</p>

      {msg && <div style={{padding:'10px',background:'#fff8c5',border:'1px solid #ffe58f',borderRadius:8,marginBottom:12}}>{msg}</div>}

      <section style={{marginBottom:20}}>
        <h2 style={{margin:'16px 0'}}>KPI Overview</h2>
        {report ? <KPICards report={report} /> : <div>Loading KPIs…</div>}
      </section>

      <section style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16, alignItems:'start'}}>
        <div>
          <h2 style={{margin:'16px 0'}}>Budget Recommendations</h2>
          <BudgetPanel recommendations={recs} onRefresh={loadAll} loading={loading} />
        </div>
        <div>
          <h2 style={{margin:'16px 0'}}>Upload CSV</h2>
          <CsvUpload onUploaded={onUploaded} />
        </div>
      </section>

      <section style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16, marginTop:16}}>
        <div>
          <h2 style={{margin:'16px 0'}}>Audiences</h2>
          <AudienceTable rows={audiences} />
        </div>
        <div>
          <h2 style={{margin:'16px 0'}}>Creatives</h2>
          <CreativeTable rows={creatives} />
        </div>
      </section>
    </div>
  )
}
