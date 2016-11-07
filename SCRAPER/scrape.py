import requests
from datetime import datetime

def read_api():
    return requests.get('http://wservice.viabicing.cat/v2/stations')

def write_to_logfile(response):
    with open("logfile", "w") as logfile:
        logfile.write(result.text)

def get_stations_list(response):
    response_dict = response.json()
    return response_dict['stations']

# I need 87, 191 and 384
def get_station_by_id(stations_list, id):
    for station in stations_list:
        if station['id'] == str(id):
            return station

def prepare_data_for_post(stations):
    post_list = []
    for station in stations:
        post_list.append({
            'station': station['id'],
            'time': str(datetime.utcnow()),
            'bikes': station['bikes']})
    return post_list
        

if __name__ == '__main__':
    response = read_api()
    stations_list = get_stations_list(response)
    stations = [ 
        get_station_by_id(stations_list, 87),
        get_station_by_id(stations_list, 191),
        get_station_by_id(stations_list, 384)]
    posts_list = prepare_data_for_post(stations)
    for post_data in posts_list:
        requests.post('http://api:5000/station_data/', json=post_data)