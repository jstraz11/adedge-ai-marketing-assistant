from .base import BaseConnector

class MetaAdsConnector(BaseConnector):
    def harvest(self):
        # stub example
        return {"platform": "Meta", "rows": 12}
