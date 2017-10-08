
import http.client
import requests
import json
import re
from .models import suggestion
def matcheschedule():
	dict= {}
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = { 'X-Auth-Token': 'bcfa111e2227403a9491066e8a033df4', 'X-Response-Control': 'minified' }
	connection.request('GET', '/v1/competitions', None, headers )
	response = json.loads(connection.getresponse().read().decode())
	for match in response:
		dict[match['id']]= match['caption']

	print(dict)


	connection1 = http.client.HTTPConnection('api.football-data.org')
	headers1 = { 'X-Auth-Token': 'bcfa111e2227403a9491066e8a033df4', 'X-Response-Control': 'minified' }
	connection1.request('GET', '/v1/fixtures', None, headers1 )
	response1 = json.loads(connection1.getresponse().read().decode())
	fixture= response1['fixtures']
	for match in fixture:
		s= match['date']
		q= suggestion(StartDate=s[0:10],StartTime=s[11:17],Hometeam=match['homeTeamName']
		,Awayteam=match['awayTeamName'],League=dict[match['competitionId']])
		q.save()

	
# fixtures= response['fixtures']

# # for match in fixtures:
# # 	if match['homeTeamName'] in list:
# # 		print( match['hometeamName'] ,match['date'])
# # 	elif match['awayTeamName'] in list:
# # 		print(match['awayTeamName'],match['date'])




# for match in fixtures:
	
# 	print(match['date'],match['homeTeamName'],"\t",match['awayTeamName'])