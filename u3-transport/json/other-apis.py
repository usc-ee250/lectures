import requests
import json
#https://open.er-api.com/v6/latest/USD
ron_swanson_url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

num = int(input("How many Ron Swanson quotes do you want to view?"))
resp = requests.get(ron_swanson_url + "/" + str(num))
#print(resp.text)
quotes = json.loads(resp.text)
for q in quotes:
	print(q)
