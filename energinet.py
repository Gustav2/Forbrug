import json
import requests
import datetime


class Energinet:
    endpoint = "https://api.eloverblik.dk/customerapi/api"
    user_token = ""
    refresh_token = ""
    headers = ""

    def get_refresh_token(self):
        req = requests.get(self.endpoint + "/token",
                           headers={
                               "Authorization": f"Bearer {self.user_token}",
                               "Content-Type": "application/json"
                           })

        return req.json()["result"]

    def get_metering_point_id(self):
        req = requests.get(self.endpoint + "/meteringpoints/meteringpoints", headers=self.headers)
        json_data = json.loads(req.text)
        return json_data["result"][0]["meteringPointId"]

    def get_usage_from_date(self, date: datetime.datetime):
        next_day = date + datetime.timedelta(days=1)
        req = requests.post(
            self.endpoint + f"/meterdata/gettimeseries/{date.strftime('%Y-%m-%d')}/{next_day.strftime('%Y-%m-%d')}/Hour",
            json={
                "meteringPoints": {
                    "meteringPoint": [
                        self.get_metering_point_id()
                    ]
                }
            },
            headers=self.headers)
        json_data = json.loads(req.text)["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"][0]["Period"][0]["Point"]

        price_data = []
        for amount in json_data:
            price_data.append(float(amount["out_Quantity.quantity"]))
        return price_data

    def __init__(self, user_token):
        self.user_token = user_token
        self.refresh_token = self.get_refresh_token()
        self.headers = {
            "Authorization": f"Bearer {self.refresh_token}",
            "accept": "application/json"
        }
