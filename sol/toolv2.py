# -*- coding: utf-8 -*
import datetime as dt
import json
import time
from datetime import timezone, timedelta, datetime

import requests

# token_dd = 'a2e2cd49e7ca093d67a4223ed32c59804965edc184697d9fc55cf7c830b7b501'
token_dd = 'a9aab412b508bb619859974fc7fb202668b436574a992efc69b3aef3e14650e9'
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


def request_ok():
    # 获取所有的数据
    url = (f"https://www.okx.com/priapi/v1/invest/activity/smart-money/token/page?pageNo=1&pageSize=10&duration=3"
           f"&order=tokenTradingTime&t=1713151873646")

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
    print("Status code:", response.status_code)
    if response.status_code == 200:
        result = response.json()
        res = result['data']['result']
        # print(res)
        arr = []
        for r in res:  # 第二个实例
            transactionAction = r["transactionAction"]
            tokenSymbol = r["tokenSymbol"]
            tokenLogo = r["tokenLogo"]
            tokenAddress = r["tokenAddress"]
            tokenTradingTime = r["tokenTradingTime"]
            smartMoneyBuyAmount = r["smartMoneyBuyAmount"]
            latestOrderPrice = r["latestOrderPrice"]
            tradeVolume5 = r["tradeVolume5"]
            tradeVolume60 = r["tradeVolume60"]
            tradeVolume1440 = r["tradeVolume1440"]
            smartMoneyCount = r["smartMoneyCount"]
            smartMoneySellCount = r["smartMoneySellCount"]
            smartMoneyBuyCount = r["smartMoneyBuyCount"]

            # 获取当前时间
            date = datetime.now()
            timestamp = int(date.timestamp())
            # 对比的时间8分钟的购买
            diff = 60 * TIME
            if (timestamp - int(tokenTradingTime) / 1000) <= diff:
                if transactionAction == "BUY":
                    get_token = (f"https://www.okx.com/priapi/v1/invest/activity/smart-money/token/holding/list"
                                 f"?pageNo=1&pageSize=50&tokenAddress={tokenAddress}&chainId=501&t=1713227607507")
                    response = requests.get(get_token, headers=headers)
                    print("Status code:", response.status_code)
                    userAddr = []
                    if response.status_code == 200:
                        result = response.json()
                        res = result['data']['result']
                        for s in res:  # 第二个实例
                            userWalletAddress = s["userWalletAddress"]
                            winRate = s["winRate"]
                            yieldRate = s["yieldRate"]
                            userAddr.append("" + userWalletAddress + "\n\r")
                            userAddr.append("★7日内收益：" + winRate + "%\n\r")
                            userAddr.append("★7日内收益率：" + yieldRate + "%\n\r")

                    userList = "".join(userAddr)
                    timeArray = time.localtime(int(tokenTradingTime) / 1000)
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    arr.append("![图片地址：](" + tokenLogo + ")\n\r")
                    arr.append(str(china_time) + "-【买入】：")
                    arr.append(str((timestamp - int(tokenTradingTime) / 1000) / 60))
                    arr.append("分钟之前" + "\n\r")
                    arr.append("当前有：" + str(smartMoneyBuyCount) + "个聪明钱买入\n\r")
                    arr.append("当前有：" + str(smartMoneyCount) + "个聪明钱操作\n\r")
                    arr.append("名称：" + tokenSymbol + "\n\r")
                    arr.append("★购买金额：" + latestOrderPrice + "$\n\r")
                    arr.append("05分钟交易额：" + tradeVolume5 + "$\n\r")
                    arr.append("60分钟交易额：" + tradeVolume60 + "$\n\r")
                    arr.append("24小时交易额：" + tradeVolume1440 + "$\n\r")
                    arr.append("聪明钱地址：" + userList + "\n\r")
                    arr = get_token_info(tokenAddress, arr)
                    arr.append("合约地址：\n\r```" + tokenAddress + "```\n\r")

                    note_str = "".join(arr)
                    print(note_str)
                    send_markdown(note_str)
                    time.sleep(5)
                    send_markdown_address(tokenAddress, "BUY")
                    arr = []
                else:
                    get_token = (f"https://www.okx.com/priapi/v1/invest/activity/smart-money/token/holding/list"
                                 f"?pageNo=1&pageSize=50&tokenAddress={tokenAddress}&chainId=501&t=1713227607507")

                    response = requests.get(get_token, headers=headers)
                    print("Status code:", response.status_code)
                    userAddr = []
                    if response.status_code == 200:
                        result = response.json()
                        res = result['data']['result']
                        for s in res:  # 第二个实例
                            userWalletAddress = s["userWalletAddress"]
                            winRate = s["winRate"]
                            yieldRate = s["yieldRate"]
                            userAddr.append("" + userWalletAddress + "\n\r")
                            userAddr.append("7日内收益：" + winRate + "%\n\r")
                            userAddr.append("7日内收益率：" + yieldRate + "%\n\r")
                    userList = "".join(userAddr)
                    timeArray = time.localtime(int(tokenTradingTime) / 1000)
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    arr.append("![图片地址：](" + tokenLogo + ")\n\r")

                    # arr.append("方式：" + transactionAction + "\n\r")
                    # arr.append("看线：<" + "https://dexscreener.com/solana/" + tokenAddress + ">\n\r")
                    # arr.append("查看合约：<" + "https://www.dexlab.space/mintinglab/spl-token/" + tokenAddress + ">\n\r")
                    # arr.append("检查合约：<" + "https://gmgn.ai/sol/token/" + tokenAddress + ">\n\r")

                    arr.append(str(china_time) + "-\n\r【卖出】：")
                    arr.append(str((timestamp - int(tokenTradingTime) / 1000) / 60))
                    arr.append("分钟之前" + "\n\r")
                    arr.append("当前有：" + str(smartMoneyCount) + "个聪明钱操作\n\r")
                    arr.append("当前有：" + str(smartMoneySellCount) + "个聪明钱卖出\n\r")
                    arr.append("名称：" + tokenSymbol + "\n\r")
                    arr.append("卖出订单金额：" + latestOrderPrice + "$\n\r")
                    arr.append("05分钟交易额：" + tradeVolume5 + "$\n\r")
                    arr.append("60分钟交易额：" + tradeVolume60 + "$\n\r")
                    arr.append("24小时交易额：" + tradeVolume1440 + "$\n\r")
                    # arr.append(
                    #     "推特搜索：<" + "https://twitter.com/search?q=%24" + tokenSymbol + "&src=typed_query>\n\r")
                    # arr.append(
                    #     "推特合约搜索：<" + "https://twitter.com/search?q=%24" + tokenAddress + "&src=typed_query>\n\r")
                    arr = get_token_info(tokenAddress, arr)
                    arr.append("合约地址：\n\r```" + tokenAddress + "```\n\r")
                    # node = request_ok()

                    note_str = "".join(arr)
                    print(note_str)
                    send_markdown(note_str)
                    send_markdown_address(tokenAddress, "SELL")
                    time.sleep(5)
                    arr = []
                if float(smartMoneyBuyAmount) > 600.0:
                    send_markdown_system()
        # time.sleep(60)
        # send_msg()


