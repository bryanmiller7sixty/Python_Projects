import time
import requests
endpoint = r"https://api.tdameritrade.com/v1/marketdata/chains"
payload = {'apikey': '', #this is where your API key goes for your application
           'symbol': 'TSLA',
           'contractType': 'CALL',
           'strikeCount': '2',
           'includeQuotes': 'TRUE',
           'toDate': '2020-12-24'
           }

content = requests.get(url=endpoint, params=payload)
data = content.json()
"""
//This info is for the stock price
****print("Bid price: " + str(data['underlyingPrice']['bid']))
****print("Ask price " + str(data['underlying']['ask']))
****print("Mark " + str(data['underlying']['mark']))
"""


"""
**The date is completely dependent on the date your accessing this data/how many strikes you requested, the 24th is the 
**expiration
**Same for the strike price, since I requested only 2 strikes above the underlying, that's the data that can be accessed
**Since it seemed like there was only 1 index within the list, index 0 was accessed
**Finally you will be able to access the keys which will vary
**To really access this data each time methods dir(), type(), keys(), values() will need to be used because the types 
**holding the values will change depending on what your trying to access
**
//if all fails you can use the for loop after requesting the strike
for x in data['callExpDateMap']['2020-12-24:1']['640.0']:
    print(x['bid'])
**
"""

print("Underlying price at time of quote: " + str(data['underlyingPrice']))
print("Description: " + str(data['callExpDateMap']['2020-12-24:1']['645.0'][0]['description']))
print("Bid: " + str(data['callExpDateMap']['2020-12-24:1']['645.0'][0]['bid']))
print("Ask: " + str(data['callExpDateMap']['2020-12-24:1']['645.0'][0]['ask']))
print("Mark: " + str(data['callExpDateMap']['2020-12-24:1']['645.0'][0]['mark']))

#Divde by 1000 since the epoch returned is in milli seconds
print("Quote time " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['underlying']['quoteTime']/1000.0))))





