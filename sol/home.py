import json

import brotli
import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from moralis import sol_api


def get_token_holders(token):
    url = f"https://api.solscan.io/v2/token/holders?token={token}&offset=0&size=20&cluster="
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
        "Au-Be": "%10%06yQXvR%05wVZ%0E%19",
        "Origin": "https://solscan.io",
        "Referer": "https://solscan.io/",
        "Sec-Ch-Ua": 'sec-ch-ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    # Decompressing Brotli compressed response
    if 'br' in response.headers.get('Content-Encoding', ''):
        try:
            decompressed_data = brotli.decompress(response.content)
            response_data = decompressed_data.decode('utf-8')
        except (brotli.error, UnicodeDecodeError):
            print("Failed to decompress the response content.")
            response_data = response.content.decode('utf-8')
    else:
        response_data = response.text

    # print("Response body:", response_data)
    data = json.loads(response_data)
    return data


api_key = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
           ".eyJjcmVhdGVkQXQiOjE3MTAwNzUyMjI4NzUsImVtYWlsIjoiaHVhbmdmZW5nZ2UxMjAxQGdtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImlhdCI6MTcxMDA3NTIyMn0.7Y5AxRTT4yCeavwe1C7HYFUlBerN1nSu5lwbiRe9VZg")


def get_token_info(address):
    url = "https://solana-gateway.moralis.io/token/mainnet/9nvM2qJZYwV8YwtWeFx6sAAtYkV9TyPcVwWyHmcj6NU7/metadata"

    params = {
        "network": "mainnet",
        "address": address
    }
    try:

        result = sol_api.account.balance(
            api_key=api_key,
            params=params,
        )

        return float(result['solana'])
    except:
        print('null')


st.title('Solana 合约分析')
token = st.text_input('输入 Solana 合约地址:')

if token:
    # 数据加载提示
    with st.spinner('正在获取合约持有者数据...'):
        data = get_token_holders(token)

    tokeninfo = []
    # 进度条
    progress_bar = st.progress(0)
    total = len(data['data']['result'])
    for index, item in enumerate(data['data']['result']):
        owner = item['owner']
        rank = item['rank']
        solana = get_token_info(owner)
        tokeninfo.append([owner, rank, solana])

        # 更新进度条
        progress_bar.progress((index + 1) / total)

    # 清除进度条
    progress_bar.empty()

    # 将数据转换为 pandas DataFrame
    df = pd.DataFrame(tokeninfo, columns=['Address', 'Rank', 'SOL'])

    # 绘制图表
    st.title('SOL Balances for Different Addresses')
    fig, ax = plt.subplots()
    ax.bar(df['Address'], df['SOL'], color='skyblue')
    plt.xlabel('地址')
    plt.ylabel('SOL 余额')
    plt.xticks(rotation=45, ha='right')

    # 显示图表
    st.pyplot(fig)
