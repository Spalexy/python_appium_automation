import pytest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Honor 10',
        'platformVersion': '9',
        'app': '/users/admin/Desktop/python/python_appium_automation/apks/org.wikipedia.apk',
        'appActivity': '.main.MainActivity',
        'automationName': 'Appium'
    }

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    yield driver

    driver.quit()


def test_search_field(driver):
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_check_text(driver, 10, 'org.wikipedia:id/search_src_text', 'Поиск')


def test_articles_search(driver):
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_send_keys(driver, 5, 'org.wikipedia:id/search_container', 'Python')
    check_element_by_id_is_not_single(driver, 'org.wikipedia:id/page_list_item_title')
    clear_search_results(driver, 'org.wikipedia:id/search_close_btn')
    wait_for_element_by_id(driver, 5, 'org.wikipedia:id/search_empty_message')


def wait_for_element_by_id(driver, wait_in_seconds, element_id):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.ID, element_id)))


def wait_for_element_by_id_and_check_text(driver, wait_in_seconds, element_id, text):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.text_to_be_present_in_element((By.ID, element_id), text))


def find_for_element_by_id_and_click(driver, element_id):
    driver.find_element_by_id(element_id).click()


def wait_for_element_by_id_and_send_keys(driver, wait_in_seconds, element_id, text):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.ID, element_id)))
    input_element = driver.find_element_by_id(element_id)
    input_element.send_keys(text)


def check_element_by_id_is_not_single(driver, element_id):
    count = driver.find_elements_by_id(element_id)
    assert len(count) > 1


def clear_search_results(driver, element_id):
    driver.find_element_by_id(element_id).click()


