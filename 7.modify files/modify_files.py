from bs4 import BeautifulSoup
import requests
import re


with open('index.html', 'r') as f:
	file =BeautifulSoup(f, 'html.parser')

tags = file.find_all('input', text='text')
for tag in tags:
	tag['palceholder'] = 'i changed you'

with open('changed.html', 'w') as doc:
	doc.write(str(file))
