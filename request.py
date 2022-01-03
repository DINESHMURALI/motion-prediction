import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'X':0.63, 'Y':9.70, 'Y':1.24})

print(r.json())