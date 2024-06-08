import inspect
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_baidu_search(driver):
    driver.get("https://www.baidu.com")
    try:
        search_element = driver.find_element(By.CLASS_NAME, 'xxxx')
        search_element.click()
    except NoSuchElementException:
        current_function = inspect.currentframe().f_code.co_name
        allure.attach(driver.get_screenshot_as_png(), f'{current_function}_element', allure.attachment_type.PNG)
