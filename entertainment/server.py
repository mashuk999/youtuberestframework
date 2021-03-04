import requests

# r = requests.post('http://127.0.0.1:8000/entertainx/', data ={'title': 'Entertainment', 'date': '2021-03-04T11:42:27Z'})

# print(r)
# print content of request
# print(r.json())


r=requests.get('http://127.0.0.1:8000/entertainx/')
print(r.json()['title'])