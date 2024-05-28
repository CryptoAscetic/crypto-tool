# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

from getAiPrice import GetAiPrice

# token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'

token_dd = 'a9aab412b508bb619859974fc7fb202668b436574a992efc69b3aef3e14650e9'
# 分钟
TIME = 1
# 胜率
PNL = 0.3

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
           "2.不要在一个狗上谈恋爱，该放手就放手;\n",
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


def request_ok():
    # 获取所有的数据
    url = f"https://gmgn.ai/defi/quotation/v1/rank/sol/wallets/7d?orderby=last_active&direction=desc"

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
        "referer": "https://gmgn.ai/discover/SymeX8WZf?chain=sol",
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
        res = result['data']['rank']
        arr = []
        for re in res:
            # print(re)
            pnl_1d = re['pnl_1d']
            pnl_7d = re['pnl_7d']
            pnl_30d = re['pnl_30d']
            # 聪明钱包地址
            wallet = re['wallet_address']
            if not pnl_7d is None:
                if pnl_7d > PNL:
                    # print(re)
                    # 获取所有的数据
                    smart_url = (f"https://gmgn.ai/defi/quotation/v1/wallet_activity/sol?type=buy&type=sell&"
                                 f"wallet=" + wallet + "&limit=10&cost=10")
                    response = requests.get(smart_url, headers=headers)
                    time.sleep(1)
                    print("Status code:", response.status_code)
                    if response.status_code == 200:
                        result = response.json()
                        activities = result['data']['activities']
                        for ac in activities:
                            wallet_timestamp = ac['timestamp']
                            # 获取当前时间
                            date = datetime.now()
                            timestamp = int(date.timestamp())
                            # 对比的时间8分钟的购买
                            diff = 60 * TIME
                            if timestamp - int(wallet_timestamp) <= diff:
                                cost_usd = ac['cost_usd']
                                event_type = ac['event_type']
                                logo = ac['token']['logo']
                                if not logo is None and cost_usd > 50.0:
                                    token_address = ac['token_address']

                                    price = ac['token']['price']
                                    symbol = ac['token']['symbol']

                                    price = str('{:.10f}'.format(price))

                                    arr, is_buy = GetAiPrice.get_token_info(token_address, arr)
                                    # arr.append("![图片地址：](" + logo + ")\n\r")
                                    # arr.append("当前时间：" + str(china_time) + "\n\r")
                                    if not pnl_7d is None:
                                        arr.append("7天收益率：" + str(round(pnl_7d, 2)) + " 倍\n\r")
                                    if not pnl_1d is None:
                                        arr.append("1天收益率：" + str(round(pnl_1d, 2)) + " 倍\n\r")
                                    if not pnl_30d is None:
                                        arr.append("30收益率：" + str(round(pnl_30d, 2)) + " 倍\n\r")
                                    # arr.append("聪明钱地址：" + str(wallet) + "\n\r")
                                    if event_type == "buy":
                                        arr.append("买就发财：" + str(event_type) + "\n\r")
                                    else:
                                        arr.append("【卖卖卖】，如果交易金额过大抄底：" + "\n\r")
                                    arr.append("交易金额：" + str(cost_usd) + "$\n\r")
                                    arr.append("购买价格：：" + str(price) + "$\n\r")
                                    # arr.append("合约名称：" + str(symbol) + "\n\r")
                                    if is_buy:
                                        note_str = "".join(arr)
                                        print(note_str)
                                        send_markdown(note_str)
                                        time.sleep(3)
                                        send_markdown_address(token_address, "BUY")
                                        time.sleep(2)
                                    arr = []


if __name__ == '__main__':
    request_ok()
