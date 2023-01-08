from bs4 import BeautifulSoup
import requests
import re


url = 'https://coinmarketcap.com/'
result = requests.get(url).text 
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.tbody
trs = tbody.contents

prices = {}
for tr in trs[:10]:
	name, price =  tr.contents[2:4]
	crypto_name = name.p.string
	crypto_price = price.a.string

	prices[crypto_name] = crypto_price

print(prices)