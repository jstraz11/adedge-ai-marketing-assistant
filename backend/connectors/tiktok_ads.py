from .base import BaseConnector

class TikTokAdsConnector(BaseConnector):
    def harvest(self):
        # stub example
        return {"platform": "TikTok", "rows": 8}
