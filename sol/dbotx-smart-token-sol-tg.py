# -*- coding: utf-8 -*
import datetime as dt
import json
import logging
import os
import time
from datetime import timezone, timedelta, datetime

import coloredlogs
import mysql.connector
import requests

from SolTokenPrice import GetSolTokenPrice

# 日志目录
LOGFILE_FIX = "smart-token-sol-"
LOG_PATH = os.getcwd() + "/log/"
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)
# 获取当前日期和时间
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
# 设置日志等级
logger.setLevel(logging.DEBUG)
# 追加写入文件a ，设置utf-8编码防止中文写入乱码
formatted_date_log = logging.FileHandler(LOG_PATH + LOGFILE_FIX + formatted_date + '.log', 'a', encoding='utf-8')
# 向文件输出的日志级别
formatted_date_log.setLevel(logging.DEBUG)
# 向文件输出的日志信息格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s -%(process)s')
formatted_date_log.setFormatter(formatter)
# 加载文件到logger对象中
logger.addHandler(formatted_date_log)
# 数据库初始化
mydb = mysql.connector.connect(host='block.chain.com', user='root', password='ute5lU7SrMPfsz', database='blockchain',
                               port='13306')

TIME = 20
token_dd = 'be66323915f3254406e75448783a1af708c93ba3ce4d9ec2ebc8bf9e1c5b01dc'
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


def send_telegram_photo(photo):
    token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
    chat_id = '-4532879792'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': ''
    }
    response = requests.post(url, data=payload)
    print(response.json())


def send_telegram_message(message, tokenAddress):
    token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
    chat_id = '-4532879792'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    inline_keyboard = [
        [
            {"text": "✅gmgn", "url": "https://gmgn.ai/sol/token/" + tokenAddress},
            # {"text": "✅dexlab", "url": "https://www.dexlab.space/mintinglab/spl-token/"
            #                            "=" + tokenAddress},
            {"text": "✅buy/sell 一键买卖", "url": "https://t.me/pepeboost_sol04_bot?start"
                                                  "=" + tokenAddress},
        ]
    ]
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown',
               'reply_markup': {
                   'inline_keyboard': inline_keyboard
               }, }

    response = requests.post(url, json=payload)
    print(response.json())


def request_ok():
    tokens = {
        # '515FRkgdKUunk4BJGndav2FgZniEqYtkdLqcgc8nLSNV': '大帅',
        '441bsKo6VHuhyUhkDiGxYKXyoZzNuF2Ru4hbPteFiEdn': 'klöss',
        'DG6QpsjvwqCGyLAYXKEmDBLRfomJ2UAmoe4MJWL9fNtt': 'Queenkayx ❤',
        'BgJrk3AJEWf41WxThAvDCkZmxuxbt3Q4aZc1P2rrHtZV': 'not BusinessWeek',
        'Gf9XgdmvNHt8fUTFsWAccNbKeyDXsgJyZN8iFJKg5Pbd': '0xuezhang|985.eth',
        '4zhALcaaGZQGexZE7VpX5Nk1ihHRDz9nfGCSt3FRy4z1': 'a-z',
        '4hBL4Z2Tvn2bCNqZniAxL82xviPJaTQeyKMdnLwsVt7L': 'happy第一人',
        '2pekTQKDsJkd7qUMVD6Z5AGdUuuQ2ZF7zGDmhKjjgVdr': "狙击001"
    }
    for token in tokens.keys():
        time.sleep(3)
        # 获取所有的数据
        url = (f"https://servapi.dbotx.com/smart_wallet/trades/" + token)
        params = {
            'page': '0',
            'size': '20',
            'type': '',
            'mint': '',
            'dexName': '',
        }
        headers = {
            'authority': 'servapi.dbotx.com',
            'accept': '*/*',
            'accept-language': 'zh,zh-CN;q=0.9',
            'origin': 'https://dbotx.com',
            'referer': 'https://dbotx.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'x-api-key': '',
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            result = response.json()
            res = result['res']
            arr = []
            for r in res:  # 第二个实例
                logger.info(r)
                # 购买方方式
                buyType = r["type"]
                blockTime = r["blockTime"]
                timeArray = time.localtime(blockTime)
                buyAtTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                # 合约名称
                mint = r["mint"]
                # 总卖出
                solAmount = r["solAmount"]
                # 数量
                quantity = r["quantity"]
                usdRate = r["usdRate"]
                if buyType == "sell":
                    if 'sellProfit' in r.keys():
                        # 盈利sol数量
                        sellProfit = r["sellProfit"]
                else:
                    sellProfit = 0.0

                tokenMeta = r["tokenMeta"]
                if 'updateAt' in tokenMeta.keys():
                    # 创建时间
                    createAt = tokenMeta["updateAt"]
                    timeArray = time.localtime(createAt / 1000)
                    createAtTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                else:
                    createAtTime = "0000-00-00 00:00:00"

                # 合约名称
                symbol = tokenMeta["symbol"]

                # 获取当前时间
                date = datetime.now()
                timestamp = int(date.timestamp())
                # 对比的时间8分钟的购买
                diff = 60 * TIME
                if (timestamp - int(blockTime)) <= diff:
                    arr.append("聪明钱标签：" + str(tokens[token]) + "\n\r")
                    arr.append("`合约名称：" + symbol + "`\n\r")
                    arr.append("`" + mint + "`\n\r")
                    arr.append("\n\r")

                    arr.append("`💵 交易：`\n\r")
                    arr.append("|——创建时间：" + createAtTime + "⏰\n\r")
                    arr.append("|——交易时间：" + buyAtTime + "⏰\n\r")
                    arr.append("|——交易类型：" + buyType + "\n\r")
                    price = GetSolTokenPrice.get_token_price(mint)
                    arr.append("|——当前价格：" + format(float(price), '.8f') + " \n\r")
                    arr.append("\n\r")

                    arr.append("`🔔 量化：`\n\r")
                    arr.append("|——交易金额：" + format(float(solAmount) * usdRate, '.2f') + " 🟢\n\r")
                    arr.append("|——代币数量：" + format(float(quantity), '.2f') + " 个🟢\n\r")
                    arr.append("|——盈利金额：" + format(float(sellProfit) * usdRate, '.2f') + " 🟢\n\r")
                    arr.append("\n\r")

                    note_str = "".join(arr)
                    # print(note_str)
                    logger.info('本次解析的数据：\n\r {0}'.format(note_str))
                    send_telegram_message(note_str, mint)
                    send_markdown(note_str)
                    time.sleep(1)
                    send_markdown_address(mint, "BUY")
                    arr = []


if __name__ == '__main__':
    request_ok()
