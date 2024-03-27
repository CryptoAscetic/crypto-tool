import datetime
import json

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
        "at": {
            "isAtAll": at_all
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)  # 直接一句post就可以实现通过机器人在群聊里发消息
    print(res.text)

    # return res.text


if __name__ == '__main__':
    token_dd = 'd9f66c8fad593f066bb4a670b5d4d6a27fa4fde8fdd324b94dd7c4e6f8b3d584'
    note_str = "钱包DataWhale自动化组队学习中..."
    date_str = datetime.datetime.now().strftime('%H:%M')
    send_msg(token_dd, date_str, note_str, True)
