import requests
api_url = 'https://api.ipify.org?format=json'
def res_data(url):
    if res.status_code == 200:
        data = res.json()
        return data



# res = requests.get(api_url)
# if res.status_code == 200:
#     data = res.json()

data = res_data(api_url)
ip_address = data.get('ip')
ip_api_location = f'https://ipapi.co/{ip_address}/json/'

ip_details = res_data(ip_api_location)
# r = requests.get(ip_api_location)
# if r.status_code == 200:
#     ip_details = r.json()
city = ip_details.get('city')
region = ip_details.get('region')
country_code = ip_details.get('country_code')

text = f'IP ({ip_address}) is located in {city}, {region}, {country_code}'
print(text)
