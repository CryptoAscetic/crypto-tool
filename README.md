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