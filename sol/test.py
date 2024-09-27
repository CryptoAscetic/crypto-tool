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
    url = "https://gmgn.ai/api/v1/token_link/sol/GewCPXyZncLyFCaU5rPvN6joVJks78qUFjCA6b7Spump"
    headers = {
        "Cookie": "_ga=GA1.1.1538430465.1713834683; __cf_bm=Lh0riuOmzSvvIgLI2jexxCTfgnlXNJSUqRIFGiqFB3k-1727420862-1"
                  ".0.1.1-Xj126WHC2RvlkqU4yJT1Uy.oWHsOo00rF_bLvpRsbGezDk.h8GFVnJKqmD68v1gJTm72xB9Zy2NOLliLUzaxKg; "
                  "cf_clearance=RiadSjB_4UmvdpjU7UpYwxfQ4BhLDiX3IrL5aWeL0aw-1727420865-1.2.1.1"
                  "-n2ZxvMRXmbByQ1H2Xkcsvb5doN3VvdW1062rVts589o7A7YfJe0ijQpgkkoqhYkKz0T5Ti4wzxuSuLSxVItinKSIo2124qeyDhwAGUrSlbnk9ZtjEgINepFGzGKZLbIMfY1mzCj738jfnOi3AuyIOXtMlGu9XY.2IEAOCOSCquI2_0pkbRkzkX0kZN4VIIxfOAbsyiFhFHnpQZcu3Fm4uT3amOinNFbLhfuKplSdb2Uuf.Qw19fZp8vpmwLj94bIrYuOn8Bc4vWJe5qBx9oU.WLM1xw1bvsknmotkYsovQ4Vy3Q0hodkcLj.xdJZ2m3MEe8anbowjnLDUiaeRzBFMOS_m7fXem8TwPY0n8Y1qAN6JO4IPBuYrVPzRQ3R3j_l; _ga_0XM0LYXGC8=GS1.1.1727420863.81.1.1727420905.0.0.0",
        "User-Agent": "PostmanRuntime/7.36.3"
    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print(response.text)

