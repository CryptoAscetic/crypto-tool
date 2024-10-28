要自定义 Telegram 消息推送，你可以使用 Telegram Bot API 创建一个机器人并发送消息。以下是基本步骤：

1. **创建一个 Telegram 机器人**：
    - 在 Telegram 中搜索 @BotFather，发送 `/newbot` 指令。
    - 按照提示设置机器人名称和用户名。
    - 获取你的机器人的 API Token。

2. **获取聊天 ID**：
    - 你可以发送一条消息给你的机器人，然后访问 `https://api.telegram.org/bot<你的API_TOKEN>/getUpdates` 来获取聊天 ID。

3. **发送消息**：
    - 使用下面的请求格式发送消息：
      ```
      https://api.telegram.org/bot<你的API_TOKEN>/sendMessage?chat_id=<聊天ID>&text=<你的消息>
      ```

4. **使用编程语言**：
    - 你可以使用 Python、Node.js 等语言调用这个 API。例如，使用 Python 的 requests 库：
      ```python
      import requests
 
      token = '你的API_TOKEN'
      chat_id = '你的聊天ID'
      message = '自定义消息内容'
 
      url = f'https://api.telegram.org/bot{token}/sendMessage'
      payload = {'chat_id': chat_id, 'text': message}
 
      response = requests.post(url, data=payload)
      print(response.json())
      ```

5. **自定义功能**：
    - 你可以集成更多的功能，比如定时推送、条件触发及图片或文件发送等。

有任何具体问题或者需要更详细的示例吗？😊

| 合约名称    | 密码                                           | 聪明钱购买次数 | 
|---------|----------------------------------------------|---------|
| MILKBAG | 2ubuHGFS4VJVxSEpvV3kDwz6JiuXdaAoGMwrwYC87tp8 | 1       |
| $Pot    | 4F9ynftRHYq3UndTqpTr7hPUUgpynCPiqHxJisqGtXjH | 1       |

## 查询群组id

https://api.telegram.org/bot7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ/getUpdates

# 查看我的信息

https://api.telegram.org/bot7492697040:AAHiTquko-VvkS15tqOcdA5Sk-TLy9EDceQ/getMe

# docs

https://docs.google.com/document/d/1bL-Gjk56w6UE0npSy3i8e-zblwBTHBCI_L1vCYgzOZM/edit?tab=t.gpz4ldognvfr