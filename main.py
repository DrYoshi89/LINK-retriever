from unittest import result
from apiclient import discovery
import webbrowser, requests, json, bs4
from support import api_key, search_engine

search = input("Enter search here: ")

url1 = "https://www.googleapis.com/customsearch/v1"
parameters= {"q": search,
			"cx": search_engine,
			"key": api_key
			}

page = requests.request("GET", url1, params=parameters)
results = json.loads(page.text)

results['items']
link_list = [item['link'] for item in results['items']]

print(link_list)

for link in link_list:
    url2= link
    res = requests.get(url2)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(soup.prettify())