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

# token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'

token_dd = 'a9aab412b508bb619859974fc7fb202668b436574a992efc69b3aef3e14650e9'
# 分钟
TIME = 3
tokenFDVMax = 500000

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
           "9.新狗SOL链千万别过夜，赚钱就卖;\n", "10.机会是跌出来的，不是冲出来的\n\r"]
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
            "title": str(china_time) + "sol-复制粘贴",
            "text": address
        },
    }

    buy_data = {
        # "at": {
        #     "isAtAll": True
        # },
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
    url = (f"https://www.okx.com/priapi/v1/invest/activity/smart-money/token/page?pageNo=1&pageSize=10&duration=3"
           f"&order=tokenTradingTime&chainId=501&txnSource=1%2C2&t=1727484671680")

    headers = {
        "accept": "application/json",
        "accept-language": "zh,zh-CN;q=0.9",
        "app-type": "web",
        "cache-control": "no-cache",
        "devid": "70c5f320-7c00-449d-95ba-d1d7af318bfc",
        "platform": "web",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-cdn": "https://www.okx.com",
        "x-id-group": "1020115334522480014-c-7",
        "x-locale": "zh_CN",
        "x-site-info": "==QfxojI5RXa05WZiwiIMFkQPx0Rfh1SPJiOiUGZvNmIsIyVUJiOi42bpdWZyJye",
        "x-utc": "8",
        "x-zkdex-env": "0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        res = result['data']['result']
        arr = []
        for r in res:  # 第二个实例
            transactionAction = r["transactionAction"]
            tokenAddress = r["tokenAddress"]
            tokenTradingTime = r["tokenTradingTime"]
            latestOrderPrice = r["latestOrderPrice"]
            smartMoneySellCount = r["smartMoneySellCount"]
            smartMoneyBuyCount = r["smartMoneyBuyCount"]
            smartMoneyBuyAmount = r["smartMoneyBuyAmount"]
            smartMoneySellAmount = r["smartMoneySellAmount"]
            tokenLogo = r["tokenLogo"]
            tokenSymbol = r["tokenSymbol"]
            tokenCreateTime = int(r["tokenCreateTime"]) / 1000
            timeArray = time.localtime(tokenCreateTime)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            # 市值
            tokenFDV = r['tokenFDV']
            # 5分钟交易量
            tradeVolume5 = r['tradeVolume5']
            # 1小时交易量
            tradeVolume60 = r['tradeVolume60']

            # 获取当前时间
            date = datetime.now()
            timestamp = int(date.timestamp())
            # 对比的时间8分钟的购买
            diff = 60 * TIME
            if (timestamp - int(tokenTradingTime) / 1000) <= diff:
                if transactionAction == "BUY":
                    # 市值大于50万
                    if float(tokenFDV) > tokenFDVMax:
                        # arr, is_buy = GetPrice.get_token_info(tokenAddress, arr)
                        if not tokenLogo is None:
                            arr.append("![图片地址：](" + tokenLogo + ")\n\r")
                        arr.append("【SOL-买买买】合约创建时间：" + otherStyleTime + "\n\r")
                        arr.append("名称：" + tokenSymbol + "\n\r")
                        arr.append("★市值：" + format(float(tokenFDV), '.2f') + " $\n\r")
                        price = GetSolTokenPrice.get_token_price(tokenAddress)
                        arr.append("★当前价格：" + format(float(price), '.8f') + " $\n\r")
                        minutes_ago = str(round((timestamp - int(tokenTradingTime) / 1000) / 60, 2))
                        arr.append("买入时间：" + minutes_ago + "分钟之前" + "\n\r")
                        arr.append("★聪明钱个数：" + str(smartMoneyBuyCount) + "个\n\r")
                        arr.append("聪明钱买入总额：" + format(float(smartMoneyBuyAmount), '.2f') + " $\n\r")
                        arr.append("聪明钱卖出总额：" + format(float(smartMoneySellAmount), '.2f') + "$\n\r")
                        arr.append("★购买金额：" + format(float(latestOrderPrice), '.2f') + " $\n\r")
                        arr.append("5分钟交易金额：" + format(float(tradeVolume5), '.2f') + " $\n\r")
                        arr.append("1小时交易总金额：" + format(float(tradeVolume60), '.2f') + " $\n\r")
                        arr.append("看线地址：<" + "https://dexscreener.com/solana/" + tokenAddress + ">\n\r")
                        look_line = "https://gmgn.ai/sol/token/" + tokenAddress
                        arr.append("AI看：<" + look_line + ">\n\r")
                        arr.append(
                            "查看合约：<" + "https://www.dexlab.space/mintinglab/spl-token/" + tokenAddress + ">\n\r")
                        note_str = "".join(arr)
                        # print(note_str)
                        logger.info('本次解析的数据：\n\r {0}'.format(note_str))
                        # if is_buy:
                        send_markdown(note_str)
                        time.sleep(5)
                        send_markdown_address(tokenAddress, "BUY")
                        arr = []
                        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        insert_data(tokenLogo, tokenSymbol, tokenAddress, format(float(tokenFDV), '.2f'), price,
                                    minutes_ago, str(smartMoneyBuyCount),
                                    format(float(smartMoneyBuyAmount), '.2f'),
                                    format(float(smartMoneySellAmount), '.2f'),
                                    format(float(latestOrderPrice), '.2f'), format(float(tradeVolume5), '.2f'),
                                    format(float(tradeVolume60), '.2f'),
                                    "", "", look_line, 501, otherStyleTime, now,
                                    1, "SOL链")
                else:
                    # arr, is_buy = GetPrice.get_token_info(tokenAddress, arr)
                    if not tokenLogo is None:
                        arr.append("![图片地址：](" + tokenLogo + ")\n\r")
                    arr.append("【卖卖卖】合约创建时间：" + otherStyleTime + "\n\r")
                    arr.append("名称：" + tokenSymbol + "\n\r")
                    arr.append(str(round((timestamp - int(tokenTradingTime) / 1000) / 60, 2)))
                    arr.append("分钟之前" + "\n\r")
                    arr.append(str(round((timestamp - int(tokenTradingTime) / 1000) / 60, 2)))
                    arr.append("分钟之前" + "\n\r")
                    arr.append("狗庄跑了，卖：" + str(smartMoneySellCount) + "个聪明钱卖出\n\r")
                    arr.append("★卖出订单金额：" + latestOrderPrice + "$\n\r")
                    note_str = "".join(arr)
                    # print(note_str)
                    # if is_buy:
                    # send_markdown(note_str)
                    # send_markdown_address(tokenAddress, "SELL")
                    # time.sleep(5)
                    # if float(smartMoneyBuyAmount) > 600.0:
                    #     send_markdown_system()
                    arr = []

        # time.sleep(60)
        # send_msg()


# 保存数据
def insert_data(img_url, token_symbol, token_address, token_fdv, price, minutes_ago, smart_money_buy_count,
                smart_money_buy_amount, smart_money_sell_amount, latest_order_price, trade_volume_5, trade_volume_60,
                wallet_address, twitter, look_line, chain_id, token_create_time, create_time, recomme_count, remark):
    my_cursor = mydb.cursor()
    # 保存数据库
    sql = ("INSERT INTO block_smart_record (img_url, token_symbol, token_address, token_fdv, price, minutes_ago, "
           "smart_money_buy_count, smart_money_buy_amount, smart_money_sell_amount, latest_order_price, "
           "trade_volume_5, trade_volume_60, wallet_address, twitter, look_line, chain_id, token_create_time, "
           "create_time, recomme_count, remark) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, "
           "%s, %s, %s, %s)")
    val = (
        img_url, token_symbol, token_address, token_fdv, price, minutes_ago, smart_money_buy_count,
        smart_money_buy_amount, smart_money_sell_amount, latest_order_price, trade_volume_5, trade_volume_60,
        wallet_address, twitter, look_line, chain_id, token_create_time, create_time, recomme_count, remark)
    my_cursor.execute(sql, val)
    mydb.commit()
    logger.info("布料数据保存成功条数{0},合约地址:{1}".format(my_cursor.rowcount, token_address))




if __name__ == '__main__':
    request_ok()
