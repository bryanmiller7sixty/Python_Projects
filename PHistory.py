import requests
"""
*     Plug in parameters in the payload, which uses epoch notation to define start/end date.
*     Charts will be reflective of  1D 1M
*     Start time in GMT is 2:30-9:00 which will be market open/close 
*     After hours chart can be requested, however since this data will be used to analyze options prices
*     That associated info isn't necessary (options can only be traded open-close) 
*     Data['candles'] list is looped through because the list contains
"""
count = 0
sum = 0
#EPOCH notation in milliseconds is required
#Ticker symbol is requested in format method
endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('TSLA')
payload = {'apikey': '', #API key goes here
           'periodType': 'month',
           'frequencyType': 'daily',
           'frequency': '1',
           'period': '1',
           'endDate': '1608584400000',
           'startDate': '1606833000000',
           'needExtendedHoursData': 'true'
           }
#Prints the average daily change over a month for specified ticker symbol
content = requests.get(url=endpoint, params=payload)
data = content.json()
for x in data['candles']:
    print("HERE")
    count += 1
    print("Difference daily: " + str(x['close'] - x['open']))
    sum += x['close'] - x['open']
print("Total sum: " + str(sum) + " Total count " + str(count))
print("Average move over a month to date: " + str(sum / count))

