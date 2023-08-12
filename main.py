import requests
import json
import os
import datetime
from energinet import Energinet
from norlys import Norlys


if __name__ == "__main__":
    energinet = Energinet(os.environ["ENERGINET_TOKEN"])
    print(energinet.get_usage_from_date(datetime.datetime(2023, 7, 10)))

    norlys = Norlys()
    print(norlys.get_data_from_date(datetime.datetime(2023, 7, 10)))

