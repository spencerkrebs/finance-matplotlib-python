import requests
import json
from matplotlib import pyplot as plt
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AMD,IBM,AAPL,NKE,TSLA,FB,AMZN,NFLX"}
headers = {
    'x-rapidapi-key': "24490f5883msh477cb23b4acd9cep15a54ejsndf8c7b9a723a",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
tickerAndPriceToBook = {}
for company in data['quoteResponse']['result']:
    symbol = company['symbol']
    priceToBook = company['priceToBook']
    tickerAndPriceToBook[symbol] = priceToBook

sortedDict = sorted(tickerAndPriceToBook.items(), key=lambda item: item[1])

xvals = []
yvals = []

for obj in sortedDict:
    xvals.append(obj[0])
    yvals.append(obj[1])

fig, ax = plt.subplots()
ax.set(xlabel='Ticker', ylabel = 'Price-To-Book Value')
ax.title('Sorted Plot-To-Book Values of Public Companies')
ax.scatter(xvals,yvals)
plt.show()