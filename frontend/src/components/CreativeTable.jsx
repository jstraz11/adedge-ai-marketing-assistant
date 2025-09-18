import React from 'react'
export default function CreativeTable({rows=[]}) {
  return (
    <div style={{border:'1px solid #eee',borderRadius:12,overflow:'hidden'}}>
      <table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead style={{background:'#fafafa'}}>
          <tr><th style={{textAlign:'left',padding:8}}>Creative</th><th style={{textAlign:'right',padding:8}}>CTR</th><th style={{textAlign:'right',padding:8}}>CVR</th></tr>
        </thead>
        <tbody>
          {rows.map(r => (
            <tr key={r.id}>
              <td style={{padding:8,borderTop:'1px solid #eee'}}>{r.name}</td>
              <td style={{padding:8,borderTop:'1px solid #eee',textAlign:'right'}}>{(r.ctr*100).toFixed(2)}%</td>
              <td style={{padding:8,borderTop:'1px solid #eee',textAlign:'right'}}>{(r.cvr*100).toFixed(2)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