# 获取token基本信息
def get_token_info(token, arr):
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
        price = res['price']
        price_1m = res['price_1m']
        price_5m = res['price_5m']
        price_1h = res['price_1h']
        holder_count = res['holder_count']
        # logo = res['logo']
        # 检查键'a'是否存在
        key_to_check = 'pool_info'
        quote_reserve = ""
        burn_status = res['burn_status']
        creator_balance = res["creator_balance"]
        social_links = res["social_links"]
        rug_ratio = res['rug_ratio']
        holder_rugged_num = res['holder_rugged_num']
        holder_token_num = res['holder_token_num']
        hot_level = res['hot_level']
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
        arr.append("当前价格：" + str(price) + "$\n\r")
        arr.append("1分钟前价格：" + str(price_1m) + "$\n\r")
        arr.append("5分钟前价格：" + str(price_5m) + "$\n\r")
        arr.append("24小时前价格：" + str(price_1h) + "$\n\r")
        arr.append("池子是否燃烧：" + burn_status + "\n\r")
        arr.append("池子燃烧比率：" + str(burn_ratio) + "%\n\r")
        arr.append("合约创建者余额：" + str(creator_balance) + " Sol\n\r")
        arr.append("合约持有人数：" + str(holder_count) + "\n\r")
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
        if key_to_check in res:
            quote_reserve = res["pool_info"]["quote_reserve"]
            arr.append("★当前池子：" + str(quote_reserve) + " Sol\n\r")
        if float(quote_reserve) > 300.0:
            if hot_level == 1:
                arr.append("【★温馨提示：建议买1s★】 \n\r")
            elif hot_level == 2:
                arr.append("【★温馨提示：建议买2s★】 \n\r")
            elif hot_level >= 3:
                arr.append("【★温馨提示：建议买3s★】 \n\r")
            else:
                arr.append("【★温馨提示，建议先观察★】 \n\r")
        else:
            arr.append("【★温馨提示，池子不足300s，小心★】 \n\r")
        # arr.append("![图片地址：](" + logo + ")\n\r")
        print(arr)
        return arr


if __name__ == '__main__':
    request_ok()
