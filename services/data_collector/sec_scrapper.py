import requests
from bs4 import BeautifulSoup

class SECFilings:
    BASE_URL = "https://www.sec.gov/Archives/edgar/data"

    @staticmethod
    def fetch_filings(cik: str, filing_type: str = "10-K"):
        filings = []
        url = f"{SECFilings.BASE_URL}/{cik}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            if filing_type in link.text:
                filings.append(link.get("href"))
        return filings
