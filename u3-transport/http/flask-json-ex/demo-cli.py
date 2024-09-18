import requests
import sys
import json


## json style data
host = "13.64.52.196"  # Azure EE-250
if len(sys.argv) > 1:
    host = sys.argv[1]
# make a dictionary with the appropriate information
myjson = {

}
# make a string with the appropriate URL to the server to send
# a POST request
post_url = ""

r = requests.post('http://' + host + ':5000/submit', json=myjson)
print(f"Status Code: {r.status_code}, Response: {r.text}")

# make a string with the appropriate URL to the server to 
#  check if your POST was successful
check_url = ""
r = requests.get('http://' + host + ':5000/check?name=prof-red')
print(f"Status Code: {r.status_code}, Response: {r.text}")

