import requests


def get_pump_config():
    headers = {
        'authority': 'frontend-api.pump.fun',
        'accept': '*/*',
        'accept-language': 'zh,zh-CN;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://pump.fun',
        'pragma': 'no-cache',
        'referer': 'https://pump.fun/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'limit': '1000',
        'offset': '0',
        'user': '4pDuLhqZ77e3mBxWb2jqfmMLufLeM6NjEP8hezTnv3Ve',
    }

    response = requests.get('https://frontend-api.pump.fun/replies/9uVHqmmTzaym1mAEdQiQgofY4B9nAHbbUAgctekDU3fa',
                            params=params, headers=headers)
    if response.status_code == 200:
        result = response.json()
        len(result)
        for reply in result:
            # print(reply)
            text = reply['text']
            user_id = reply['id']
            username = reply['username']
            if username is None:
                username = str(user_id) + '小白'
            print("用户：" + str(username) + "，说的内容：" + text + "\n\r")


if __name__ == '__main__':
    get_pump_config()
