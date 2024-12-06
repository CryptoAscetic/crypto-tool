# -*- coding: utf-8 -*

import requests


def get_token_rat(token):
    url = f"https://gmgn.ai/defi/quotation/v1/tokens/stats/sol/" + token
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
        res = result['data']

        top_rat_trader_count = res['top_rat_trader_count']
        top_rat_trader_amount_percentage = res['top_rat_trader_amount_percentage']

        arr.append("老鼠仓个数：：" + str(top_rat_trader_count) + "\n\r")
        arr.append("老鼠仓占比：" + str(top_rat_trader_amount_percentage * 100) + " %\n\r")

        note_str = "".join(arr)
        print(note_str)


if __name__ == '__main__':
    # 招财猫
    # get_token_info("25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ")

    get_token_rat("71qkaXcSjeNBDHzUh1X87zGW8GqgdFM4S4j5nAeuMSpZ")
