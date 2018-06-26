import requests
import json

headers = {"Content-Type":"application/json", "Accept":"application/json","Authorization":"Token token=mytoken"}
body = {"name" : "PrakharTestComponentBlahBlah","description": "Test Decsription", "rootWorkspace" : "5b180f4db3da08156a57ecb3"}
url = "http://app.ardoq.com/api/component?org=myorg"

response = requests.post(url,data=body,headers=headers)
json_data = json.loads(response.text)
print(json_data)