import requests
from b4s import BeautifulSoup

url = u'https://twitter.com/search?q='

r = requests.get(url+query)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('P', class_='tweet-text')]

print(tweets)
$ python3 twitter-search.py
[]
