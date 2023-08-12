import requests
import json
import datetime


class Norlys:
    ENDPOINT = "https://norlys.dk/api/flexel/getall"
    NET_FEE = 0
    ENERGY_FEE = 14
    STATE_FEE = 87

    def add_fees(self, prices):
        new_prices = []
        for price in prices:
            new_prices.append(price + self.NET_FEE + self.ENERGY_FEE + self.STATE_FEE)
        return new_prices

    def get_data(self):
        req = requests.get(self.ENDPOINT)
        json_data = json.loads(req.text)
        return json_data

    def get_data_from_date(self, date: datetime.datetime, add_fees=True):
        req = requests.get(self.ENDPOINT)
        json_data = json.loads(req.text)

        for data in json_data:
            price_date = datetime.datetime.strptime(data["PriceDate"], "%Y-%m-%dT%H:%M:%SZ")
            if price_date == date:
                prices = []
                for price in data["DisplayPrices"]:
                    prices.append(price["value"])
                if add_fees:
                    return self.add_fees(prices)
                return prices


if __name__ == "__main__":
    norlys = Norlys()
    date = datetime.datetime(2023, 1, 1)
    print(date)
    print(norlys.get_data_from_date(date))
