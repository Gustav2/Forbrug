import requests
import json
import os
from energinet import Energinet

FETCH_DAYS = "10"
NORLYS_ENDPOINT = f"https://norlys.dk/api/flexel/getall?days={FETCH_DAYS}&sector=DK1&isBusiness=false"


def get_norlys_price_info():
    req = requests.get(NORLYS_ENDPOINT)
    json_data = json.loads(req.text)
    return json_data


if __name__ == "__main__":
    energinet = Energinet(os.environ["ENERGINET_TOKEN"])
    print(energinet.get_metering_point_id())
