from .base import BaseConnector

class GoogleAdsConnector(BaseConnector):
    def harvest(self):
        # stub example
        return {"platform": "Google", "rows": 10}
