import json

import requests

TOKEN = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
CHAT_ID = '-4594318180'
# 创建 Inline Keyboard
keyboard = {
    "inline_keyboard": [
        [
            {"text": "👍 点赞", "callback_data": "like"}
        ]
    ]
}

# 发送消息
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
payload = {
    'chat_id': CHAT_ID,
    'text': '请给我点赞！',
    'reply_markup': json.dumps(keyboard)
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('消息发送成功！')
else:
    print('消息发送失败！', response.text)
