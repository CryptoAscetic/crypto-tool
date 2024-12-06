import requests

headers = {
    'authority': 'servapi.dbotx.com',
    'accept': '*/*',
    'accept-language': 'zh,zh-CN;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://dbotx.com',
    'pragma': 'no-cache',
    'referer': 'https://dbotx.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    'x-api-key': '9uu170guyufzmipfjto5mkww18u6c0uu',
}

params = {
    'duration': '7',
    'isWatched': 'false',
    'page': '0',
    'size': '24',
}

response = requests.get('https://servapi.dbotx.com/smart_wallet/assets/statistics', params=params, headers=headers)

print(response)
