import asyncio
import datetime as dt
import logging
import os
import time
from datetime import timezone, timedelta, datetime

import coloredlogs
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# 日志目录
LOGFILE_FIX = "smart-token-sol-"
LOG_PATH = os.getcwd() + "/log/"
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)
# 获取当前日期和时间
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_date_now = now.strftime("%Y-%m-%d %H:%M:%S")
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

TIME = 3

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


def send_telegram_photo(photo):
    token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
    chat_id = '-4535898387'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': ''
    }
    response = requests.post(url, data=payload)
    print(response.json())


def send_telegram_message(message, tokenAddress, tokenSymbol):
    token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
    chat_id = '-4535898387'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    inline_keyboard = [
        [
            {"text": "✅gmgn", "url": "https://gmgn.ai/sol/token/" + tokenAddress},
            {"text": "✅pump", "url": "https://pump.fun/" + tokenAddress},
        ], [
            {"text": "✅搜名称", "url": "https://x.com/search?q=$" + tokenSymbol + "&src=typed_query"},
            {"text": "✅搜合约", "url": "https://x.com/search?q=$" + tokenAddress + "&src=typed_query"},
        ], [
            {"text": "✅buy/sell 一键买卖", "url": "https://t.me/pepeboost_sol04_bot?start"
                                                  "=" + tokenAddress, "callback_data": "like"},
        ],
    ]
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown',
               'reply_markup': {
                   'inline_keyboard': inline_keyboard
               }, }

    response = requests.post(url, json=payload)
    print(response.json())


# https://pump.fun/coin/FjTJCCQpLU4fpH58mN1bTQXiQsjJVYai3QYFjYqYpump
def get_dev_coin():
    tokens = {
        'EZX7c1hARBCiVTY62EJLEPwVsUaZWhmvKkuW3nxexidY': '山羊-Dev',
        '5AGPWxSmkMaKh87sUMLEoek58Xys3KAhqmSaZCf7susm': 'GNON-Dev',
        '6P2XrFUBfm6qGSadmopSMovtqNDN5hWj3JJ3bqjaL2NP': 'ACT-Dev',
        '5W7UZNQk6oCFbNdPowRJZpByErqzifQFVNVtN4uKb3cV': '香蕉-Dev',
        '6a7tZxBST4vbKCD4EGtKNoiRW3bJgcLBg7kiQo2PvGyG': 'LUCE吉祥物-Dev',
        '4G26CB3YnBKbQbM4SyXknb3ZwKcR2apFijADSSQsWEvJ': 'Project89-Dev',
        'Ah3NmLiAw5vCEcfFM2T4tUgZTdTv4uwb5xFQnXxQv6CS': '绿章鱼-Dev',
        '6g1gsuxnNaA2kZtvK8k62AmHrmMuX5dnLj2b7zqTCghx': '红章鱼-Dev',
        'HrHJputHcA8mkwrcQB3GkrJ2u1f7Fm4LzAZptSYSsUcf': 'punt松鼠-Dev',
        'HyYNVYmnFmi87NsQqWzLJhUTPBKQUfgfhdbBa554nMFF': 'Fart-Dev',
        'Btxty83QiNskbHX5XPMWk9o54SYj9uNpKEKkbCu6gL3q': '河马-Dev',
        'Haee7H5bKDCnm6dXLkeR9DcWw9Puhnkwk71QBUSHcpUt': '徐狗Bazingame-Dev',
        'DTQQf6xhbRFqbSUzHsQ4e1PJroCR3dVKvUnt7sj11HJc': 'tictok的宠物CHILLGUY',
        'T5j2UBTvLYPCwDP5MVkSALN7fwuLFDL9jUXJNjjb8sc': 'Rif的dev',
        '7HzeDxUWkpbdEe6RBwfZg4rYfu4pvwajMwh97mMobFq6': 'FATAH的dev'

    }

    headers = {
        'authority': 'frontend-api.pump.fun',
        'accept': '*/*',
        'accept-language': 'zh,zh-CN;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://pump.fun',
        'pragma': 'no-cache',
        'referer': 'https://pump.fun/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'offset': '0',
        'limit': '10',
        'includeNsfw': 'true',
    }

    for token in tokens:
        response = requests.get('https://frontend-api.pump.fun/coins/user-created-coins/' + token, params=params,
                                headers=headers)
        if response.status_code == 200:
            arr = []
            result = response.json()
            for re in result:
                # tokenAddress
                tokenAddress = re["mint"]
                # 名称
                symbol = re["symbol"]
                # url
                image_uri = re["image_uri"]
                # twitter
                twitter = re["twitter"]
                # 创建时间
                tokenCreateTime = int(re["created_timestamp"]) / 1000
                timeArray = time.localtime(tokenCreateTime)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                # 市值
                usd_market_cap = re["usd_market_cap"]
                # 回复数
                reply_count = re["reply_count"]
                print(str(tokens[token]))
                # 获取当前时间
                date = datetime.now()
                timestamp = int(date.timestamp())
                # 对比的时间8分钟的购买
                diff = 60 * TIME
                if (timestamp - int(tokenCreateTime)) <= diff:
                    arr.append("`合约名称：" + symbol + "`\n\r")
                    arr.append("`" + tokenAddress + "`\n\r")
                    arr.append("\n\r")

                    arr.append("`💵 交易：`\n\r")
                    arr.append("|——创建时间：" + otherStyleTime + "⏰\n\r")
                    arr.append("|——当前时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "⏰\n\r")
                    arr.append("|——当前市值：" + format(float(usd_market_cap) / 10000, '.2f') + " W\n\r")
                    # arr.append("|——当前价格：" + format(float(price), '.8f') + " \n\r")
                    minutes_ago = str(round((timestamp - int(tokenCreateTime)) / 60, 2))
                    arr.append("|——合约创建时间：" + minutes_ago + "分钟之前" + "⏰\n\r")
                    arr.append("\n\r")

                    arr.append("`🔔 量化：`\n\r")
                    arr.append("|——Pump的评论数：" + str(reply_count) + " 🟢\n\r")
                    arr.append("|——Dev的名字：" + str(tokens[token]) + " 🟢\n\r")
                    arr.append("\n\r")

                    arr.append("`🔔 复盘：`\n\r")
                    arr.append("|——干二段，逆向思维。；" + " 🟢\n\r")

                    arr.append("\n\r")

                    note_str = "".join(arr)
                    # print(note_str)
                    logger.info('本次解析的数据：\n\r {0}'.format(note_str))
                    # if is_buy:
                    send_telegram_photo(image_uri)
                    send_telegram_message(note_str, tokenAddress, symbol)
                    arr = []
                    time.sleep(3)


if __name__ == '__main__':

    # 创建调度器
    scheduler = AsyncIOScheduler()
    # 添加任务，设置每3分钟执行一次
    scheduler.add_job(get_dev_coin, 'interval', minutes=3)
    # 启动调度器
    scheduler.start()
    # 主程序运行
    try:
        print("Scheduler started. Press Ctrl+C to exit.")
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
        print("Scheduler stopped.")
