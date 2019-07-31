import pytest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture(autouse=True)
def driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Honor 10',
        'platformVersion': '9',
        'app': '/users/admin/Desktop/python/python_appium_automation/apks/org.wikipedia.apk',
        'appActivity': '.main.MainActivity',
        'automationName': 'Appium',
        'orientation': 'PORTRAIT'
    }

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    yield driver

    driver.quit()


def test_search_field(driver):
    driver.orientation = 'LANDSCAPE'
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_check_text(driver, 10, 'org.wikipedia:id/search_src_text', 'Поиск')


def test_articles_search(driver):
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_send_keys(driver, 5, 'org.wikipedia:id/search_container', 'Python')
    check_element_by_id_is_not_single(driver, 'org.wikipedia:id/page_list_item_title')
    clear_search_results(driver, 'org.wikipedia:id/search_close_btn')
    wait_for_element_by_id(driver, 5, 'org.wikipedia:id/search_empty_message')


def test_word_in_search_results(driver):
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_send_keys(driver, 5, 'org.wikipedia:id/search_container', 'Python')


def test_verify_each_search_result_contains_search_world(driver):
    search_key_word = 'python'
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')
    wait_for_element_by_id_and_send_keys(driver, 5, 'org.wikipedia:id/search_container', search_key_word)

    search_results = driver.find_elements_by_id('org.wikipedia:id/page_list_item_title')
    for result in search_results:
        result_title = result.get_attribute('text')
        assert search_key_word in result_title.lower(), 'Key word was not found in the title of search results'


def test_save_two_articles_remove_one(driver):
    first_search = 'Python'
    second_search = 'PyCharm'
    folder_name = 'Appium tests'

    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')

    wait_for_element_by_id_and_send_keys(driver, 5,
                                         'org.wikipedia:id/search_container',
                                         first_search)

    wait_for_element_by_xpath_and_click(driver, 5,
                                        "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@text='"
                                        + first_search + "']")

    wait_for_element_by_id(driver, 5,
                           'org.wikipedia:id/view_page_title_text')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//android.widget.ImageView[@content-desc="More options"]')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//*[contains(@text, "Add to reading list")]')

    find_for_element_by_id_and_click(driver,
                                     'org.wikipedia:id/onboarding_button')

    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/text_input')

    wait_for_element_by_id_and_clear(driver, 5,
                                     'org.wikipedia:id/text_input')

    wait_for_element_by_id_and_send_keys(driver, 5,
                                         'org.wikipedia:id/text_input',
                                         folder_name)

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//*[contains(@text, "OK")]')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//android.widget.ImageButton[@content-desc="Navigate up"]')

    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')

    wait_for_element_by_id_and_clear(driver, 1,
                                     'org.wikipedia:id/search_container')

    wait_for_element_by_id_and_send_keys(driver, 5,
                                         'org.wikipedia:id/search_container',
                                         second_search)

    wait_for_element_by_xpath_and_click(driver, 5,
                                        "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@text='"
                                        + second_search + "']")

    wait_for_element_by_id(driver, 5,
                           'org.wikipedia:id/view_page_title_text')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//android.widget.ImageView[@content-desc="More options"]')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//*[contains(@text, "Add to reading list")]')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '// *[ @ text = "' + folder_name + '"]')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//android.widget.ImageButton[@content-desc=\'Navigate up\']')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//android.widget.FrameLayout[@content-desc=\'My lists\']')

    wait_for_element_by_xpath_and_click(driver, 5,
                                        '//*[@resource-id=\'org.wikipedia:id/reading_list_list\']//*[@text=\'' + folder_name + '\']')

    swipe_element_to_left(driver,
                          '//*[@text=\'' + first_search + '\']')

    wait_for_element_not_present(driver, 5,
                                 (By.XPATH, '//*[@text=\'' + first_search + '\']\')'))


def test_check_article_title_present(driver):
    search = 'Python'
    find_for_element_by_id_and_click(driver, 'org.wikipedia:id/search_container')

    wait_for_element_by_id_and_send_keys(driver, 5,
                                         'org.wikipedia:id/search_container',
                                         search)

    wait_for_element_by_xpath_and_click(driver, 5,
                                        "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@text='"
                                        + search + "']")

    assert_element_present_by_id(driver, 'org.wikipedia:id/view_page_title_text')


def assert_element_present_by_id(driver, element_id):
    elements = driver.find_elements_by_id(element_id)
    elements_size = len(elements)
    assert elements_size > 0


def swipe_element_to_left(driver, element_xpath):
    element = driver.find_element_by_xpath(element_xpath)
    location = element.location
    size = element.size
    left_x = location.get('x')
    right_x = left_x + size.get('width')
    upper_y = location.get('y')
    lower_y = upper_y + size.get('height')
    middle_y = (upper_y + lower_y) / 2
    action = TouchAction(driver)
    action.press(x=right_x, y=middle_y)
    action.move_to(x=left_x, y=middle_y)
    action.release()
    action.perform()


def wait_for_element_by_id(driver, wait_in_seconds, element_id):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.ID, element_id)))


def wait_for_element_by_id_and_check_text(driver, wait_in_seconds, element_id, text):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.text_to_be_present_in_element((By.ID, element_id), text))


def find_for_element_by_id_and_click(driver, element_id):
    driver.find_element_by_id(element_id).click()


def wait_for_element_by_id_and_clear(driver, wait_in_seconds, element_id):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.ID, element_id)))
    input_element = driver.find_element_by_id(element_id)
    input_element.clear()


def wait_for_element_by_id_and_send_keys(driver, wait_in_seconds, element_id, text):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.ID, element_id)))
    input_element = driver.find_element_by_id(element_id)
    input_element.send_keys(text)


def wait_for_element_by_xpath_is_present(driver, wait_in_seconds, element_xpath):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))


def wait_for_element_by_xpath_and_click(driver, wait_in_seconds, element_xpath):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    element = driver.find_element_by_xpath(element_xpath)
    element.click()


def wait_for_element_not_present(driver, wait_in_seconds, element_locator):
    wait = WebDriverWait(driver, wait_in_seconds)
    wait.until(EC.invisibility_of_element_located(element_locator))


def check_element_by_id_is_not_single(driver, element_id):
    count = driver.find_elements_by_id(element_id)
    assert len(count) > 1


def clear_search_results(driver, element_id):
    driver.find_element_by_id(element_id).click()




