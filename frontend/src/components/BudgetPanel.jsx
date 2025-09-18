import React from 'react'
export default function BudgetPanel({recommendations=[], onRefresh, loading}) {
  return (
    <div style={{border:'1px solid #eee',borderRadius:12,overflow:'hidden'}}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',padding:10,background:'#fafafa'}}>
        <strong>Recommended Split</strong>
        <button onClick={onRefresh} disabled={loading} style={{padding:'6px 10px',border:'1px solid #ddd',borderRadius:8,background:'#fff',cursor:'pointer'}}>Refresh</button>
      </div>
      <table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead><tr><th style={{textAlign:'left',padding:8}}>Platform</th><th style={{textAlign:'right',padding:8}}>Share</th><th style={{textAlign:'left',padding:8}}>Why</th></tr></thead>
        <tbody>
          {recommendations.map((r,idx)=>(
            <tr key={idx}>
              <td style={{padding:8,borderTop:'1px solid #eee'}}>{r.platform}</td>
              <td style={{padding:8,borderTop:'1px solid #eee',textAlign:'right'}}>{(r.share*100).toFixed(0)}%</td>
              <td style={{padding:8,borderTop:'1px solid #eee'}}>{r.rationale}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
