import requests

url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"hulu","type":"series","genre":"16","page":"1","keyword":"chi","language":"en"}

headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)