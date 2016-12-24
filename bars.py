import json
f=open('data.json','r',encoding='UTF-8')
a=json.load(f)
for i in a:
    print (i['Name'])
