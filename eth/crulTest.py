import requests

headers = {
    'authority': 'servapi.dbotx.com',
    'accept': '*/*',
    'accept-language': 'zh,zh-CN;q=0.9',
    'origin': 'https://dbotx.com',
    'referer': 'https://dbotx.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-api-key': '',
}

params = {
    'duration': '7',
    'isWatched': 'false',
    'page': '0',
    'size': '24',
}

response = requests.get('https://servapi.dbotx.com/smart_wallet/assets/statistics', params=params, headers=headers)

print(response.json())
