"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--profile-directory=Default')
options.add_argument('--headless')
url="https://news.yahoo.co.jp/"

try:
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        driver.refresh()

        # TOPファイルを確認
        for i in range(1,8,1):
            print(driver.find_element(By.XPATH,f"/html/body/div[1]/div/main/div[1]/div/section[1]/div/div/div/ul/li[{str(i)}]/a").text)

except Exception as e:
    print(str(e))