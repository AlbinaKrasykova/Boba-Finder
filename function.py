import requests

API_KEY = 'D66se69oJo4Oyj1_ljAnQ8aeU_5QwmyVmGZdfaiEyYKWObGZ8_yS88UUp3YVZdSmRAYwn7eZLblU2icLS2D5MGSz4bIMC5gLlQePQQxRFvqeBmtYwKKzs5S6gsYyZnYx'
url = "https://api.yelp.com/v3/businesses/search"
headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }

def get_api(theme, location, limit):
    
    
    params = {
        "term": theme,  # Specify your search term here
        "location": location,  # Specify the location
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        businesses = data.get('businesses', [])
        if businesses:
            for business in businesses:
                name = business.get('name')
                rate = business.get('rating')
                img = business.get('image_url')

                print("Name:", business.get('name'))
                print("Rating:", business.get('rating'))
                print("Image URL:", business.get('image_url'))
                print()
        else:
            print("No businesses found.")
    else:
        print("Failed to retrieve data:", response.status_code)
    return name, rate, img

get_api('Boba', 'NYC', 3)