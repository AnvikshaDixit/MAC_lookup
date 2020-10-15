import requests,json

# Enter the MAC address
val = input("Please enter the MAC address = ")

#Concatenate the url with API url
url = "https://api.macaddress.io/v1?apiKey=at_H69ZaLRmvUBU8hCuJKeE1SUOSDHew&output=json&search="+val
response = requests.get(url)
#Converting the response to json and then getting the company name from the JSON data
json_response = json.dumps(response.json())
resp_dict = json.loads(json_response)
print("The Company name for ",val,"MAC Address is = ", resp_dict['vendorDetails']['companyName'])