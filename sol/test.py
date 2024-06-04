import requests


def base58_decode(cipher_input: str) -> str:
    """
    base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
    :param cipher_input: 输入base58编码值
    :return: base58的解码值
    @author hongfeiyinxue 2022-04-30-1651329023.0065577
    """
    #  定义base58的58个编码
    base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    cipher = cipher_input
    #  检查密文字符的有效性，密文字符必须是base58中的字符，否则返回提示
    bad = ''
    for item in cipher:
        if base58.find(item) == -1:
            bad += item
    if bad != '':
        return '不是有效的Base58编码，请仔留意如下字符：' + bad

    #    获取密文每个字符在base58中的下标值
    tmp = []
    for item in cipher:
        tmp.append(base58.find(item))
    temp = tmp[0]
    for i in range(len(tmp) - 1):
        temp = temp * 58 + tmp[i + 1]
    temp = bin(temp).replace('0b', '')
    #    print('temp=', temp, '-len-', len(temp))

    #   判断temp二进制编码数量能否被8整除，例如编码长度为18，首先截取（18%8）余数个字符求对应的ascii字符
    remainder = len(temp) % 8
    plain_text = ''

    if remainder != 0:
        temp_start = temp[0:remainder]
        plain_text = chr(int(temp[0:remainder], 2))

    for i in range(remainder, len(temp), 8):
        #    print(chr(int((temp[i:i+8]), 2)))
        plain_text += chr(int((temp[i:i + 8]), 2))
        i += 8
    return plain_text


def base58_encode(string_input):
    """
    base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
    base58的编码思路是反复除以58取余数直至为0，base64的编码原理是64进制，2的6次方刚好等于64
    :param string_input: 输入待编码的字符
    :return: base58的编码值
    """
    base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    string = string_input
    string_binary = ''
    #   获取输入字符ascii码值的二进制码字符串，8个bit为一组
    for i in range(len(string)):
        string_binary = string_binary + str('{:0>8}'.format(bin(ord(string[i])).replace('0b', '')))
    string_decimal = int(string_binary, 2)
    string_58_list = []
    while True:
        string_58_list.insert(0, string_decimal % 58)
        string_decimal = string_decimal // 58
        if string_decimal == 0:
            break
    string_58 = ""
    for i in string_58_list:
        string_58 += base58[i]
    return string_58


print()

if __name__ == '__main__':
    # 兑换要花的b
    inputToken = "So11111111111111111111111111111111111111112"
    # 兑换目标币地址
    outputToken = "5zgTYTDK836G2Fc4ZLQp4rsyi78pAbuDr4qaQUE1pump"
    # 最小单位lamports， 100000000=0.1SOL
    amount = "100000000"
    # 发起交易钱包地址
    fromAddress = ""

    # 滑点 滑点，%之上的数值，比如10表示10%
    slippage = 1.0

    url = (f"https://gmgn.ai/defi/router/v1/sol/tx/get_swap_route?token_in_address={inputToken}&token_out_address="
           f"{outputToken}&in_amount={amount}&from_address={fromAddress}&slippage={slippage}")
    headers = {
        "authority": "gmgn.ai",
        "accept": "application/json, text/plain, */*'",
        "accept-language": "zh,zh-CN;q=0.9",
        "cache-control": "no-cache",
        "cookie": "_ga=GA1.1.1538430465.1713834683; _ga_0XM0LYXGC8=GS1.1.1714184467.2.1.1714184492.0.0.0",
        "pragma": "no-cache",
        "referer": "https://gmgn.ai",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                      "Safari/537.36",

    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print(response.text)

    swapTransaction = response.text[]

    post_url = "https://gmgn.ai/defi/router/v1/sol/tx/submit_signed_transaction"
    headers = {
        "content-type': 'application/json"
    }

    base58_decode(base58_encode('hongfei'))

    data = {'signed_tx':}
    requests.post(post_url, data={''}, headers=headers)
