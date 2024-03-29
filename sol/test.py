import datetime

import pytz

# 创建一个 datetime 对象，表示当前时间
now = datetime.datetime.now()

# 创建一个 pytz 时区对象，表示中国时区
china_tz = pytz.timezone('Asia/Shanghai')

# 使用时区对象将 datetime 对象转换为中国时区时间
china_time = china_tz.localize(now)

# 将中国时区时间转换为纽约时区时间
new_york_tz = pytz.timezone('America/New_York')
new_york_time = china_time.astimezone(new_york_tz)

# 输出中国时区时间和纽约时区时间
print('中国时间：', str(china_time))
print('纽约时间：', new_york_time)
