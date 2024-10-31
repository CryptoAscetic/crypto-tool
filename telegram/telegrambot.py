import requests

token = '7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ'
chat_id = '-1002475514494'
message = "EYmuLAEhEWTuyjxP8EJBvd4yAZB2P99NfnWt3EqHpump"

url = f'https://api.telegram.org/bot{token}/sendMessage'
payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}

response = requests.post(url, data=payload)
print(response.json())
