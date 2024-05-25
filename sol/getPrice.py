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
            # print(res)
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
            # print(res)
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
            # print(res)
            price = res['price']
            price_1m = res['price_1m']
            price_5m = res['price_5m']
            price_1h = res['price_1h']
            price_6h = res['price_6h']
            price_24h = res['price_24h']
            buys_1m = res['buys_1m']
            sells_1m = res['sells_1m']
            buys_5m = res['buys_5m']
            sells_5m = res['sells_5m']
            buy_volume_1m = res['buy_volume_1m']
            sell_volume_1m = res['sell_volume_1m']
            buy_volume_5m = res['buy_volume_5m']
            sell_volume_5m = res['sell_volume_5m']
            symbol = res['symbol']
            max_supply = res['max_supply']
            market_cap = res['market_cap']
            logo = res['logo']
            open_timestamp = res['open_timestamp']
            if not logo is None:
                arr.append("![图片地址：](" + logo + ")\n\r")
            arr.append("当前时间：" + str(china_time) + "\n\r")
            timeArray = time.localtime(open_timestamp + TIME_NOW)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            arr.append("合约创建时间：" + otherStyleTime + "\n\r")
            arr.append("名称：" + symbol + "\n\r")
            arr.append("最大供应量：" + str(max_supply) + "\n\r")
            arr.append("市值：" + str(round(market_cap / 10000, 2)) + "w $ \n\r")
            if 'renounced_mint' in res.keys():
                renounced_mint = res['renounced_mint']
            else:
                renounced_mint = 0

            if renounced_mint == 1:
                arr.append("是否停止mint：" + "是,相对安全" + "\n\r")
            else:
                arr.append("是否停止mint：" + "否,别上了" + "\n\r")
            top_10_holder_rate = res['top_10_holder_rate']
            if not top_10_holder_rate is None and float(top_10_holder_rate) < 1.0:
                arr.append("top10持仓占比：" + str(round(float(top_10_holder_rate) * 100, 2)) + "%\n\r")
            else:
                arr.append("top10持仓占比：" + str(100) + "%\n\r")
            holder_count = res['holder_count']
            rugged_tokens = res['rugged_tokens']
            if len(rugged_tokens) > 0:
                for r in rugged_tokens:
                    # arr.append("狗庄的跑路合约：" + str(r['address']) + "\n\r")
                    arr.append("跑路合约名称：" + str(r['symbol']) + "\n\r")
            # 检查键'a'是否存在
            key_to_check = 'pool_info'
            quote_reserve = 0
            burn_status = res['burn_status']
            if 'creator_balance' in res.keys():
                creator_balance = res["creator_balance"]
            else:
                creator_balance = 0
            if 'launchpad' in res.keys():
                launchpad = res["launchpad"]
                arr.append("发射平台：" + str(launchpad) + " \n\r")
            if 'launchpad_progress' in res.keys():
                launchpad_progress = res["launchpad_progress"]
                arr.append("发射平台进度：" + str(round(float(launchpad_progress), 2)) + " %\n\r")
            social_links = res["social_links"]
            rug_ratio = res['rug_ratio']
            holder_rugged_num = res['holder_rugged_num']
            holder_token_num = res['holder_token_num']
            hot_level = res['hot_level']
            burn_ratio = 0
            if len(res['burn_ratio']) > 0:
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
            if not price is None:
                arr.append("当前价格：" + str('{:.10f}'.format(price) + " $ \n\r"))
            if not price_1m is None:
                arr.append("1分钟前价格：" + str('{:.10f}'.format(price_1m) + " $ \n\r"))
            if not price_5m is None:
                arr.append("5分钟前价格：" + str('{:.10f}'.format(price_5m) + " $ \n\r"))
            if not price_1h is None:
                arr.append("1小时前价格：" + str('{:.10f}'.format(price_1h) + " $ \n\r"))
            if not price_6h is None:
                arr.append("6小时前价格：" + str('{:.10f}'.format(price_6h) + " $ \n\r"))
            if not price_24h is None:
                arr.append("24小时前价格：" + str('{:.10f}'.format(price_24h) + " $ \n\r"))
            if not buys_1m is None:
                arr.append("1分钟购买：：" + str(buys_1m) + " 次 \n\r")
            if not sells_1m is None:
                arr.append("1分钟卖出：：" + str(sells_1m) + " 次 \n\r")
            if not buys_5m is None:
                arr.append("5分钟购买：：" + str(buys_5m) + " 次 \n\r")
            if not sells_5m is None:
                arr.append("5分钟卖出：：" + str(sells_5m) + " 次 \n\r")
            if not buy_volume_1m is None:
                arr.append("1分钟买入金额：：" + str(round(buy_volume_1m, 2)) + " $ \n\r")
            if not sell_volume_1m is None:
                arr.append("1分钟卖出金额：：" + str(round(sell_volume_1m, 2)) + " $ \n\r")
            if not buy_volume_5m is None:
                arr.append("5分钟买入金额：：" + str(round(buy_volume_5m, 2)) + " $ \n\r")
            if not sell_volume_5m is None:
                arr.append("5分钟卖出金额：：" + str(round(sell_volume_5m, 2)) + " $ \n\r")
            if burn_status == "burn":
                arr.append("池子是否燃烧： 已燃烧" + "\n\r")
            else:
                arr.append("池子是否燃烧： 小心，池子没烧" + "\n\r")

            arr.append("池子燃烧比率：" + str(float(burn_ratio) * 100) + "%\n\r")
            arr = GetPrice.get_token_rat(token, arr)
            arr = GetPrice.get_kol_token(token, arr)
            arr = GetPrice.get_smart_token(token, arr)
            arr.append("合约创建者余额：" + str(round(creator_balance, 2)) + " Sol\n\r")
            arr.append("合约持有人数：" + str(holder_count) + "\n\r")
            arr.append("火热等级：" + str(hot_level) + " \n\r")
            if rug_ratio is None:
                pass
            else:
                arr.append("dev逃跑比例：" + str(round(rug_ratio * 100, 2)) + "%\n\r")
            if rug_ratio is None:
                pass
            else:
                arr.append("总创建的土狗数：" + str(holder_token_num) + "\n\r")
            if rug_ratio is None:
                pass
            else:
                arr.append("跑路的土狗数：" + str(holder_rugged_num) + "\n\r")
            if key_to_check in res:
                quote_reserve = res["pool_info"]["quote_reserve"]
                arr.append("当前池子：" + str(round(float(quote_reserve), 0)) + " Sol\n\r")
            initial_quote_reserve = res["pool_info"]["initial_quote_reserve"]
            if not initial_quote_reserve is None:
                arr.append("dev初始化池子：" + str(round(float(initial_quote_reserve), 0)) + " Sol\n\r")
            if float(quote_reserve) > LIMIT_QUOTE_RESERVE:
                is_buy = True
            else:
                is_buy = False
            if float(quote_reserve) > 300.0:
                if not rug_ratio is None:
                    if hot_level == 1 and renounced_mint == 1 and rug_ratio < 0.5 and float(burn_ratio) > 0.99:
                        arr.append("【☆温馨提示：如果合约安全建议买1s☆】 \n\r")
                    elif hot_level == 2 and renounced_mint == 1 and rug_ratio < 0.5 and float(burn_ratio) > 0.99:
                        arr.append("【☆☆温馨提示：如果合约安全建议买2s☆】 \n\r")
                    elif hot_level >= 3 and renounced_mint == 1 and rug_ratio < 0.5 and float(burn_ratio) > 0.99:
                        arr.append("【☆☆☆温馨提示：如果合约安全建议买3s☆】 \n\r")
                    else:
                        arr.append("【☆温馨提示，池子可以，小心跑路☆】 \n\r")
                else:
                    arr.append("【☆温馨提示，老鼠仓占比大或者热度不够，看线上☆】 \n\r")
            else:
                arr.append("【☆温馨提示，小池子，当心跑路☆】 \n\r")
            arr.append("合约地址：" + token + "\n\r")

        return arr, is_buy


@api.route('/get_token', methods=['get'])
def article():
    token = flask.request.args.get("id")
    arr = []
    arr, is_buy = GetPrice.get_token_info(token, arr)
    # note_str = "".join(arr)

    return arr


# if __name__ == '__main__':
#     arr = []
#     GetPrice.get_smart_token("4ABXJEK62bfKqPiCbSsUtmb4nfkCNPDGtvLhwQcAWNjc", arr)

if __name__ == '__main__':
    # get_smart_token()
    # api.run(port=6888, debug=False, host='0.0.0.0')  # 启动服务
    arr = []
    # # # 招财猫
    # # # get_token_info("25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ")
    arr, is_buy = GetPrice.get_token_info("3WKzqdh3ZW3tP2PhAtAuDu4e1XsEzFhk7qnN8mApm3S2", arr)
    note_str = "".join(arr)
    print(note_str)
