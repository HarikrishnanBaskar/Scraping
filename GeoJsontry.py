import urllib.request,urllib.parse,urllib.error
import json
import ssl

ctx=ssl.create_default_context()
ssl.check_hostname=False
ssl.verify_mode=ssl.CERT_NONE

api_key=42
service_url='http://py4e-data.dr-chuck.net/json?'
params=dict()
while True:
    Address=input('Enter Address:')
    params['address']=Address
    params['key']=api_key
    url=service_url+urllib.parse.urlencode(params)
    print(url)
    print('=================================')
    entry=urllib.request.urlopen(url,context=ctx).read()
    data=json.loads(entry)
    print(data['results'][0]['place_id'])
