import json


class AnalyticsLibrary:
    def analyze(self, data_json):
        print("AnalyticsLibrary received JSON data:")
        print(json.dumps(data_json, indent=2))
