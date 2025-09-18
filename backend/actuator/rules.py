def apply_rules(kpis: dict) -> dict:
    """Simple advice rules over KPIs."""
    advice = []
    if kpis.get("cpa") and kpis["cpa"] > 50:
        advice.append("CPA high: test new creatives.")
    if (kpis.get("roas") or 0) < 1.0:
        advice.append("Low ROAS: shift spend toward best platform.")
    return {"advice": advice}
