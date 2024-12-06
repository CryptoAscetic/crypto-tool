import requests

TOKEN = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
CHAT_ID = '-4594318180'
LINK_TEXT = '点击这里'
LINK_URL = 'https://gmgn.ai/sol/token/pBbJV9S0_FLFRDqvz8xPHNDx1Zc8M76x7h8zcaBHoe4fPFb8Ypump'
MESSAGE = f'百度一下：[ {LINK_TEXT} ]({LINK_URL})'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
payload = {
    'chat_id': CHAT_ID,
    'text': MESSAGE,
    'parse_mode': 'Markdown'  # 或者使用 'MarkdownV2'
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('消息发送成功！')
else:
    print('消息发送失败！', response.text)
