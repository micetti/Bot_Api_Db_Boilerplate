import requests

r = requests.post('http://configuration-service.slingshot.eu-west-1.prod.aws.skyscanner.local/api/services', 
    json = {
        "service_name": "hotels-front-end-aws",
        "squad_name": "hotels web front end",
        "traffic_config": "true",
        "environments": ["pre-prod", "prod"]
})

print(r.text)
print(r.content)
print(r.json())
print(r.raw)
