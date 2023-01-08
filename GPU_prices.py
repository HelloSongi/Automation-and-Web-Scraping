from bs4 import BeautifulSoup
import requests


url = 'https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product'
result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')

prices = soup.find_all(text='$')
parent = prices[0].parent
strong = parent.find('strong')
print(strong.string)