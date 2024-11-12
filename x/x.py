import requests

# 替换为你的 Bearer Token
BEARER_TOKEN = ('AAAAAAAAAAAAAAAAAAAAADabwgEAAAAAc5JV%2FY%2BImkHTXOc341osXGqsvSg'
                '%3DifWxTJDeHAeQwq2CBElYoWspIkDbZgc9ieOdBoWN8nRcgx3BWL')

# 设置请求头
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


# 爬取特定推文的函数
def scrape_tweet(tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tweet_data = response
        print(tweet_data)


print(scrape_tweet("1850775414752547237"))
