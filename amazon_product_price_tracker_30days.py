import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import matplotlib.pyplot as plt

url = 'https://www.amazon.co.uk/LG-32UN88A-Monitor-IPS-3840x2160-Ergonomic/dp/B088LVN3TW/ref=sr_1_3?geniuslink=true&keywords=lg+32+inch+Ultra+fine+monitor&qid=1670851095&sr=8-3'

prices = []
for i in range(30):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('span', {'class': 'a-price-whole'})
    price = float(price_element.text)
    prices.append(price)

prices_df = pd.DataFrame(prices, columns=['price'])
prices_df['date'] = [datetime.datetime.now() - datetime.timedelta(days=i) for i in range(30)]

prices_df.plot(x='date', y='price')
plt.show()
