import json
import urllib.request,urllib.parse,urllib.error
import ssl

ctx=ssl.create_default_context
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

num_list=[]
url=input('Enter url:')
acc=urllib.request.urlopen(url,context=ctx).read()
data=json.loads(acc)
print(data['comments'])
print('=================================')
for item in data['comments']:
    num_list.append(item['count'])
num_list=[int(i) for i in num_list]
print('Sum=%d'%sum(num_list))
