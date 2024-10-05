import requests
import random
import os
from dotenv import load_dotenv
from atproto import Client

load_dotenv()

email = os.getenv('BLUESKY_EMAIL')
password = os.getenv('BLUESKY_PASSWORD')
pexels_api_key = os.getenv('PEXELS_API_KEY')

pexels_url = 'https://api.pexels.com/v1/search'

image_size_limit = 976.56 * 1024

search_terms = ['furniture', 'wood furniture', 'plastic furniture', 'metal furniture', 'glass furniture',
                'bamboo furniture', 'ceramic furniture', 'bathroom furniture', 'kitchen furniture',
                'restroom furniture', 'bedroom furniture', 'garden furniture', 'office furniture', 'hotel furniture']

random_term = random.choice(search_terms)

results_per_page = 100
max_pages = 5

random_page = random.randint(1, max_pages)

params = {
    'query': random_term,
    'per_page': results_per_page,
    'page': random_page
}

headers = {
    'Authorization': pexels_api_key
}

response = requests.get(pexels_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    
    if data['photos']:
        suitable_image_found = False

        while not suitable_image_found and data['photos']:
            random_image = random.choice(data['photos'])
            
            image_url = random_image['src']['large']
            image_response = requests.get(image_url)
            
            if image_response.status_code == 200:
                image_data = image_response.content

                image_size = len(image_data)

                if image_size <= image_size_limit:
                    suitable_image_found = True

            data['photos'].remove(random_image)
        
        if suitable_image_found:
            image_alt_text = f"{random_term.capitalize()}"

            try:
                client = Client(base_url='https://bsky.social')
                client.login(email, password)
            except Exception as e:
                print(f"Login error: {e}")

            try:
                upload_response = client.send_image(image=image_data, text='', image_alt=image_alt_text)
                    
            except Exception as e:
                print(f"Post creation error: {e}")
        else:
            print("No suitable image found.")
    else:
        print("No image found.")
else:
    print(f"Error on Pexels API: {response.status_code}")
