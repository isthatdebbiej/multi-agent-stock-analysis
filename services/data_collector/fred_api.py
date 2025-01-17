import requests

class FREDData:
    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_series(self, series_id: str, start_date: str, end_date: str):
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "observation_start": start_date,
            "observation_end": end_date,
        }
        response = requests.get(self.BASE_URL, params=params)
        return response.json().get("observations", [])
