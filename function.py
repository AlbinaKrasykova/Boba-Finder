import requests
import random

API_KEY = 'D66se69oJo4Oyj1_ljAnQ8aeU_5QwmyVmGZdfaiEyYKWObGZ8_yS88UUp3YVZdSmRAYwn7eZLblU2icLS2D5MGSz4bIMC5gLlQePQQxRFvqeBmtYwKKzs5S6gsYyZnYx'
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

def get_api(theme, location):
    params = {
        "term": theme,      # Specify your search term here
        "location": location,  # Specify the location
        
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        businesses = data.get('businesses', [])
        
        if businesses:
            num = len(businesses)
            random_num = range(0, num)
            random_num = random.choice(random_num)
            
            random_business = businesses[random_num]
           
            name = random_business.get('name')
            rate = random_business.get('rating')
            img = random_business.get('image_url')

            print("Name:", name)
            print("Rating:", rate)
            print("Image URL:", img)
            print()
        else:
            print("No businesses found.")
    else:
        print("Failed to retrieve data:", response.status_code)
    return name, img, rate

get_api('Boba', 'NYC')
