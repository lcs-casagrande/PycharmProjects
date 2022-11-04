import requests

response = requests.get('https://www.flashscore.com/basketball/usa/nba/results/')

print(response.status_code)
print('>>Header<<')
print(response.headers)
print('\n>>Content<<')
print(response.content)