import datetime
import json
import time

import requests


def send_msg(token_dd, date_str, msg, at_all=False):
    """
    通过钉钉机器人发送内容
    @param date_str:
    @param msg:
    @param at_all:
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    content_str = "{0}定时推送：\n\n{1}\n".format(date_str, msg)

    data = {
        "msgtype": "text",
        "text": {
            "content": content_str
        },
        # "at": {
        #     "isAtAll": at_all
        # },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)


def request_ok():
    url = f"https://www.okx.com/priapi/v1/invest/activity/smart-money/list?pageNo=1&t=1711533530879"
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
            # print(r)
            transactionAction = r["transactionAction"]
            tokenSymbol = r["tokenSymbol"]
            tokenLogo = r["tokenLogo"]
            tokenAddress = r["tokenAddress"]
            orderPrice = r["orderPrice"]
            investmentTime = r["investmentTime"]
            arr.append("方式：" + transactionAction + "\n\r")
            arr.append("Token：" + tokenSymbol + "\n\r")
            arr.append("logo：" + tokenLogo + "\n\r")
            arr.append("合约地址：" + tokenAddress + "\n\r")
            arr.append("聪明钱购买金额：" + orderPrice + "\n\r")
            timeArray = time.localtime(int(investmentTime) / 1000)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            arr.append("购买时间：" + otherStyleTime + "\n\r")
            arr.append("--------------------------------------\n\r")
        return arr


if __name__ == '__main__':
    node = request_ok()
    str1 = "".join(node)
    print(str1)
    token_dd = ''
    note_str = "SOL-深度学习聪明钱包\n\r" + str1
    date_str = datetime.datetime.now().strftime('%H:%M')
    send_msg(token_dd, date_str, note_str, True)
