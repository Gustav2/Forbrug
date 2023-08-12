import requests
import json
import datetime


class Norlys:
    endpoint = "https://norlys.dk/api/flexel/getall"

    def get_data(self):
        req = requests.get(self.endpoint)
        json_data = json.loads(req.text)
        return json_data

    def get_data_from_date(self, date: datetime.datetime):
        req = requests.get(self.endpoint)
        json_data = json.loads(req.text)

        for data in json_data:
            price_date = datetime.datetime.strptime(data["PriceDate"], "%Y-%m-%dT%H:%M:%SZ")
            if price_date == date:
                return data



if __name__ == "__main__":
    norlys = Norlys()
    date = datetime.datetime(2023, 1, 1)
    print(date)
    print(norlys.get_data_from_date(date))