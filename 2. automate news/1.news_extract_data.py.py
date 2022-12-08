from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = '/Users/hellosongi/Desktopchromedriver' 

#creating a driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(web)

#finding element in HTML website
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')


titles = []
subtitles = []
links = []

for container in containers:
	title = container.find_element(by='xpath', value='./a/h3').text
	sub_title = container.find_element(by='xpath', value='./a/p').text
	link = container.find_element(by='xpath', value='./a').get_attribute('href')

	titles.append(title)
	subtitles.append(sub_title)
	links.append(link)

my_dict = {'title': titles, 'sub_title': subtitles, 'link': links}
df_headlines = pd.Dataframe(my_dict)
df_headlines.to_csv('df_headline.csv')

driver.quit()