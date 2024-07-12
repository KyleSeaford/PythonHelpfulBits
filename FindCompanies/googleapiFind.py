import requests
import json
import re
from openpyxl import Workbook

# Google Places API Key
# MARK: CHANGE
API_KEY = 'YOUR_API_KEY'

# Categories that will be searched for
CATEGORIES = [
    {'category_id': '12345', 'category_name': 'Accountancy'},
    {'category_id': '67890', 'category_name': 'Law'},
    {'category_id': '11111', 'category_name': 'Finance'},
    {'category_id': '20001', 'category_name': 'Real Estate'},
    {'category_id': '20002', 'category_name': 'Retail'},
    {'category_id': '20003', 'category_name': 'Restaurants'},
    {'category_id': '20004', 'category_name': 'Health and Wellness'},
    {'category_id': '20005', 'category_name': 'Education'},
    {'category_id': '20006', 'category_name': 'Automotive'},
    {'category_id': '20007', 'category_name': 'Travel and Tourism'},
    {'category_id': '20008', 'category_name': 'Entertainment'},
    {'category_id': '20009', 'category_name': 'E-commerce'},
    {'category_id': '20010', 'category_name': 'Technology'},
    {'category_id': '20011', 'category_name': 'Home Services'},
    {'category_id': '20012', 'category_name': 'Manufacturing'},
    {'category_id': '20013', 'category_name': 'Nonprofit Organizations'},
    {'category_id': '20014', 'category_name': 'Hospitality'},
    {'category_id': '20015', 'category_name': 'Construction'},
    {'category_id': '20016', 'category_name': 'Sports and Fitness'},
    {'category_id': '20017', 'category_name': 'Events and Conferences'},
    {'category_id': '20018', 'category_name': 'Beauty and Personal Care'},
    {'category_id': '20019', 'category_name': 'Consulting'},
    {'category_id': '20020', 'category_name': 'Insurance'},
    {'category_id': '20021', 'category_name': 'Logistics and Transportation'},
    {'category_id': '20022', 'category_name': 'Media and Publishing'},
    {'category_id': '20023', 'category_name': 'Medical and Dental Services'},
    {'category_id': '20024', 'category_name': 'Telecommunications'},
    {'category_id': '20025', 'category_name': 'Agriculture'},
    {'category_id': '20026', 'category_name': 'Pharmaceuticals'},
    {'category_id': '20027', 'category_name': 'Pet Services'},
    {'category_id': '20028', 'category_name': 'Legal Services'},
    {'category_id': '20029', 'category_name': 'Human Resources and Recruitment'},
    {'category_id': '20030', 'category_name': 'Energy and Utilities'}
]


# Google Places API Base URL
PLACES_API_BASE_URL = 'https://maps.googleapis.com/maps/api/place'

# Directory to save the companies
# MARK: CHANGE
COMPANY_DIR = 'YOUR_DIRECTORY_PATH'


# This searches for companies based on the location, radius, keyword and api key
def search_companies(location, radius, keyword, api_key):
    url = f"{PLACES_API_BASE_URL}/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'keyword': keyword,
        'key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# This gets the details of the place
def get_place_details(place_id, api_key):
    url = f"{PLACES_API_BASE_URL}/details/json"
    params = {
        'place_id': place_id,
        'key': api_key,
        'fields': 'name,formatted_address,geometry,website,formatted_phone_number'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Ensures the filename is valid
def sanitize_filename(filename, max_length=255):
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    if len(filename) > max_length:
        filename = filename[:max_length]
    return filename

# This finds and posts the companies to an excel file within a radius of 50km of the location
def find_and_post_companies(category, keyword, latitude, longitude, radius=50000):
    location = f'{latitude},{longitude}'
    
    try:
        search_results = search_companies(location, radius, keyword, API_KEY)
        print(f"Search Results: {json.dumps(search_results, indent=2)}")  # Debug: Print the raw search results
    except requests.RequestException as e:
        print(f"Error during search: {e}")
        return
    
    wb = Workbook()
    sheet = wb.active
    sheet.append(["Category ID", "Company Name", "Address", "Latitude", "Longitude", "Email", "Phone", "Website", "Google Maps Link"])
    
    companies = search_results.get('results', [])
    print(f"Found {len(companies)} companies for category {category['category_name']}")

    if not companies:
        print("No companies found.")
        return
    
    # MARK: CHANGE
    # change to the amount of companies you want to search per category
    companies = companies[:5]
    
    for company in companies:
        place_id = company['place_id']
        
        try:
            details = get_place_details(place_id, API_KEY)
            print(f"Place Details: {json.dumps(details, indent=2)}")  # Debug: Print the place details
        except requests.RequestException as e:
            print(f"Error fetching details for place_id {place_id}: {e}")
            continue
        
        result = details.get('result', {})
        
        row = [
            category['category_id'],
            result.get('name'),
            result.get('formatted_address'),
            result.get('geometry', {}).get('location', {}).get('lat'),
            result.get('geometry', {}).get('location', {}).get('lng'),
            None,  # Email is not typically available through Places API
            result.get('formatted_phone_number'),
            result.get('website'),
            f"https://www.google.com/maps/place/?q=place_id:{place_id}"
        ]
        
        sheet.append(row)
    
    # Save the results to an Excel file for each category
    filename = sanitize_filename(f"companies_{category['category_name']}.xlsx")
    wb.save(filename)
    print(f"Saved results to {filename}")

def main():
    for category in CATEGORIES:
        keyword = category['category_name']
        # MARK: CHANGE
        # change the latitude and longitude to the location you want to search, currently set to Macclesfield, Uk
        latitude = 53.2606635
        longitude = -2.1255158
        find_and_post_companies(category, keyword, latitude, longitude)

if __name__ == '__main__':
    main()
