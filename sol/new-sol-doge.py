# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

token_dd = '1b22d689b3572c931f39f31bcc4730ce95bbd7f474bc1fb11d61f0ac96a062a9'
# 分钟
TIME = 6

beijing = timezone(timedelta(hours=8))
print(f'1、北京时区为：{beijing}')

Tokyo = timezone(timedelta(hours=9))
print(f'2、东京时区为：{Tokyo}')

New_York = timezone(timedelta(hours=-4))
print(f'3、纽约时区为：{New_York}')

utc = timezone.utc
print(f'4、世界标准时区为：{utc}')

utc_time = datetime.utcnow()
print(f'UTC时间为：{utc_time}')
print(f'本地时间为：{datetime.now()}')

china_time = utc_time.astimezone(beijing)
time_tokyo = utc_time.astimezone(Tokyo)
time_newyork = utc_time.astimezone(New_York)

print('1、更改时区为北京后的时间：', china_time)
print('2、更改时区为东京后的时间：', time_tokyo)
print('3、更改时区为纽约后的时间：', time_newyork)


# 获取当前时间呈现到毫秒级别并转换为时间戳
def get_current_time_ms_to_timestamp():
    return int(time.time() * 1000)


# 获取当前时间呈现到当天的0时0分0秒000毫秒并转换为时间戳
def get_current_time_day_to_timestamp():
    # 获取当日0时0分0秒000毫秒
    today_0 = dt.datetime.combine(dt.date.today(), dt.time.min)
    # 转换为时间戳
    today_0_timestamp = int(time.mktime(today_0.timetuple())) * 1000
    return today_0_timestamp


# 获取当前时间呈现到毫秒级别
def get_current_time_ms():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# 获取当前时间呈现到秒级别
def get_current_time_s():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 将毫秒级别的时间戳转换为时间格式
def timestamp_to_time(timestamp):
    return dt.datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


# 获取当前月份的首日
def get_current_month_first_day():
    return dt.datetime.strptime(dt.datetime.now().strftime('%Y-%m') + '-01', '%Y-%m-%d')


