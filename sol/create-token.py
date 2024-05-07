# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

from getPrice import GetPrice

token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'
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


# 系统检测提示
def send_msg():
    """
    通过钉钉机器人发送内容
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    content_str = str(china_time) + "-【系统提醒】sol的科学家们创建合约扫描完毕，系统会每20分钟检测一次！"
    data = {
        "msgtype": "text",
        "text": {
            "content": content_str
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


# 大于600的提示
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


# 地址
def send_markdown_address(address):
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
            "text": address
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


#  核心内容
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
        "at": {
            "atUserIds": [
                "CryptoAscetic"
            ],
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def request_ok():
    url = f"https://mintinglab-solana-api.dexlab.space/v1/mintinglab/tokens/last-actions"
    headers = {
        "authority": "mintinglab-solana-api.dexlab.space",
        "accept": "*/*",
        "accept-language": "zh,zh-CN;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.dexlab.space",
        "platform": "web",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "referer": "https://www.dexlab.space/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "x-utc": "8",
        "x-zkdex-env": "0"
    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        res = response.json()
        arr = []
        for r in res:  # 第二个实例
            block_time = r["block_time"]
            mint_address = r["mint_address"]
            action_type = r["action_type"]
            token_symbol = r["token_symbol"]
            signer_address = r["signer_address"]
            # token_name = r["token_name"]
            token_symbol_image = r["token_symbol_image"]
            signature = r["signature"]
            # 获取当前时间
            date = datetime.now()
            timestamp = int(date.timestamp())
            # 对比的时间8分钟的购买
            diff = 60 * TIME
            if (timestamp - int(block_time)) <= diff:
                if action_type == "CREATE_TOKEN" or action_type == "SET_AUTHORITY":
                    timeArray = time.localtime(int(block_time))
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    arr, is_buy = GetPrice.get_token_info(mint_address, arr)
                    if action_type == "CREATE_TOKEN":
                        arr.append("-【科学家创建合约了】温馨提示各位：")
                    else:
                        arr.append("-【科学家创把合约放弃权限】温馨提示各位：")
                    arr.append(str((timestamp - int(block_time)) / 60))
                    arr.append("分钟之前，操作时间：" + otherStyleTime + "\n\r")

                    note_str = "".join(arr)
                    print(note_str)
                    send_markdown(note_str)
                    time.sleep(4)
                    send_markdown_address(mint_address)
                    arr = []
                    # send_markdown_system()
                else:
                    if not token_symbol is None:
                        timeArray = time.localtime(int(block_time))
                        arr, is_buy = GetPrice.get_token_info(mint_address, arr)
                        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                        arr.append("-【科学家设置权限】温馨提示各位：")
                        arr.append(str((timestamp - int(block_time)) / 60))
                        arr.append("分钟之前，烧池子：：" + otherStyleTime + "\n\r")

                        note_str = "".join(arr)
                        print(note_str)
                        send_markdown(note_str)
                        time.sleep(4)
                        send_markdown_address(mint_address)
                        arr = []
        time.sleep(30)
        send_msg()


if __name__ == '__main__':
    request_ok()
