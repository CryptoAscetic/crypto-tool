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

# 日志目录
LOGFILE_FIX = "smart-token-count-"
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
# 数据库初始化ute5lU7SrMPfsz
mydb = mysql.connector.connect(host='block.chain.com', user='root', password='ute5lU7SrMPfsz', database='blockchain',
                               port='13306')

# token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'

token_dd = '2fb4e8566e1348bf837cd8527798b8f4461287a2403bda7d15f9903ee8592909'
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


def number_repeat_data():
    my_cursor = mydb.cursor()
    # SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%s')
    select_sql = ("SELECT count(token_symbol) AS recomme_count, token_symbol, token_address , date_format(DATE_ADD( "
                  "create_time, INTERVAL 8 HOUR), '%Y-%m-%d') AS create_time FROM block_smart_record WHERE  "
                  "date_format(DATE_ADD(create_time, INTERVAL 8 HOUR), '%Y-%m-%d') = DATE_FORMAT(DATE_ADD(now(),"
                  "INTERVAL 8 HOUR),'%Y-%m-%d') AND recomme_count > "
                  "0 GROUP BY token_symbol, token_address, date_format(DATE_ADD(create_time, INTERVAL 8 HOUR),  "
                  "'%Y-%m-%d') ORDER BY recomme_count DESC LIMIT 10")
    my_cursor.execute(select_sql)
    my_result = my_cursor.fetchall()
    markdown_table = create_simple_table(my_result)
    print(markdown_table)
    send_markdown(markdown_table)
    logger.info("本次执行统计结果：{0}".format(my_result))
    return my_result


def create_simple_table1(data):
    table = "| Header1 | Header2 |\n| ------- | ------- |\n"
    for row in data:
        table += f"| {row[0]} | {row[1]} |\n"
    return table


def create_simple_table(data):
    table = "| 推荐次数 | 合约名称 | 密码 | 时间 \n| ----------- | ----------- | ----------- | ----------- |\n"
    for row in data:
        table += f"| {row[0]} | {row[1]} |{row[2]}|{row[3]}|\n"
    return table


def number_repeat_data_smart():
    my_cursor = mydb.cursor()
    # SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%s')
    select_sql = ("SELECT token_symbol, token_address, max(smart_money_buy_count) AS buyCount FROM ( SELECT "
                  "token_symbol, token_address, smart_money_buy_count FROM block_smart_record WHERE date_format("
                  "create_time, '%Y-%m-%d') > date_format(DATE_sub(now(), INTERVAL 2 DAY), '%Y-%m-%d') ) a GROUP BY "
                  "token_address, token_symbol ORDER BY buyCount DESC LIMIT 20")
    my_cursor.execute(select_sql)
    my_result = my_cursor.fetchall()
    markdown_table = create_simple_table_smart(my_result)
    print(markdown_table)
    send_markdown(markdown_table)
    logger.info("本次执行统计结果：{0}".format(my_result))
    return my_result


def create_simple_table_smart(data):
    table = "| 合约名称 | 密码 | 大数据汇总聪明钱购买次数 | \n| ------- | ------- | ------- |\n"
    for row in data:
        table += f"| {row[0]} | {row[1]} |{row[2]}|\n"
    return table


def number_repeat_data_smart_less():
    my_cursor = mydb.cursor()
    # SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%s')
    select_sql = ("select * from ( select token_symbol, token_address, max(smart_money_buy_count) as buyCount from ( "
                  "select token_symbol,token_address,smart_money_buy_count from block_smart_record where date_format( "
                  "create_time, '%Y-%m-%d') > date_format(DATE_sub(now(), INTERVAL 2 day ), '%Y-%m-%d')) a group by "
                  "token_address, token_symbol limit 20) b where buyCount <3")
    my_cursor.execute(select_sql)
    my_result = my_cursor.fetchall()
    markdown_table = create_simple_table_smart_less(my_result)
    print(markdown_table)
    send_markdown(markdown_table)
    logger.info("本次执行统计结果：{0}".format(my_result))
    return my_result


def create_simple_table_smart_less(data):
    table = "| 合约名称 | 密码 | 一般聪明钱购买次数 | \n| ------- | ------- | ------- |\n"
    for row in data:
        table += f"| {row[0]} | {row[1]} |{row[2]}|\n"
    return table


if __name__ == '__main__':
    number_repeat_data()
    number_repeat_data_smart()
    number_repeat_data_smart_less()
