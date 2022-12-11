test_url = input('Enter your URL: ')
api_key = 'AIzaSyA4gJ8DyvPx15LaoxJ9_RfK2GzOgC8woZQ'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'
import requests
res = requests.get(api_url)
if res.status_code == 200:
    data = res.json()
    cls_score = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
    experimental_interactions = data.get('loadingExperience').get('metrics').get('EXPERIMENTAL_INTERACTION_TO_NEXT_PAINT').get('distributions').get('min')
    print(cls_score)
    print(experimental_interactions)
else:
    print('something wrong')