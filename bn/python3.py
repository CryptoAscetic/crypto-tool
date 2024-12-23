import ssl

from requests_html import HTMLSession

# # #def find_futures_coin():
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48'

result = HTMLSession().get(url).html.search('USDⓈ-Margined {} Perpetual Contracts')
print(result)
