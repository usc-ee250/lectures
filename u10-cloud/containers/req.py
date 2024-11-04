import requests
import json
import sys
## json style data
#r = requests.post('http://localhost:5000/scores', json={'score':'70'})

## formdata style
if len(sys.argv) < 2:
    print("Please provide the desired port")
    sys.exit(1)
base_url = 'http://127.0.0.1:' + sys.argv[1] 
r = requests.post(base_url+'/scores', data={'score':'70'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.post(base_url+'/scores', data={'score':'75'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.get(base_url+'/avg')
if r.status_code == 200:
    print("Get average returned: ", r.text)

r = requests.post(base_url+'/scores', data={'score':'85'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.get(base_url+'/avg')
if r.status_code == 200:
    print("Get average returned: ", r.text)

r = requests.get(base_url+'/lookup?index=1')
if r.status_code == 200:
    print("2nd score added ", r.text)

