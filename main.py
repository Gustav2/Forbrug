import requests
import json
import os
import time
from energinet import Energinet
from norlys import Norlys


if __name__ == "__main__":
    energinet = Energinet(os.environ["ENERGINET_TOKEN"])
    print(energinet.get_metering_point_id())
