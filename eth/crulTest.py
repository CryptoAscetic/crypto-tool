import subprocess

# 定义URL和自定义头信息
url = "https://gmgn.ai/defi/quotation/v1/wallet_activity/sol?type=buy&type=sell&wallet=82jXFTVu2XwCnG63pGqdf1yAfGMLbmXNzmBE5nupx6YF&limit=10&cost=10"
headers = {
    "authority": "gmgn.ai",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh,zh-CN;q=0.9",
    "cache-control": "no-cache",
    "cookie": "_ga=GA1.1.1538430465.1713834683; cf_clearance=vdi2icIYeA0pR.pzS47xMbAbBMfnPE5H9_2vIlkFlo4-1728606314-1.2.1.1-eHnu90X7ra2SYI1jS9BhKhZyeTR7YV61_pXpDnCvGbI6SM7.cFMvfSqhC6CIVaXe3UTgO_zdJMtXAi8IaHGy97qOHVnjUuiIRPDXk8nUgUQA9IfrPQVHeOp1K93JwH_waB_YyshoRsJMPpI7eMlNAKE0PbCjfQJ2NfH6vwQyMt9yMHSVBrHw9IEpDuFUMTvT2iq4V5DWqFcHV2vkOV6PXl8tr5i3EBpz2AYHEieSMPKbw5iuyfocP7tLKsBv7xE.hnociI95qWLE4UFDBpaybaAj3vDy7rwt9r4WH_ZoqVfQwNN7B5oKbvq9AKwqVjV7xrKKYmQlvHiQjTrpXy5GH21hiSyHJ_JHSgiUTMCTTXU5DqC2Wx.wIii5_I0bruwjAZtc.lC8I5fkEEERpXsiLk6FjtqDi4BBK1ZsjtI.XPc; _ga_0XM0LYXGC8=GS1.1.1728605831.98.1.1728606400.0.0.0; __cf_bm=OyAVK8mKtlAEmMd5vibrgKHt5VKZWK5wLqRQ1sYl0lA-1728606437-1.0.1.1-FeZE3EpqLQa7Dcrwdg6oJfzCK36ojTfb3GLSMtsIgFxUQde2sBscJHv3SGYsH6h5RNIpTjyhTLI2RlntGy5rZQ",
    "pragma": "no-cache",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                  "Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-platform": "Android",

}

# 构造curl命令
curl_command = ["curl", "-s", url]

# 添加头信息到命令中
for header, value in headers.items():
    curl_command.extend(["-H", f"{header}: {value}"])

try:
    # 调用curl命令
    result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
    # 输出结果
    print("Response:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")
