class StockDataProvider:
    def get_stock_data(self):
        return """
        <stocks>
            <stock>
                <symbol>AAPL</symbol>
                <price>195.55</price>
            </stock>
            <stock>
                <symbol>GOOGL</symbol>
                <price>2731.50</price>
            </stock>
        </stocks>
        """
