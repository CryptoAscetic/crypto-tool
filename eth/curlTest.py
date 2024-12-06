from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置 Chrome 浏览器选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 如果不需要显示浏览器窗口，可以启用无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# 设置请求头
chrome_options.add_argument(
    'accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
chrome_options.add_argument('accept-language=zh,zh-CN;q=0.9')
chrome_options.add_argument('cache-control=no-cache')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36')

# 创建 Selenium 浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开目标 URL
url = 'https://gmgn.ai/defi/quotation/v1/wallet_activity/sol?type=buy&type=sell&wallet=82jXFTVu2XwCnG63pGqdf1yAfGMLbmXNzmBE5nupx6YF&limit=10&cost=10'

# 打开页面
driver.get(url)

# 获取页面内容
page_content = driver.page_source

# 输出内容
print(page_content)

# 关闭浏览器
driver.quit()
