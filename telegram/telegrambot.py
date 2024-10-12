import requests

token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
chat_id = '-4594318180'
message = """
名称       | 年龄 | 城市
----------|------|------
Alice     | 25   | New York
Bob       | 30   | London
Charlie   | 22   | Paris
"""

url = f'https://api.telegram.org/bot{token}/sendMessage'
payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}

response = requests.post(url, data=payload)
print(response.json())
