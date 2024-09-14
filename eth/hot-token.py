# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

from getPrice import GetPrice

token_dd = 'fedcbd5442846473d7f4c2a08dafdd7538e29ace9f0829cb8f8af02cbd725be7'
# token_dd = 'a9aab412b508bb619859974fc7fb202668b436574a992efc69b3aef3e14650e9'
# 分钟
TIME = 180

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


def get_hot_token():
    url = (f"https://gmgn.ai/defi/quotation/v1/rank/eth/swaps/1h?orderby=smartmoney&direction=desc&filters[]="
           f"has_social&filters[]=not_honeypot&filters[]=verified&filters[]="
           f"renounced&filters[]=locked&min_liquidity=10000&min_volume=100000&min_swaps=100&max_swaps=1000")
    headers = {
        "authority": "gmgn.ai",
        "accept": "application/json, text/plain, */*'",
        "accept-language": "zh,zh-CN;q=0.9",
        "cache-control": "no-cache",
        "cookie": "_ga=GA1.1.1538430465.1713834683; cf_clearance=.OyaesAhLSMsM5eF2KlNX79_NZwt3uF5DwSgXkDnEJ8"
                  "-1723854910-1.2.1.1-F8vMYbk4qMo9g5ibqisZP69oa8kb.29cP_rEy6z2Fk9Id61yMRh7zKGDsMF"
                  ".r4cgaUDlAH8ooF3pbDNIvn.GLhvB6WVYGfOBfJHAxu0l0REF86BexB5xnXlMVV.FgG2IDE25_NcOsh9h_D8kPE3uJ"
                  ".W0XrEL_pUvfvNedxnMe2emNFuKZUn01O4OK0CFeD0Jn6I0"
                  ".Mku73Y7r_w8J8JZ5jUGjR85qBLImi77sR0IMtJjw1pikWSSVb6Imuk2UqQ0Iq"
                  ".0cBLouOh4Vo99zyNw5AScroUFpAwT9Ctv3WRmlTzZlSqy86jKt17BKJaXYI.fOZrhjzoEVoUk"
                  ".m2R32F6IrBnYh5T_XcR2fLEqEMpMimJr9YnihBAUtAd5Ce4GmlfTLDD2GUZMcnVMNnxmLhQ4w9fFqaBNxQQeh6_1yVLMQc; "
                  "__cf_bm=nolL.xKKdw7qaKzLNJGLcAoM24LGENAMovD8cgPM0bE-1723854914-1.0.1.1-XSU0zDsMukZxKzyaopnKC"
                  ".rl7YYbgO.u8DgrD6oYFSC6G1eCclhSNRkbawDaDpPiMD663hlufTgyLcy1PMLAxg; "
                  "_ga_0XM0LYXGC8=GS1.1.1723854780.73.1.1723854954.0.0.0",
        "pragma": "no-cache",
        "referer": "https://gmgn.ai/trend?chain=eth",
        "sec-ch-ua": '"Google Chrome";v="117", "Chromium";v="117", "Not A;Brand";v="99", "Microsoft Edge";v="117"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                      "Safari/537.36",

    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    arr = []
    if response.status_code == 200:
        result = response.json()
        res = result['data']['rank']
        for r in res:
            pool_creation_timestamp = r['pool_creation_timestamp']
            token = r['address']
            # 获取当前时间
            date = datetime.now()
            timestamp = int(date.timestamp())
            # 对比的时间8分钟的购买
            diff = 60 * TIME
            if not pool_creation_timestamp is None:
                if (timestamp - pool_creation_timestamp) <= diff:
                    arr, is_buy = GetPrice.get_token_info(token, arr)
                    note_str = "".join(arr)
                    print(note_str)

                    # print(note_str)
                    send_markdown(note_str)
                    time.sleep(5)
                    send_markdown_address(token, "BUY")
                    time.sleep(3)
                    arr = []


if __name__ == '__main__':
    get_hot_token()
