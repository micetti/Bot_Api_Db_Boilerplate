import requests

r = requests.post('http://0.0.0.0:5000/echo/', json = {'message':'hey, ho, dude'})

print(r.text)