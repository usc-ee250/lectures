import requests
import json

## json style data
#r = requests.post('http://localhost:5000/scores', json={'score':'70'})

## formdata style
r = requests.post('http://13.64.52.196:5000/scores', data={'score':'70'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

