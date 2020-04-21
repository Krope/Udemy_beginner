import urllib.request as ur
import urllib.parse as up
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter location: ")
parametrs = {"sensor": "false", "address": address}
url = serviceurl + up.urlencode(parametrs)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print(data)
print('Retrieved', len(data), 'characters')
json_p = json.loads(data)

place = json_p["results"][0]["place_id"]
print("Place id", place)
