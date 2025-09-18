import React from 'react'

function Card({title, value, sub}) {
  return (
    <div style={{border:'1px solid #eee',borderRadius:12,padding:16,boxShadow:'0 1px 3px rgba(0,0,0,0.05)'}}>
      <div style={{fontSize:12,color:'#777'}}>{title}</div>
      <div style={{fontSize:22,fontWeight:700}}>{value}</div>
      {sub && <div style={{fontSize:12,color:'#999'}}>{sub}</div>}
    </div>
  )
}

export default function KPICards({report}) {
  const fmt2 = (n)=> (n==null?'-':Number(n).toFixed(2))
  const grid = {display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:12}
  return (
    <div style={grid}>
      <Card title='Impressions' value={report.impressions} />
      <Card title='Clicks' value={report.clicks} />
      <Card title='Conversions' value={report.conversions} />
      <Card title='Cost' value={'$'+fmt2(report.cost)} />
      <Card title='CVR' value={fmt2(report.cvr*100)+'%'} />
      <Card title='ROAS' value={report.roas==null?'-':fmt2(report.roas)} />
    </div>
  )
}
