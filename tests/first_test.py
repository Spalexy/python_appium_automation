from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Honor 10',
        'platformVersion': '9',
        'app': '/users/admin/Desktop/python/python_appium_automation/apks/org.wikipedia.apk',
        'appActivity': '.main.MainActivity',
        'automationName': 'Appium'
    }

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    try:
        wait_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
        wait_for_element_by_id_and_check_text(driver, 10, 'org.wikipedia:id/search_src_text', 'Поиск')

    finally:
        driver.quit()


def wait_for_element_by_id_and_check_text(driver, wait_in_seconds, element_id, text):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.text_to_be_present_in_element((By.ID, element_id), text))


def wait_for_element_by_id_and_click(driver, element_id):
    driver.find_element_by_id(element_id).click()



