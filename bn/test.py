from datetime import datetime

import requests


def fetch_new_listings():
    url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageNo=1&pageSize=5"
    response = requests.get(url)
    data = response.json()

    new_listings = []
    for catalog in data['data']['catalogs']:
        if catalog['catalogName'] == "New Cryptocurrency Listing":
            for article in catalog['articles']:
                new_listings.append({
                    'title': article['title'],
                    'release_date': datetime.fromtimestamp(article['releaseDate'] / 1000).strftime('%Y-%m-%d %H:8M:%S')
                })
    return new_listings


def display_new_list(new_listings):
    print("###")
    for listing in new_listings:
        print(f"- **{listing['title']}**-发布日期:{listing['release date']}")


if __name__ == '__main__':
    new_listings = fetch_new_listings()
    display_new_list(new_listings)
