from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import pandas as pd
from datetime import datetime
import io

from .settings import Settings, get_settings
from .db import get_session, engine
from .models import Base, PlatformMetrics, PlatformSpend, AudienceMetrics, CreativeMetrics, Campaign
from .schemas import (
    AudienceOut, CreativeOut, BudgetRec, BestOut, ReportOut,
    ApplyIn, UploadCSVResponse, RecommendationsOut, HarvestResponse, CreativeGenResponse
)
from .mock_data import mock_audiences, mock_creatives
from .recommender import budget_recommendations, best_platform
from .training.train_audience import train_lightgbm_stub

app = FastAPI(title="AI Marketing Assistant API", version="1.0.0")

# Allow all CORS in MVP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auto-create tables
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/audiences", response_model=List[AudienceOut])
def audiences():
    return mock_audiences()

@app.get("/creatives", response_model=List[CreativeOut])
def creatives():
    return mock_creatives()

@app.get("/budget", response_model=List[BudgetRec])
def budget(session=Depends(get_session)):
    return budget_recommendations(session)

@app.get("/best", response_model=BestOut)
def best(session=Depends(get_session)):
    return best_platform(session)

@app.get("/recommendations/budget", response_model=RecommendationsOut)
def recommendations_budget(session=Depends(get_session)):
    recs = budget_recommendations(session)
    return {"recommendations": recs}

@app.get("/report", response_model=ReportOut)
def report(session=Depends(get_session)):
    q = session.query(PlatformMetrics)
    df = pd.read_sql(q.statement, session.bind)
    if df.empty:
        return {"impressions": 0, "clicks": 0, "conversions": 0, "cost": 0.0, "cvr": 0.0, "cpa": None, "roas": None}
    total_impr = int(df["impressions"].sum())
    total_clicks = int(df["clicks"].sum())
    total_conv = int(df["conversions"].sum())
    total_cost = float(df["cost"].sum())
    cvr = (total_conv / total_clicks) if total_clicks > 0 else 0.0
    cpa = (total_cost / total_conv) if total_conv > 0 else None
    # simple value per conversion = $100 for ROAS illustration
    roas = ((total_conv * 100.0) / total_cost) if total_cost > 0 else None
    return {"impressions": total_impr, "clicks": total_clicks, "conversions": total_conv, "cost": total_cost, "cvr": cvr, "cpa": cpa, "roas": roas}

@app.post("/upload/csv", response_model=UploadCSVResponse)
async def upload_csv(file: UploadFile = File(...), session=Depends(get_session)):
    content = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(content))
    except Exception:
        df = pd.read_excel(io.BytesIO(content))
    required = {"Platform", "Impressions", "Clicks", "Conversions", "Cost"}
    if not required.issubset(set(df.columns)):
        raise HTTPException(status_code=400, detail=f"CSV must contain: {sorted(list(required))}")
    if "Date" not in df.columns:
        df["Date"] = datetime.utcnow().date()
    inserted = 0
    for _, row in df.iterrows():
        pm = PlatformMetrics(
            platform=str(row["Platform"]),
            date=pd.to_datetime(row["Date"]).date(),
            impressions=int(row["Impressions"]),
            clicks=int(row["Clicks"]),
            conversions=int(row["Conversions"]),
            cost=float(row["Cost"])
        )
        session.add(pm)
        inserted += 1
    session.commit()
    return {"ok": True, "inserted": inserted}

@app.post("/train/audience")
def train_audience(settings: Settings = Depends(get_settings)):
    model_path = train_lightgbm_stub(settings)
    return {"ok": True, "model_path": model_path}

@app.post("/connectors/harvest", response_model=HarvestResponse)
def connectors_harvest():
    # Stub ingest
    return {"ok": True, "ingested": 42, "sources": ["google_ads", "meta_ads", "tiktok_ads"]}

@app.post("/creative/generate", response_model=CreativeGenResponse)
def creative_generate(topic: Optional[str] = None):
    topic = topic or "Spring sale on pet care"
    headlines = [
        f"{topic}: Save Today!",
        f"{topic}: Limited Time Offer",
        f"{topic}: Shop Now",
    ]
    return {"ok": True, "headlines": headlines}

@app.post("/apply")
def apply(payload: ApplyIn):
    # Stub apply to platforms
    return {"ok": True, "applied": payload.recommendations}
