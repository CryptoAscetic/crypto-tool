## python处理时间

https://docs.python.org/zh-cn/3/library/datetime.html#strftime-and-strptime-behavior

## AI处理的核心逻辑

- 1.池子的大小必须大于300
- 2.必须有推特，如果三无产品不上（推特、官网、电报）
- 3.top的占比，30%能上
- 4.老鼠仓的占比高于30%直接不上
- 5.对比一下机器人看一下占比情况
- 6.对比一下分钟价格，差距太大不上
- 7.热度代币冲进去赚了就跑，留利润
- 8.pupm出来的，看那个进度大于5的可以关注
- 9.合约名字也可以割一波韭菜，看名字如果特殊的上完赚就跑

0 1 * * * sh /usr/local/nginx/script/nginx_log.sh
#*/60 * * * *  python /data/tool/crypto-tool/eth/hot-token.py
#*/1 * * * * python /data/tool/crypto-tool/sol/ai-kol-tokens.py
*/1 * * * * python /data/tool/crypto-tool/sol/ai-kol-le.py
#*/3 * * * * python /data/tool/crypto-tool/sol/ai-smart-token.py
*/2 * * * *  python /data/tool/crypto-tool/sol/smart-token.py
#*/6 * * * *  python /data/tool/crypto-tool/sol/create-token.py
#*/6 * * * *  python /data/tool/crypto-tool/sol/hot-token.py
#*/6 * * * *  python /data/tool/crypto-tool/sol/new-token.py

# 每分钟执行一次，将文本“123”写入到testFile文件中

*/1 * * * * echo 123 >> /usr/local/nginx/logs/testFile

-bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF8)
/bin/sh: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF8)
sudo localedef -i en_US -f UTF-8 en_US.UTF-8

## 1.检查合约

https://tokensniffer.com/token/eth/0x82021df5dc2cab797978cec423cec35a15925887

## 2.检查合约gopluslabs

curl 'https://api.gopluslabs.io/api/v1/token_security/1?contract_addresses=0x82021df5dc2cab797978cec423cec35a15925887' \

[//]: # (-H 'authority: api.gopluslabs.io' \)

[//]: # (-H 'accept: application/json, text/plain, */*' \)
-H 'accept-language: zh,zh-CN;q=0.9' \
-H 'cache-control: no-cache' \
-H 'origin: https://gopluslabs.io' \
-H 'pragma: no-cache' \
-H 'referer: https://gopluslabs.io/' \
-H 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "Linux"' \
-H 'sec-fetch-dest: empty' \
-H 'sec-fetch-mode: cors' \
-H 'sec-fetch-site: same-site' \
-H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
--compressed

## 3.api-store

https://ape.store/

curl 'https://gmgn.ai/defi/quotation/v1/tokens/top_holders/sol/ALW1DD65EtewCiRz65gUDvYYAqQWLwjo68XAnsR7pump?limit=20&cost=20&tag=rat_trader&orderby=amount_percentage&direction=desc' \
-H 'authority: gmgn.ai' \
-H 'accept: application/json, text/plain, */*' \
-H 'accept-language: zh,zh-CN;q=0.9' \
-H 'cache-control: no-cache' \
-H 'cookie: _ga=GA1.1.1538430465.1713834683;
cf_clearance=Sip.TP0Xjme.W62T0Z8lk0tFMNfDIMtlzqvI8ZQbmRk-1728605833-1.2.1.1-mixv6HPDXwkEQwEJDSX_RmlpEnUuSWgvzRmbLmXwyenhX1XJ3UrC0guPdiEBS1Sy55G3G9crI_H0n_j4ZgV0euD8RKuYl3NZ5cycFgeaXJo2KuxVZ0wRE_R8bNweEiPWr2m6OkeQBcmdix1K29DYZxNWoH6CEml2gvoZmZstCMksIqYKXFKyrawpK_G5BsKkTMsHgqpjkfaBNZdf4j6lo7fx_cNeM4zFg.v3K3BAmt.oBuRiU7EOGwgZui2A0hkWMSjDvU5Kl9yu9em0XlZ.xEeqI9gdfL9QIx_86c0o8Ns37wUXveKN0nR4iT9aNt7whmQ25HIZAAy5roAK6Gm8ezyGwmTAUwWsUHAIZOJIjczxGBUXH6kWA1RAGtacujWG; _
ga_0XM0LYXGC8=GS1.1.1728605831.98.1.1728606176.0.0.0; __
cf_bm=TcSHl3t72Oc22i7bYZbFFBBhvDBp3BHXqJuf39GgYUk-1728606180-1.0.1.1-fzQ4WpdyrbYxhZxd0oTC8XEa4TeENXahnnUdsICyVbtmMk8aAzk6tst0GglHVmTTM5RxrpJ8IrnKflDtNpNKLw' \
-H 'pragma: no-cache' \
-H 'referer: https://gmgn.ai/sol/token/pBbJV9S0_ALW1DD65EtewCiRz65gUDvYYAqQWLwjo68XAnsR7pump' \
-H 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
-H 'sec-ch-ua-mobile: ?1' \
-H 'sec-ch-ua-platform: "Android"' \
-H 'sec-fetch-dest: empty' \
-H 'sec-fetch-mode: cors' \
-H 'sec-fetch-site: same-origin' \
-H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/117.0.0.0 Mobile Safari/537.36' \
--compressed

## 代码快速转换 curl-pytho或者java

https://www.lddgo.net/convert/curl-to-code

## dbotx可以使用程序自动交易

https://dbotx.com/zh/docs/account-create?chain=ethereum

## tg语法

https://github.com/dingdangcats/Telegram-Markdown-Html-Deeplink-Guide

*粗体文本*
_斜体文本_
__下划线文本__
~~删除线文本~~
||剧透字符||
*粗体 _斜体 粗体 ~斜体 粗体 删除线 ||斜体 粗体 删除线 剧透||~ __下划线 斜体 粗体___ 粗体*
[叮当猫](http://www.example.com/)
[叮当猫](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)     #个性化表情
`等宽字体`
"```张晓丽
生日：1992-10-03 #多行等宽字体

```"
