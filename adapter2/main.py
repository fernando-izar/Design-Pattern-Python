from core.stock_data_provider import StockDataProvider
from libs.analytics_library import AnalyticsLibrary
from adapters.analytics_adapter import AnalyticsAdapter


def main():
    provider = StockDataProvider()
    xml_data = provider.get_stock_data()

    analytics_lib = AnalyticsLibrary()
    adapter = AnalyticsAdapter(analytics_lib)

    adapter.analyze(xml_data)


if __name__ == "__main__":
    main()
