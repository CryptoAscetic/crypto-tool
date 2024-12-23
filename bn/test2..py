import ssl

from requests_html import HTMLSession


def find_futures_coin():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48#/48'
    result = HTMLSession().get(url).html.search('usDⓢ-M {} Perpetual Contracts')
    if result is not None:
        msg = f'檢測到幣按添加幣種:{result[0]}({result[1]})'
        print(msg)
        msg = result[0]
        print(result)
    else:
        print("暂未检测到")


if __name__ == '__main__':
    find_futures_coin()
