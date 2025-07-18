import xml.etree.ElementTree as ET
from libs.analytics_library import AnalyticsLibrary


class AnalyticsAdapter:
    def __init__(self, analytics_lib: AnalyticsLibrary):
        self.analytics_lib = analytics_lib

    def analyze(self, xml_data: str):
        root = ET.fromstring(xml_data)
        result = []

        for stock in root.findall("stock"):
            symbol = stock.find("symbol").text
            price = float(stock.find("price").text)
            result.append({"symbol": symbol, "price": price})

        self.analytics_lib.analyze(result)
