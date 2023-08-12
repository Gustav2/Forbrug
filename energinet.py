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

    def __init__(self, user_token):
        self.user_token = user_token
        self.refresh_token = self.get_refresh_token()
        self.headers = {
            "Authorization": f"Bearer {self.refresh_token}",
            "accept": "application/json"
        }

