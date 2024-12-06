import requests


def get_proxy_ips():
    url = 'http://www.zdopen.com/ShortProxy/GetIP/?api=202406141434087624&akey=ebd0c7a845dbcc97&timespan=5&type=1'  # 替换为代理IP网站的URL
    response = requests.get(url)
    if response.status_code == 200:
        proxy_ips = response.text  # 假设返回的是JSON格式数据
        return proxy_ips
    else:
        return []


def bing_plist():
    url = ('http://www.zdopen.com/ShortProxy/BindIPList/?api=202406141434087624&'
           'akey=ebd0c7a845dbcc97&ipList=123.14.75.177')  # 替换为代理IP网站的URL
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()  # 假设返回的是JSON格式数据
        return result
    else:
        return []


def is_valid_proxy(proxy):
    proxies = {
        'http': f'http://{proxy["ip"]}:{proxy["port"]}',
        'https': f'https://{proxy["ip"]}:{proxy["port"]}',
    }
    url = 'http://example.com'  # 替换为需要验证的URL
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False


if __name__ == '__main__':
    # print(bing_plist())
    proxy_ips = get_proxy_ips()
    print(proxy_ips)

    for proxy in proxy_ips:
        if is_valid_proxy(proxy):
            print(f"有效代理IP：{proxy['ip']}:{proxy['port']}")
