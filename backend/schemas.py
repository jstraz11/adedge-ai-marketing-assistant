from pydantic import BaseModel
from typing import List, Optional

class AudienceOut(BaseModel):
    id: int
    segment: str
    score: float

class CreativeOut(BaseModel):
    id: int
    name: str
    ctr: float
    cvr: float

class BudgetRec(BaseModel):
    platform: str
    share: float
    rationale: str

class BestOut(BaseModel):
    platform: str
    score: float
    window_days: int

class ReportOut(BaseModel):
    impressions: int
    clicks: int
    conversions: int
    cost: float
    cvr: float
    cpa: Optional[float] = None
    roas: Optional[float] = None

class UploadCSVResponse(BaseModel):
    ok: bool
    inserted: int

class RecommendationsOut(BaseModel):
    recommendations: List[BudgetRec]

class ApplyIn(BaseModel):
    recommendations: List[BudgetRec]

class HarvestResponse(BaseModel):
    ok: bool
    ingested: int
    sources: List[str]

class CreativeGenResponse(BaseModel):
    ok: bool
    headlines: List[str]
