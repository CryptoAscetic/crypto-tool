# -*- coding: utf-8 -*

import requests


def get_token_info(token):
    url = f"https://gmgn.ai/defi/quotation/v1/tokens/sol/" + token
    headers = {
        "authority": "gmgn.ai",
        "accept": "application/json, text/plain, */*'",
        "accept-language": "zh,zh-CN;q=0.9",
        "cache-control": "no-cache",
        "cookie": "_ga=GA1.1.1538430465.1713834683; _ga_0XM0LYXGC8=GS1.1.1714184467.2.1.1714184492.0.0.0",
        "pragma": "no-cache",
        "referer": "https://gmgn.ai/sol/token/" + token,
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                      "Safari/537.36",

    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        result = response.json()
        res = result['data']['token']
        print(res)
        arr = []
        price = res['price']
        price_1m = res['price_1m']
        price_5m = res['price_5m']
        price_1h = res['price_1h']
        holder_count = res['holder_count']
        quote_reserve = res["pool_info"]["quote_reserve"]
        burn_status = res['burn_status']
        creator_balance = res["creator_balance"]
        social_links = res["social_links"]
        if len(social_links) > 0:
            twitter_username = res["social_links"]["twitter_username"]
            website = res["social_links"]["website"]
            telegram = res["social_links"]["telegram"]
            if twitter_username is None:
                pass
            else:
                arr.append("推特：<" + "https://twitter.com/" + twitter_username + ">\n\r")
            if website is None:
                pass
            else:
                arr.append("官网地址：<" + website + ">\n\r")
            if telegram is None:
                pass
            else:
                arr.append("官网地址：<" + telegram + ">\n\r")
        arr.append("当前价格：" + str(price) + "$\n\r")
        arr.append("1分钟前价格：" + str(price_1m) + "$\n\r")
        arr.append("5分钟前价格：" + str(price_5m) + "$\n\r")
        arr.append("1小时前价格：" + str(price_1h) + "$\n\r")
        arr.append("池子是否燃烧：" + burn_status + "\n\r")
        arr.append("合约创建者余额：" + str(creator_balance) + " Sol\n\r")
        arr.append("合约持有人数：" + str(holder_count) + "\n\r")
        arr.append("池子sol数：" + str(quote_reserve) + "Sol\n\r")

        note_str = "".join(arr)
        print(note_str)


if __name__ == '__main__':
    get_token_info("ChanM2vka4gJ3ob1SejJXnxoNuoAXGGJxDMJRSLD7nzW")
