import json
from urllib.request import urlopen
import datetime

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

'''
route-schedules : 	route, scheduled-stops
					route : key/number, name, coverage

					scheduled-stops : cancelled, 	times , variant, bus
													times : arrival , departure
													variant: key, name
'''

def calcWaitTime(est): 
	now = str(datetime.datetime.now())
	now = now[11:19]
	e_hrs = int(est[:2])
	e_min = int(est[3:5])
	n_hrs = int(now[:2])
	n_min = int(now[3:5])
	wait_time =  str(e_hrs-n_hrs) + ":" + str(e_min-n_min)

	return wait_time




for route_schedules in data['stop-schedule']['route-schedules']:
	#print(route_schedules)
	bus_keys = route_schedules['route']['key']
	coverage = route_schedules['route']['coverage']
	for keys in route_schedules['scheduled-stops']:
		cancelled = keys['cancelled']
		arr_est_time = keys['times']['arrival']['estimated']
		arr_est_time =  arr_est_time[11:]
		name = keys['variant']['name']
		wait_time = calcWaitTime(arr_est_time)
	stop_routes[bus_keys] = name, wait_time#,coverage,cancelled,arr_est_time

for i in stop_routes:
	if cancelled == 'false':
		print(stop_routes)


# routes = json.dumps( (data['stop-schedule']['route-schedules']), indent=2 )
# print(routes)

# print(json.dumps(data, indent=2))

