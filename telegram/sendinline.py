import requests

# 替换为你的 API TOKEN 和聊天 ID
token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
chat_id = '-4594318180'
message = '机器人：'

inline_keyboard = [
    [
        {"text": "buy/sell 一键买卖",
         "url": "https://t.me/pepeboost_sol04_bot?start=3BeJ9zCgQhaqKMu2HgKJ79yQBChD1Pf3hPwRX44fpump"},
    ]
]

payload = {
    'chat_id': chat_id,
    'text': message,
    'reply_markup': {
        'inline_keyboard': inline_keyboard
    }
}

url = f'https://api.telegram.org/bot{token}/sendMessage'
response = requests.post(url, json=payload)
print(response.json())
