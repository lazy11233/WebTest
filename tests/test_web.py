import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# def test_bilibili():
#     driver = webdriver.Chrome()
#     try:
#         driver.get("https://www.bilibili.com")
#         # 1. 找到输入框
#         search_box = driver.find_element(By.CLASS_NAME, "nav-search-input")
#         search_box.send_keys("疯狂滴小黑")
#         search_box.send_keys(Keys.ENTER)
#         # 等待几秒钟以便看到结果
#         driver.implicitly_wait(5)
#         # 关闭driver
#         driver.quit()
#     finally:
#         driver.quit()
#
#
# test_bilibili()


def test_google_search_fail(driver):
    driver.get("https://www.baidu.com")
    # search_element = driver.find_element(By.CLASS_NAME, 'xxxx')
    assert False
