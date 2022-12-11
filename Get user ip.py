api_url = 'https://api.ipify.org?format=json'
import requests
res = requests.get(api_url)

if res.status_code == 200:
    data = res.json()
    ip = data.get('ip')
ip_api_location = f'https://ipapi.co/{ip}/json/'

r = requests.get(ip_api_location)
if r.status_code == 200:
    ip_details = r.json()
    city = ip_details.get('city')
    region = ip_details.get('region')
    country_code = ip_details.get('country_code')
sentence = f'IP ({ip}) is located in {city}, {region}, {country_code}'
print(sentence)
