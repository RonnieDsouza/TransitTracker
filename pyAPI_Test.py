import json
from urllib.request import urlopen

api_key = "9Ld737shDDwqfsXWSZ3m"

stops_link = "https://api.winnipegtransit.com/v3/stops/60105/schedule.json?api-key=9Ld737shDDwqfsXWSZ3m"

with urlopen(stops_link) as response:
	source = response.read()

# print(source)

data = json.loads(source)

stop = json.dumps( (data['stop-schedule']['stop']), indent=2 ) 

# for routes in data['stop-schedule']:
# 	del routes['stop']

stop_routes = dict()

for routes in data['stop-schedule']['route-schedules']:
	for keys in routes['scheduled-stops']:
		yes = keys['cancelled']
		arr_est_time = keys['times']['arrival']['estimated']
		print(arr_est_time)
	bus_keys = (routes['route']['key'])



# routes = json.dumps( (data['stop-schedule']['route-schedules']), indent=2 )
# print(routes)

# print(json.dumps(data, indent=2))

