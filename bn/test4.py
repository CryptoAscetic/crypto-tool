import requests

cookies = {
    'nft-init-compliance': 'true',
    'bnc-uuid': 'e9d473e5-b24f-49d4-94d5-1784163a12fb',
    'userPreferredCurrency': 'USD_USD',
    'ref': 'JULHQYON',
    'refstarttime': '1731313568003',
    'se_gd': 'wQYVRBgJXDEB1YTQEWxsgZZChCQIRBRUlAWRdVUVVBXUgU1NWUUM1',
    'se_gsd': 'Yyc0XCtjICcjBig7NDYhFTI8ClVWAAoRVl9CUldXUFBRHVNT1',
    'lo_uid': '1731313572506-quhlnprrhlp',
    'OptanonAlertBoxClosed': '2024-11-11T08:27:40.837Z',
    'BNC_FV_KEY': '33cf2a40df86aa82ab3dfb334be085a41db9ddd1',
    'lang': 'zh-cn',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219232182f161542-02fa19b491cdda8-10462c6c-2073600-19232182f1717d8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMzIxODJmMTYxNTQyLTAyZmExOWI0OTFjZGRhOC0xMDQ2MmM2Yy0yMDczNjAwLTE5MjMyMTgyZjE3MTdkOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219232182f161542-02fa19b491cdda8-10462c6c-2073600-19232182f1717d8%22%7D',
    'theme': 'dark',
    'BNC_FV_KEY_T': '101-07kFua1XJBhY8LiEqGdq6M61LySmrguEEFmWTDim%2Be1CE7NFc3JHUlu02%2Ba02KRA3ZnRQ0zntDYRjPgVYQMVxw%3D%3D-xOa1TLjhSiiVZU3k52cy4Q%3D%3D-a9',
    'BNC_FV_KEY_EXPIRE': '1732517669484',
    '_gid': 'GA1.2.1983977497.1732496070',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Nov+25+2024+10%3A44%3A28+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5def0abf-2341-4fd3-9a73-cbcfd7ba5478&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&intType=1&geolocation=HK%3B',
    '_ga': 'GA1.2.2120616442.1731313569',
    '_ga_3WP50LGEEC': 'GS1.1.1732500487.6.1.1732502669.55.0.0',
}

headers = {
    'authority': 'www.binance.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh,zh-CN;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'nft-init-compliance=true; bnc-uuid=e9d473e5-b24f-49d4-94d5-1784163a12fb; userPreferredCurrency=USD_USD; ref=JULHQYON; refstarttime=1731313568003; se_gd=wQYVRBgJXDEB1YTQEWxsgZZChCQIRBRUlAWRdVUVVBXUgU1NWUUM1; se_gsd=Yyc0XCtjICcjBig7NDYhFTI8ClVWAAoRVl9CUldXUFBRHVNT1; lo_uid=1731313572506-quhlnprrhlp; OptanonAlertBoxClosed=2024-11-11T08:27:40.837Z; BNC_FV_KEY=33cf2a40df86aa82ab3dfb334be085a41db9ddd1; lang=zh-cn; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219232182f161542-02fa19b491cdda8-10462c6c-2073600-19232182f1717d8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMzIxODJmMTYxNTQyLTAyZmExOWI0OTFjZGRhOC0xMDQ2MmM2Yy0yMDczNjAwLTE5MjMyMTgyZjE3MTdkOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219232182f161542-02fa19b491cdda8-10462c6c-2073600-19232182f1717d8%22%7D; theme=dark; BNC_FV_KEY_T=101-07kFua1XJBhY8LiEqGdq6M61LySmrguEEFmWTDim%2Be1CE7NFc3JHUlu02%2Ba02KRA3ZnRQ0zntDYRjPgVYQMVxw%3D%3D-xOa1TLjhSiiVZU3k52cy4Q%3D%3D-a9; BNC_FV_KEY_EXPIRE=1732517669484; _gid=GA1.2.1983977497.1732496070; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Nov+25+2024+10%3A44%3A28+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5def0abf-2341-4fd3-9a73-cbcfd7ba5478&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&intType=1&geolocation=HK%3B; _ga=GA1.2.2120616442.1731313569; _ga_3WP50LGEEC=GS1.1.1732500487.6.1.1732502669.55.0.0',
    'pragma': 'no-cache',
    'referer': 'https://t.co/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    'type': '1',
    'pageNo': '1',
    'pageSize': '5',
}

response = requests.get('https://www.binance.com/bapi/composite/v1/public/cms/article/list/query', params=params,
                        cookies=cookies, headers=headers)

print(response)
