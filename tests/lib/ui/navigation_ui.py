from selenium.webdriver.common.by import By

from .main_page_object import MainPageObject


class NavigationUI(MainPageObject):

    MY_LISTS_LINK = (By.XPATH, '//android.widget.FrameLayout[@content-desc=\'My lists\']')

    def click_my_lists(self):
        self.wait_for_element_and_click(self.MY_LISTS_LINK, 'Cannot find navigation button to My lists', 5)
