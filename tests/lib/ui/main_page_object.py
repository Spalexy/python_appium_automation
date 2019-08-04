
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPageObject:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def wait_for_element_present(self, element_path, error_message, timeout_seconds):
        wait = WebDriverWait(self.driver, timeout_seconds)
        return wait.until(ec.presence_of_element_located(element_path), error_message + "\n")

    def wait_for_element_not_present(self, element_path, error_message, timeout_seconds):
        wait = WebDriverWait(self.driver, timeout_seconds)
        return wait.until(ec.invisibility_of_element_located(element_path), error_message + "\n")

    def wait_for_element_and_click(self, element_path, error_message, timeout_seconds):
        element = self.wait_for_element_present(element_path, error_message, timeout_seconds)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, element_path, value, error_message, timeout_seconds):
        element = self.wait_for_element_present(element_path, error_message, timeout_seconds)
        element.send_keys(value)
        return element

    def wait_for_element_and_clear(self, element_path, error_message, timeout_seconds):
        input_element = self.wait_for_element_present(element_path, error_message, timeout_seconds)
        input_element.clear()
        return input_element

    def wait_for_elements(self, elements_path, error_message, timeout_seconds):
        wait = WebDriverWait(self.driver, timeout_seconds)
        return wait.until(ec.presence_of_all_elements_located(elements_path), error_message + "\n")

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        action = TouchAction(self)
        action \
            .press(x=start_x, y=start_y) \
            .wait(ms=duration) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self

    def swipe_element_to_left(self, element_path):
        element = self.wait_for_element_present(element_path, 'Cannot find element to swipe', 5)
        location = element.location
        size = element.size
        left_x = location.get('x')
        right_x = left_x + size.get('width')
        upper_y = location.get('y')
        lower_y = upper_y + size.get('height')
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self)
        action.press(x=right_x, y=middle_y)
        action.move_to(x=left_x, y=middle_y)
        action.release()
        action.perform()

    def swipe_up(self):
        window_size = self.driver.get_window_size()
        self.swipe(
            window_size['width'] * 0.5, window_size['height'] * 0.4,
            window_size['width'] * 0.5, window_size['height'] * 0.1,
        )

    def wait_for_element_by_id_and_check_text(self, wait_in_seconds, element_id, text):
        wait = WebDriverWait(self, wait_in_seconds)
        wait.until(ec.text_to_be_present_in_element((By.ID, element_id), text))

    def wait_for_element_by_xpath_is_present(self, wait_in_seconds, element_xpath):
        wait = WebDriverWait(self, wait_in_seconds)
        wait.until(ec.presence_of_element_located((By.XPATH, element_xpath)))

    def check_element_by_id_is_not_single(self, element_id):
        count = self.find_elements_by_id(element_id)
        assert len(count) > 1

    def clear_search_results(self, element_id):
        self.find_element_by_id(element_id).click()


