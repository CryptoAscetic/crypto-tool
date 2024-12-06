#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from uiautomation import WindowControl

# 绑定微信主窗口
wx = WindowControl(
    Name='微信',
    # searchDepth=1
)

# 切换窗口
wx.SwitchToThisWindow()
# 寻找会话控件绑定
hw = wx.ListControl(Name='会话')
# 通过pd读取数据
df = pd.read_csv('回复数据.csv', encoding='gb18030')

# 死循环接受消息
while True:
    # 从查找未读消息
    we = hw.TextControl(searchDepth=4)

    # 死循环维持，没有超时报错
    while not we.Exists(0):
        pass

    # 存在未读消息
    if we.Name:
        # 点击未读消息
        we.Click(simulateMove=False)

        # 读取最后一条消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
        # 判断关键字
        msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        # 数据筛选，移除空数据
        msg.dropna(axis=0, how='any', inplace=True)
        # 做成列表
        ar = np.array(msg).tolist()

        # 能够匹配到数据时
        if ar:
            # 将数据输入
            # 替换换行符号
            wx.SendKeys(ar[0].replace('{br}', '{Shift}{Enter}'), waitTime=0)
            # 发送消息
            wx.SendKeys('{Enter}', waitTime=0)

            # 通过消息匹配检索会话栏的联系人
            wx.TextControl(SubName=ar[0][:5]).RightClick()
        # 没有匹配到数据时
        else:
            wx.TextControl(SubName=last_msg[:5]).RightClick()

        # 匹配右击控件
        # ment = MenuControl(ClassName='CMenuWnd')
        # 点击右键控件中的不显示聊天
        # ment.TextControl(Name='不显示聊天').Click()
