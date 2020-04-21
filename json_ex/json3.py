import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'charcters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js['status'] != 'OK':
        print('=== Failure To Tetrieve ===')
        print(data)
        continue

    lst = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]['formatted_address']
    print(location)
