import requests

url = 'http://www.localhost:5000/api/add_message/1234'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data=myobj)

print(x.text)