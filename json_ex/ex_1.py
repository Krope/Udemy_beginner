# This program prompt the user for a search string (a location)
# call the Google geocoding API and extract information
# from the returned JSON (in this exercise is the two-character country code)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = "..."

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("=== Failure To Retrieve ===")
        print(data)
        continue

    if "country" in js["results"][0]["address_components"][-1]["types"]:
        country_code = js["results"][0]["address_components"][-1]["short_name"]
        print("Country code:", country_code)
    else:
        print("This location is not in any country! Cannot return country code.")
