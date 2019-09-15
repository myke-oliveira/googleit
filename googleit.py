#! /home/myke/anaconda3/bin/python

import requests, bs4, webbrowser, re

term = input('Enter a term for searching: ')
term = '+'.join(term.split())
print(term)
regex = re.compile(r'http.*')

htmltext = requests.get(f'https://www.google.com.br/search?q={term}')
htmltext.raise_for_status()

soup = bs4.BeautifulSoup(htmltext.text, 'lxml')
for divtag in soup.find_all('div', class_='kCrYT'):
	for atag in divtag.find_all('a'):
		href = atag.get('href')
		match = regex.search(href)
		if match:
			url = match.group()
			print(f'Opening {url}...')
			webbrowser.open(url)
