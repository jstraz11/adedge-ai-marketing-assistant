from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from .models import PlatformMetrics
from .bandit import thompson_sampling_allocations
import pandas as pd

WINDOW_DAYS = 14

def _recent_df(session: Session):
    cutoff = (datetime.utcnow() - timedelta(days=WINDOW_DAYS)).date()
    q = session.query(PlatformMetrics).filter(PlatformMetrics.date >= cutoff)
    df = pd.read_sql(q.statement, session.bind)
    return df

def best_platform(session: Session):
    df = _recent_df(session)
    if df.empty:
        return {"platform": "Google", "score": 0.33, "window_days": WINDOW_DAYS}
    grouped = df.groupby("platform").agg({"impressions":"sum","conversions":"sum","cost":"sum"}).reset_index()
    allocs = thompson_sampling_allocations(grouped)
    if not allocs:
        return {"platform": "Google", "score": 0.33, "window_days": WINDOW_DAYS}
    best = max(allocs, key=lambda x: x["share"])
    return {"platform": best["platform"], "score": best["share"], "window_days": WINDOW_DAYS}

def budget_recommendations(session: Session):
    df = _recent_df(session)
    if df.empty:
        q_all = session.query(PlatformMetrics)
        df_all = pd.read_sql(q_all.statement, session.bind)
        if df_all.empty:
            platforms = ["Google","Meta","TikTok"]
            return [{"platform": p, "share": round(1.0/3, 2), "rationale": "No data; equal split"} for p in platforms]
        grouped = df_all.groupby("platform").agg({"conversions":"sum","cost":"sum"}).reset_index()
        grouped["roas"] = grouped.apply(lambda r: ((r["conversions"]*100.0)/r["cost"]) if r["cost"]>0 else 0.0, axis=1)
        total = grouped["roas"].sum()
        if total <= 0:
            platforms = grouped["platform"].tolist()
            return [{"platform": p, "share": round(1.0/len(platforms),2), "rationale":"No spend or value; equal split"} for p in platforms]
        recs=[]
        for _,row in grouped.iterrows():
            recs.append({"platform": row["platform"], "share": round(row["roas"]/total, 2), "rationale":"Fallback by ROAS"})
        return recs

    grouped = df.groupby("platform").agg({"impressions":"sum","conversions":"sum","cost":"sum"}).reset_index()
    allocs = thompson_sampling_allocations(grouped)
    s = sum(a["share"] for a in allocs) or 1.0
    out = []
    for a in allocs:
        out.append({"platform": a["platform"], "share": round(a["share"]/s, 2), "rationale": "Thompson Sampling over 14d impressions/conversions"})
    return out
