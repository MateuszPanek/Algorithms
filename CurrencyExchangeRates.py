import requests
import numpy as np
import pandas as pd
from pprint import pprint as pp


class Currency:
    def __init__(self):
        self.resp = resp
        self.data_frame = data_frame

    def frame_the_data(self):
        pass

resp1 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json')
resp = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/last/30/?format=json')
res3 = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/2019-08-01/2019-09-21/?format=json')

rates = res3.json()['rates']
df = pd.DataFrame(rates)
# df.to_excel('r.xlsx')  # tworzy plik excel z danymi wczytanymi za pomocą powyższego kodu


