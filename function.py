import requests
import random


'''
Let's find a perfect food match !



'''

api_key = '_WRbNCTbDokxy_wfb5q_8dlFN0ZOMyaB4PTZUxiQZVqHRi29zPpVyyduIGbem_m7XIy9oXw408Cu0LcKTncaTnMOeZ2k2-jcFANJAfjZbZ6bAoWXgZ-hTVTcI2lrZnYx'
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": f"Bearer {api_key}",
    "accept": "application/json"
}

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Defaults for our simple example.
term= 'dinner'
location= 'San Francisco'
SEARCH_LIMIT = 3

def get_api(api_key, term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT

    }

    response = requests.get(url, headers=headers, params=url_params)
    data = response.json() 
   
   # Extracting names and image URLs from the JSON response
    businesses = data.get('businesses', [])
    names = [business.get('name') for business in businesses]
    image_urls = [business.get('image_url') for business in businesses]

    return names, image_urls


businesses = get_api(api_key, term, 'NYC')
print(businesses)




