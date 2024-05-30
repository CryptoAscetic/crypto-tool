# -*- coding: utf-8 -*
import time
from datetime import timezone, timedelta, datetime

import flask
import requests

# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__)

beijing = timezone(timedelta(hours=8))
Tokyo = timezone(timedelta(hours=9))
New_York = timezone(timedelta(hours=-4))
utc = timezone.utc
utc_time = datetime.utcnow()
china_time = utc_time.astimezone(beijing)
time_tokyo = utc_time.astimezone(Tokyo)
time_newyork = utc_time.astimezone(New_York)

LIMIT_QUOTE_RESERVE = 130.0
TIME_NOW = 8 * 60 * 60


class GetPrice:

    @staticmethod
    def get_token_rat(token, arr):
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
        print("Status code:", response.status_code)
        if response.status_code == 200:
            result = response.json()
            res = result['data']

            top_rat_trader_count = res['top_rat_trader_count']
            top_rat_trader_amount_percentage = res['top_rat_trader_amount_percentage']

            arr.append("老鼠仓个数：：" + str(top_rat_trader_count) + "个\n\r")
            arr.append("老鼠仓占比：" + str(round(float(top_rat_trader_amount_percentage * 100), 2)) + " %\n\r")

        return arr

    # https://gmgn.ai/defi/quotation/v1/trades/sol/9jaZhJM6nMHTo4hY9DGabQ1HNuUWhJtm7js1fmKMVpkN?limit=50
    @staticmethod
    def get_kol_token(token, arr):
        url = f"https://gmgn.ai/defi/quotation/v1/trades/sol/" + token + "?limit=100&&tag=renowned"
        headers = {
            "authority": "gmgn.ai",
            "accept": "application/json, text/plain, */*'",
            "accept-language": "zh,zh-CN;q=0.9",
            "authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9"
                             ".eyJhdWQiOiJnbWduLmFpL2FjY2VzcyIsImV4cCI6MTcxNTkxNDE3NCwiaWF0IjoxNzE1NzQx"
                             "Mzc0LCJpc3MiOiJnbWduLmFpL3NpZ25lciIsInN1YiI6ImdtZ24uYWkvYWNjZXNzIiwidmVyc2"
                             "lvbiI6IjEuMCIsImFkZHJlc3MiOiIyVXFBVjJBR1lrdHkzeVhSeHYyZ0ZaTjNhUXZvOVg0Zjdhd"
                             "moxTE1rTjZzeSIsImNoYWluIjoic29sIn0.E-1oShnWksT5-EZeE7SZxegQN42KnRVb7Uqv_xkl"
                             "hUzZRD3n39yYiCZB74zVmXBaS9XuDCOwjXknLi3xB3LAzA'",
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
        # rat_trader  sandwich_bot
        new_li = []
        if response.status_code == 200:
            result = response.json()
            res = result['data']['history']
            print(res)
            for re in res:
                maker = re['maker']
                price_usd = re['price_usd']
                amount_usd = re['amount_usd']
                event = re['event']
                maker_name = re['maker_name']
                timestamp = re['timestamp']
                amount_usd = re['amount_usd']
                timeArray = time.localtime(timestamp + +TIME_NOW)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                if not price_usd is None:
                    arr.append("操作时间：" + otherStyleTime + "\n\r")
                    arr.append(maker_name + ":" + event + "：价格：" + str('{:.10f}'.format(float(price_usd)) + "$ ")
                               + "金额：" + str(round(amount_usd, 2)) + " $\n\r")

                    arr.append("购买金额：" + str(amount_usd) + " $\n\r")
                if maker not in new_li:
                    new_li.append(maker)

            arr.append("Kol数：" + str(len(new_li)) + "\n\r")

            print(arr)
        return arr

    # https://gmgn.ai/defi/quotation/v1/trades/sol/9jaZhJM6nMHTo4hY9DGabQ1HNuUWhJtm7js1fmKMVpkN?limit=50
    @staticmethod
    def get_smart_token(token, arr):
        url = f"https://gmgn.ai/defi/quotation/v1/trades/sol/" + token + "?limit=100&&tag=smart_degen"
        headers = {
            "authority": "gmgn.ai",
            "accept": "application/json, text/plain, */*'",
            "accept-language": "zh,zh-CN;q=0.9",
            "authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9"
                             ".eyJhdWQiOiJnbWduLmFpL2FjY2VzcyIsImV4cCI6MTcxNTkxNDE3NCwiaWF0IjoxNzE1NzQx"
                             "Mzc0LCJpc3MiOiJnbWduLmFpL3NpZ25lciIsInN1YiI6ImdtZ24uYWkvYWNjZXNzIiwidmVyc2"
                             "lvbiI6IjEuMCIsImFkZHJlc3MiOiIyVXFBVjJBR1lrdHkzeVhSeHYyZ0ZaTjNhUXZvOVg0Zjdhd"
                             "moxTE1rTjZzeSIsImNoYWluIjoic29sIn0.E-1oShnWksT5-EZeE7SZxegQN42KnRVb7Uqv_xkl"
                             "hUzZRD3n39yYiCZB74zVmXBaS9XuDCOwjXknLi3xB3LAzA'",
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
        # rat_trader  sandwich_bot
        new_li = []
        if response.status_code == 200:
            result = response.json()
            res = result['data']['history']
            buy = 0
            sell = 0
            buy_sum = 0.0
            sell_sum = 0.0
            print(res)
            for re in res:
                maker = re['maker']
                event = re['event']
                amount_usd = re['amount_usd']
                if not amount_usd is None:
                    if event == "sell":
                        sell = sell + 1
                        sell_sum = sell_sum + amount_usd
                    else:
                        buy = buy + 1
                        buy_sum = buy_sum + amount_usd
                    if maker not in new_li:
                        new_li.append(maker)

            arr.append("聪明钱：" + str(len(new_li)) + "\n\r")
            arr.append("购买次数：" + str(buy) + " 卖除次数：" + str(sell) + "\n\r")
            arr.append("购买金额：" + str(float(buy_sum)) + " $ 卖除金额：" + str(float(sell_sum)) + " $\n\r")
        return arr

    @staticmethod
    def get_token_info(token, arr):
        global is_buy
        url = f"https://gmgn.ai/defi/quotation/v1/tokens/eth/" + token
        headers = {
            "authority": "gmgn.ai",
            "accept": "application/json, text/plain, */*'",
            "accept-language": "zh,zh-CN;q=0.9",
            "cache-control": "no-cache",
            "cookie": "_ga=GA1.1.1538430465.1713834683; _ga_0XM0LYXGC8=GS1.1.1714184467.2.1.1714184492.0.0.0",
            "pragma": "no-cache",
            "referer": "https://gmgn.ai/eth/token/" + token,
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
            price = res['price']
            price_5m = res['price_5m']
            price_1h = res['price_1h']
            price_6h = res['price_6h']
            price_24h = res['price_24h']
            symbol = res['symbol']
            logo = res['logo']

            if not logo is None:
                arr.append("![图片地址：](" + logo + ")\n\r")
            arr.append("当前时间：" + str(china_time) + "\n\r")
            arr.append("当前价格：" + str('{:.10f}'.format(price) + " $ \n\r"))
            arr.append("合约名称：" + str(symbol + " $ \n\r"))

            if not price_6h is None:
                arr.append("5分钟前价格：" + str('{:.10f}'.format(price_5m) + " $ \n\r"))
            if not price_1h is None:
                arr.append("1小时前价格：" + str('{:.10f}'.format(price_1h) + " $ \n\r"))
            if not price_6h is None:
                arr.append("6小时前价格：" + str('{:.10f}'.format(price_6h) + " $ \n\r"))
            if not price_24h is None:
                arr.append("24小时前价格：" + str('{:.10f}'.format(price_24h) + " $ \n\r"))

            arr.append("合约创建者余额：" + str(round(creator_balance, 2)) + " Sol\n\r")
            arr.append("合约持有人数：" + str(holder_count) + "\n\r")

            arr.append("合约地址：" + token + "\n\r")

        return arr, is_buy


if __name__ == '__main__':
    # get_smart_token()
    # api.run(port=6888, debug=False, host='0.0.0.0')  # 启动服务
    arr = []
    # # # 招财猫
    # # # get_token_info("25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ")
    arr, is_buy = GetPrice.get_token_info("0xd29da236dd4aac627346e1bba06a619e8c22d7c5", arr)
    note_str = "".join(arr)
    print(note_str)
