# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

from getAiPrice import GetAiPrice

# token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'

token_dd = '2fb4e8566e1348bf837cd8527798b8f4461287a2403bda7d15f9903ee8592909'
# 分钟
TIME = 1
# 胜率
PNL = 0.5

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
        "at": {
            "isAtAll": True
        },
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


# https://gmgn.ai/sol/address/BTp4uCeCeWKxT6pzTmqJzzrtyqeTmtF1zr2EtpnZSw7F
def request_ok():
    arr = []
    tokens = {
        '515FRkgdKUunk4BJGndav2FgZniEqYtkdLqcgc8nLSNV': '大帅',
        '441bsKo6VHuhyUhkDiGxYKXyoZzNuF2Ru4hbPteFiEdn': 'klöss',
        'BgJrk3AJEWf41WxThAvDCkZmxuxbt3Q4aZc1P2rrHtZV': 'not BusinessWeek',
        '9sB4T5UBqdz5M7zEce2idFRAPVKe65DpuBooWYoRtpQi': '໓uke of ¢ryptoshi',
        'DxpA16RZwXmUAFHHxBRwNb1DUrnKyS1e8rYkh1MvjbxC': 'Kenny Powerz-cat超低价',
        'Gf9XgdmvNHt8fUTFsWAccNbKeyDXsgJyZN8iFJKg5Pbd': '0xuezhang|985.eth',
        'DG6QpsjvwqCGyLAYXKEmDBLRfomJ2UAmoe4MJWL9fNtt': 'Queenkayx ❤',
        'G1NhjBssPqbu6rkaiTjmc1SCTGxjzMf4vnvhmkQFRiBL': 'M1STΞR5ΞRM4N',
        'ABDAKRTDRfDUbosQinqXs8NRH3AjeA4s2j2pFukzicFf': 'NickakaMole-阿乐第一人',
        'BTp4uCeCeWKxT6pzTmqJzzrtyqeTmtF1zr2EtpnZSw7F': 'richclassdecor.eth-moga第一人',
        'C6DYY8opJ5dxLEGGUWvwBGACyszxmDQ9VHdV5DeyrgbH': 'smart-1-超低',
        '9hy2BKD9yf5H6HWR4Vr8xnsNdvnYrZEjqx3H7vp4gbGe': 'smart-2-还行',
        'D68Jqb7jEZAGtav4aVui536mtT1KAJ4bKwYgFqy8etW7': 'smart-3-稍高',
        '82jXFTVu2XwCnG63pGqdf1yAfGMLbmXNzmBE5nupx6YF': 'xule-happy',
        'Haee7H5bKDCnm6dXLkeR9DcWw9Puhnkwk71QBUSHcpUt': 'xule-bazinga',
        'E2SRcmvvX71efevxnYJTcW9oggnprz7Xk2aSj3DV558L': 'xule-father-1',
        'HLe1XVdMPiTakEryE2t593iv9pK9YEMBmRzMk71WetpK': 'xule-father-2'
    }

    #     my_dict = {'a': 1, 'b': 2, 'c': 3}
    # for key in my_dict.keys():
    #     print(key, my_dict[key])
    for token in tokens.keys():
        # 获取所有的数据
        url = (f"https://gmgn.ai/defi/quotation/v1/wallet_activity/sol?type=buy&type=sell&wallet=" + token
               + "&limit=10&cost=10")

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
            "referer": "https://gmgn.ai/sol/address/" + token,
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                          "Safari/537.36",

        }
        response = requests.get(url, headers=headers)
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
                    token_address = ac['token_address']
                    price = ac['token']['price']
                    price = str('{:.10f}'.format(price))

                    arr, is_buy = GetAiPrice.get_token_info(token_address, arr)
                    if event_type == "buy":
                        arr.append("买就发财：" + str(event_type) + "\n\r")
                    else:
                        arr.append("【卖卖卖】，如果交易金额过大抄底：" + "\n\r")
                    arr.append("交易金额：" + str(cost_usd) + "$\n\r")
                    arr.append("购买价格：：" + str(price) + "$\n\r")
                    arr.append("kol名字：" + str(tokens[token]) + "\n\r")

                    note_str = "".join(arr)
                    print(note_str)
                    send_markdown(note_str)
                    time.sleep(1)
                    send_markdown_address(token_address, "BUY")
                    time.sleep(1)
                    arr = []
                    if 'xule' in str(tokens[token]):
                        send_markdown_system()
                        time.sleep(1)


if __name__ == '__main__':
    request_ok()
