"""


[使用模块]: requests >>> pip install requests   <第三方模块>
           selenium >>> pip install selenium   <第三方模块>
           parsel >>> pip install parsel       <第三方模块>
           time                                <内置模块>


"""

# 导入时间模块
import time

# 数据解析模块
import parsel
# driver.find_element_by_css_selector() 4 一定会报错 弃用 3
# 导入数据请求模块
import requests
# 导入浏览器对象
from selenium import webdriver
# 导入元素定位功能
from selenium.webdriver.common.by import By

# 实例化一个浏览器对象
driver = webdriver.Chrome()

# 打开浏览器的窗口
driver.get('https://www.jsyks.com/kmy-mnks')
# 强制等待
time.sleep(2)
# 最大化浏览器的窗口
driver.maximize_window()
# 隐式等待  智能
driver.implicitly_wait(10)

# elements 返回的是一个列表对象
lis = driver.find_elements(By.CSS_SELECTOR, '.Content>li')
# print(len(lis))
# print(lis)
for li in lis:
    time.sleep(0.2)  # 优先考虑使用随机数
    rid = li.get_attribute('c')
    # print(rid)
    url = f'https://tiba.jsyks.com/Post/{rid}.htm'
    # 获取到响应体对象的文本数据
    response = requests.get(url=url).text
    # 转对象
    selector = parsel.Selector(response)
    answer = selector.css('#question u::text').get()
    # print(answer)
    # 重新赋值
    if answer == '对':
        answer = '正确'
    elif answer == '错':
        answer = '错误'
    # else:  不确定的情况
    # print(answer)
    bs = li.find_elements(By.CSS_SELECTOR, 'B')
    for b in bs:
        # 获取选项的内容
        choose = b.text
        #     print('题目的选项是', choose)
        # print('正确答案是', answer)
        # 可能错题
        # if answer in choose:
        #     # 正确答案的点击操作
        #     b.click()
        if len(choose) > 2:
            choose = choose[0]
        if answer == choose:
            b.click()

# 提交试卷
driver.find_element(By.CSS_SELECTOR, '.btnJJ').click()

# 添加阻塞
input()

# 关闭浏览器
driver.quit()
