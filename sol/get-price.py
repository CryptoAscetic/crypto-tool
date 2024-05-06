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
    arr = []
    print("Status code:", response.status_code)
    if response.status_code == 200:
        result = response.json()
        res = result['data']['token']
        print(res)
        price = res['price']
        price_1m = res['price_1m']
        price_5m = res['price_5m']
        price_1h = res['price_1h']
        holder_count = res['holder_count']
        rugged_tokens = res['rugged_tokens']
        if len(rugged_tokens) > 0:
            for r in rugged_tokens:
                arr.append("狗庄的跑路合约：" + str(r['address']) + "\n\r")
                arr.append("跑路合约名称：" + str(r['symbol']) + "\n\r")

        symbol = res['symbol']
        # 检查键'a'是否存在
        key_to_check = 'pool_info'
        quote_reserve = ""
        if key_to_check in res:
            quote_reserve = res["pool_info"]["quote_reserve"]
            arr.append("当前池子：" + str(quote_reserve) + " Sol\n\r")
        burn_status = res['burn_status']
        creator_balance = res["creator_balance"]
        social_links = res["social_links"]
        rug_ratio = res['rug_ratio']
        holder_rugged_num = res['holder_rugged_num']
        holder_token_num = res['holder_token_num']
        hot_level = res['hot_level']
        burn_ratio = res['burn_ratio']
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
                arr.append("电报：<" + telegram + ">\n\r")
        arr.append("当前价格：" + str(price) + "$\n\r")
        arr.append("1分钟前价格：" + str(price_1m) + "$\n\r")
        arr.append("5分钟前价格：" + str(price_5m) + "$\n\r")
        arr.append("24小时前价格：" + str(price_1h) + "$\n\r")
        arr.append("池子是否燃烧：" + burn_status + "\n\r")
        arr.append("池子燃烧比率：" + str(burn_ratio) + "%\n\r")
        arr.append("合约创建者余额：" + str(creator_balance) + " Sol\n\r")
        arr.append("合约持有人数：" + str(holder_count) + "\n\r")
        arr.append("火热等级：" + str(hot_level) + " \n\r")
        arr.append("名称：" + str(symbol) + " \n\r")

        if rug_ratio is None:
            pass
        else:
            arr.append("dev逃跑比例：" + str(rug_ratio * 100) + "%\n\r")
        if rug_ratio is None:
            pass
        else:
            arr.append("总创建的土狗数：" + str(holder_token_num) + "\n\r")
        if rug_ratio is None:
            pass
        else:
            arr.append("跑路的土狗数：" + str(holder_rugged_num) + "\n\r")
        if float(quote_reserve) > 300.0:
            if hot_level == 1:
                arr.append("【☆温馨提示：建议买1s☆】 \n\r")
            elif hot_level == 2:
                arr.append("【☆温馨提示：建议买2s☆】 \n\r")
            elif hot_level >= 3:
                arr.append("【☆温馨提示：建议买3s☆】 \n\r")
            else:
                arr.append("【☆温馨提示，建议先观察☆】 \n\r")
        else:
            arr.append("【☆温馨提示，池子不足300s，小心☆】 \n\r")

        arr.append("合约地址：" + token)

        note_str = "".join(arr)
        print(note_str)


if __name__ == '__main__':
    # 招财猫
    # get_token_info("25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ")

    get_token_info("48VSMni6syK6idRR5gKh7tQNYTUHByPyMGb4iKYLvFr8")
