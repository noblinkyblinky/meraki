import requests
import json

# This is the org id of the Meraki org you wish to access - usually 6 numeric characters
orgId = "123456"
# This is the network id of the network you wish to access - starts with N_
netId = "N_86753098675309"
# This is the serial number of the devices you want to pull CDP/LLDP info from
serial = "Q123-1234-1234"
# The time in seconds you want the information for. ex: 86400 = 24 hours
timespan = "86400"
# Your API key
apikey = "paste your token here"

# Build the request URL
url = "https://dashboard.meraki.com/api/v1/organizations/" + orgId + "/networks/" + netId + "/devices/" + serial + "/lldp_cdp?timespan=" + timespan + " "

# API Payload and Headers
payload={}
headers = {
  'X-Cisco-Meraki-API-Key': apikey,
  'Accept-en': 'application/json'
}

#Get the response back and dump into json format
response = requests.get(url, headers=headers, data=payload).json()

#Print the response in json format
print(json.dumps(response, indent=2, sort_keys=True))