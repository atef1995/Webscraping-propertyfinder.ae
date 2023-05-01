"""
A script that extracts real estate property data from PropertyFinder.ae.

This script uses BeautifulSoup and Requests libraries to extract data from the PropertyFinder.ae website
and save it as a CSV file.

The user can specify the search criteria (location, property type, min/max price, etc.) using the command line arguments.

Usage:
    python propertyfinder.py [-h] [-o OUTPUT_FILE] [-l LOCATION] [-p PROPERTY_TYPE] [-min MIN_PRICE] [-max MAX_PRICE]

    -h, --help          Show this help message and exit
    -o, --output        Output file path (default: 'propertyfinder.csv')
    -l, --location      Property location
    -p, --property      Property type (e.g. apartment, villa, townhouse)
    -min, --min-price   Minimum price (in AED)
    -max, --max-price   Maximum price (in AED)

Examples:
    python propertyfinder.py -l 'Dubai Marina' -p 'apartment' -min 500000 -max 1000000
    python propertyfinder.py -o 'my_properties.csv' -p 'villa' -min 2000000
"""

import argparse
import csv
import requests
from bs4 import BeautifulSoup


def get_properties(location=None, property_type=None, min_price=None, max_price=None):
    """
    Scrapes property data from PropertyFinder.ae.

    Args:
        location: Property location
        property_type: Property type (e.g. apartment, villa, townhouse)
        min_price: Minimum price (in AED)
        max_price: Maximum price (in AED)

    Returns:
        A list of dictionaries containing property data (title, price, location, type, area, bedrooms, bathrooms)
    """
    print("Starting.")
    # Construct the search URL based on the search criteria
    search_url = "https://www.propertyfinder.ae/en/search?"
    params = {
        "c": "1",
        "ob": "mr",
        "page": "1",

    }

    if min_price:
        params["pf"] = min_price

    if max_price:
        params["pt"] = max_price

    print(params)

    search_url = search_url.format(property_type=property_type, location=location)
    search_url += "&".join([f"{k}={v}" for k, v in params.items()])
    
    print(search_url)

    # Send a GET request to the search URL
    response = requests.get(search_url,headers={'User-Agent': 'Custom'})

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser",)

    # Extract the search results
    results = soup.find_all("div",{"class":"card-list__item"})
    # print(results)

    # Extract the property data from each search result
    with open('output.csv', 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title','price','location'])
        for result in results:
            title = result.find("p", {"class":"card-intro__type"}).text.strip().replace("\n"," ").replace(" "," "*1)
            price = result.find("p", {"class":"card-intro__price"}).text.strip().replace("\n"," ").replace(" ","")
            location = result.find("span", {"class":"card-specifications__location-text"}).text.strip().replace("\n","").replace(" ","")
            # area = result.find("div", {"class":"card__property-amenity card__property-amenity--area"}).text.strip()
            # bedrooms = result.find("div", {"class":"card__property-amenity card__property-amenity--bedroom"}).text.strip()
            # bathrooms = result.find("div", {"class":"card__property-amenity card__property-amenity--bathroom"}).text.strip()

            # property_data = [
            #     [title],
            #     [price],
            #     [location],
            # ]
                # "area":area,
                # "bedrooms":bedrooms,
                # "bathrooms":bathrooms

                # Create a CSV writer object

            # Write each row of data
            
            writer.writerow([title,price,location])

if __name__ == "__main__":
    get_properties("dubai","properties",1,1000000)