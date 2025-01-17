import yfinance as yf

class YahooFinance:
    @staticmethod
    def fetch_historical_data(ticker: str, start_date: str, end_date: str):
        stock = yf.Ticker(ticker)
        return stock.history(start=start_date, end=end_date)

    @staticmethod
    def fetch_metadata(ticker: str):
        stock = yf.Ticker(ticker)
        return stock.info