def send_msg():
    """
    通过钉钉机器人发送内容
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    content_str = str(china_time) + "-【系统提醒】sol聪明钱买卖聪明钱地址，本次已经扫描完毕，系统会每20分钟检测一次！"
    data = {
        "msgtype": "text",
        "text": {
            "content": content_str
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def send_markdown_system():
    """
    通过钉钉机器人发送内容
    @param msg:
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    msg = ["#### 冲狗必读：\n\r ```", "\n 1.所有项目都是土狗，千万不能贪多，不能格局;\n",
           "2.不要在一个狗上贪恋爱，该放手就放手;\n",
           "3.加仓要慢慢加，不能一口吃个胖子;\n", "4.看好的项目一定留一个底仓；\n",
           "5.高倍项目10-30倍一定要出一大部分，否则跌下来就后悔了;\n",
           "6.拿到一个Token先观察，不着急买，看一下项目方，自己做个初步判断上的仓位;\n",
           "7.要以小博大，不能以大博小，否则你将很快出局;\n", "8.如果使用机器人冲，赚钱了立即卖，不要后悔,好狗很多;\n",
           "9.机会是跌出来的，不是冲出来的\n\r"]
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": str(china_time) + "sol",
            "text": "".join(msg)
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def send_markdown(msg):
    """
    通过钉钉机器人发送内容
    @param msg:
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": str(china_time) + "sol",
            "text": msg
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def send_markdown_address(address, type):
    """
    通过钉钉机器人发送内容
    @param msg:
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}

    sell_data = {
        "msgtype": "markdown",
        "markdown": {
            "title": str(china_time) + "sol-直接复制粘贴",
            "text": address
        },
    }

    buy_data = {
        "at": {
            "isAtAll": True
        },
        "msgtype": "markdown",
        "markdown": {
            "title": str(china_time) + "sol-直接复制粘贴",
            "text": address
        },
    }
    if type == "BUY":
        res = requests.post(url, data=json.dumps(buy_data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    else:
        res = requests.post(url, data=json.dumps(sell_data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def get_new_token():
    url = f"https://gmgn.ai/defi/quotation/v1/pairs/sol/new_pairs?limit=50&orderby=" \
          f"open_timestamp&direction=desc&filters[]=not_honeypot&filters[]=not_risk&min_quote_usd=10000"
    headers = {
        "authority": "gmgn.ai",
        "accept": "application/json, text/plain, */*'",
        "accept-language": "zh,zh-CN;q=0.9",
        "cache-control": "no-cache",
        "cookie": "_ga=GA1.1.1538430465.1713834683; _ga_0XM0LYXGC8=GS1.1.1714184467.2.1.1714184492.0.0.0",
        "pragma": "no-cache",
        "referer": "https://gmgn.ai/new-pair?chain=sol",
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
        res = result['data']['pairs']
        for r in res:
            creation_timestamp = r['creation_timestamp']
            token = r['base_address']
            # 获取当前时间
            date = datetime.now()
            timestamp = int(date.timestamp())
            # 对比的时间8分钟的购买
            diff = 60 * TIME
            if (timestamp - creation_timestamp) <= diff:
                arr = get_token_info(token)
                note_str = "".join(arr)
                # print(note_str)
                send_markdown(note_str)
                time.sleep(5)
                send_markdown_address(token, "BUY")
                time.sleep(3)


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
        symbol = res['symbol']
        price_1m = res['price_1m']
        price_5m = res['price_5m']
        price_1h = res['price_1h']
        holder_count = res['holder_count']
        logo = res['logo']
        # 检查键'a'是否存在
        key_to_check = 'pool_info'
        quote_reserve = "0"
        burn_status = res['burn_status']
        if 'creator_balance' in res.keys():
            creator_balance = res["creator_balance"]
        else:
            creator_balance = 0
        social_links = res["social_links"]
        rug_ratio = res['rug_ratio']
        holder_rugged_num = res['holder_rugged_num']
        holder_token_num = res['holder_token_num']
        hot_level = res['hot_level']
        burn_ratio = res['burn_ratio']
        rugged_tokens = res['rugged_tokens']
        buys_1m = res['buys_1m']
        buys_5m = res['buys_5m']
        sells_1m = res['sells_1m']
        sells_5m = res['sells_5m']
        arr.append("![图片地址：](" + logo + ")\n\r")
        arr.append("名称：" + symbol + "\n\r")
        renounced_mint = res['renounced_mint']
        if renounced_mint == 1:
            arr.append("是否停止mint：" + "是" + "\n\r")
        else:
            arr.append("是否停止mint：" + "否" + "\n\r")
        top_10_holder_rate = res['top_10_holder_rate']
        arr.append("top10持仓占比：" + str(top_10_holder_rate * 100) + "%\n\r")
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
        arr.append("1分钟买单次数：" + str(buys_1m) + "次\n\r")
        arr.append("5分钟买单次数：" + str(buys_5m) + "次\n\r")
        arr.append("1分钟卖单次数：" + str(sells_1m) + "次\n\r")
        arr.append("1分钟卖单次数：" + str(sells_5m) + "次\n\r")
        arr.append("池子是否燃烧：" + burn_status + "\n\r")
        arr.append("池子燃烧比率：" + str(burn_ratio) + "%\n\r")
        arr.append("合约创建者余额：" + str(creator_balance) + " Sol\n\r")
        arr.append("合约持有人数：" + str(holder_count) + "\n\r")
        arr = get_token_rat(token, arr)
        arr.append("★火热等级：" + str(hot_level) + " \n\r")
        if rug_ratio is None:
            pass
        else:
            arr.append("★dev逃跑比例：" + str(rug_ratio * 100) + "%\n\r")
        if rug_ratio is None:
            pass
        else:
            arr.append("★总创建的土狗数：" + str(holder_token_num) + "\n\r")
        if rug_ratio is None:
            pass
        else:
            arr.append("★跑路的土狗数：" + str(holder_rugged_num) + "\n\r")
        # 历史跑路盘
        if len(rugged_tokens) > 0:
            for r in rugged_tokens:
                # arr.append("狗庄的跑路合约：" + str(r['address']) + "\n\r")
                arr.append("跑路合约名称：" + str(r['symbol']) + "\n\r")
        if key_to_check in res:
            quote_reserve = res["pool_info"]["quote_reserve"]
            arr.append("★当前池子：" + str(quote_reserve) + " Sol\n\r")

        if rug_ratio is None:
            if float(quote_reserve) > 300.0:
                if hot_level == 1:
                    arr.append("【★温馨提示：建议买1s,跑快点★】 \n\r")
                elif hot_level == 2:
                    arr.append("【★温馨提示：建议买2s,跑快点★】 \n\r")
                elif hot_level >= 3:
                    arr.append("【★温馨提示：建议买3s,跑快点★】 \n\r")
                else:
                    arr.append("【★温馨提示，建议先观察★】 \n\r")
            else:
                arr.append("【★温馨提示，池子不足300s，小心★】 \n\r")
        else:
            arr.append("【★温馨提示，随时跑路，跑快点★】 \n\r")

    return arr


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

        arr.append("老鼠仓个数：：" + str(top_rat_trader_count) + "\n\r")
        arr.append("老鼠仓占比：" + str(top_rat_trader_amount_percentage * 100) + " %\n\r")
    return arr


if __name__ == '__main__':
    get_new_token()
