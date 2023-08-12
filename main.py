import requests
import json
import os
import datetime
from energinet import Energinet
from norlys import Norlys

if __name__ == "__main__":
    energinet = Energinet(os.environ["ENERGINET_TOKEN"])
    energinet_usage = energinet.get_usage_from_date(datetime.datetime(2023, 8, 1))

    norlys = Norlys()
    norlys_prices = norlys.get_data_from_date(datetime.datetime(2023, 8, 1), add_fees=True)

    total_prices = []
    for i in range(len(energinet_usage)):
        total_prices.append(energinet_usage[i] * norlys_prices[i])

    print("Total pris", round(sum(total_prices)/100, 3), "kr")
    print("Total energi", sum(energinet_usage), "kWh")
