import requests


class GetSolTokenPrice:
    @staticmethod
    def get_token_price(token):
        url = "https://price.jup.ag/v4/price?ids=" + token
        headers = {
            "authority": "price.jup.ag",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh,zh-CN;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://solscan.io",
            "pragma": "no-cache",
            "referer": "https://solscan.io/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                          "Safari/537.36",
        }
        response = requests.get(url, headers=headers)
        print("Status code:", response.status_code)
        # print(response.text)
        result = response.json()
        print(result)
        if len(result['data']) > 0:
            price = result["data"][token]['price']
        else:
            price = 0.0
        print(price)
        return price


if __name__ == '__main__':
    print(GetSolTokenPrice.get_token_price("6QSVGUEyBZWRshnXKhS96NQ97vGWiTu61SyHLAbYpump"))
