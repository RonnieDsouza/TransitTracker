import json
from urllib.request import urlopen
from datetime import datetime

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

# returns a timedelta object thats the difference of now and estimated_time parameter
# parses the estimated_time parameter into a dateitme object to allow for calculations
def calcWaitTime(estimated_time, now = datetime.now(), interval = 'default'): 
	
	est_year = int(estimated_time[:4])
	est_month = int(estimated_time[5:7])
	est_day = int(estimated_time[8:10])
	est_hour = int(estimated_time[11:13])
	est_min = int(estimated_time[14:16])
	est_sec = int(estimated_time[17:19])
	
	est_datetime = datetime(est_year,est_month,est_day,est_hour,est_min,est_sec)
	print(est_datetime)

	duration = est_datetime - now
	# print(duration)
	return str(duration);



for route_schedules in data['stop-schedule']['route-schedules']:
	#print(route_schedules)
	bus_keys = route_schedules['route']['key']
	coverage = route_schedules['route']['coverage']
	for keys in route_schedules['scheduled-stops']:
		cancelled = keys['cancelled']
		arr_est_time = keys['times']['arrival']['estimated']
		# arr_est_time =  arr_est_time[11:]
		name = keys['variant']['name']
		wait_time = calcWaitTime(arr_est_time)
	stop_routes[bus_keys] = name, wait_time#,coverage,cancelled,arr_est_time

for i in stop_routes:
	if cancelled == 'false':
		print(stop_routes)


# routes = json.dumps( (data['stop-schedule']['route-schedules']), indent=2 )
# print(routes)

# print(json.dumps(data, indent=2))

