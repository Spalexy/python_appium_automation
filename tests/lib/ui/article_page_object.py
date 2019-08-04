
from selenium.webdriver.common.by import By

from .main_page_object import MainPageObject


class ArticlePageObject(MainPageObject):

    TITLE = (By.ID, 'org.wikipedia:id/view_page_title_text')
    FOOTER_ELEMENT = (By.XPATH, '//*[@text=\'View page in browser\'')
    OPTIONS_BUTTON = (By.XPATH, '//android.widget.ImageView[@content-desc=\'More options\']')
    OPTIONS_ADD_TO_MY_LIST_BUTTON = (By.XPATH, '//*[contains(@text, \'Add to reading list\')]')
    ADD_TO_MY_LIST_OVERLAY = (By.ID, 'org.wikipedia:id/onboarding_button')
    MY_LIST_NAME_INPUT = (By.ID, 'org.wikipedia:id/text_input')
    MY_LIST_OK_BUTTON = (By.XPATH, '//*[contains(@text, "OK")]')
    CLOSE_ARTICLE_BUTTON = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    EXISTING_LIST_BUTTON = '//*[@text=\'{SUBSTRING}\']'

    def get_result_search_element(self, substring):
        return self.EXISTING_LIST_BUTTON.replace('{SUBSTRING}', substring)

    def wait_for_title_element(self):
        return self.wait_for_element_present(self.TITLE, 'Cannot find article title on page', 15)

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return getattr(title_element, 'text')

    def swipe_to_footer(self):
        self.swipe_up_to_find_element(self.FOOTER_ELEMENT, 'Cannot find the end of article', 20)

    def add_article_to_my_list(self, folder_name):
        self.wait_for_element_and_click(self.OPTIONS_BUTTON, 'Cannot find the options button', 5)
        self.wait_for_element_and_click(self.OPTIONS_ADD_TO_MY_LIST_BUTTON,
                                        'Cannot find the option to add article to reading list', 5)
        self.wait_for_element_and_click(self.ADD_TO_MY_LIST_OVERLAY, 'Cannot find \'Got it\' tip overlay', 5)
        self.wait_for_element_and_click(self.MY_LIST_NAME_INPUT, 'Cannot find input to set name of articles folder', 5)
        self.wait_for_element_and_clear(self.MY_LIST_NAME_INPUT,
                                        'Cannot find input to set name of articles folder', 5)
        self.wait_for_element_and_send_keys(self.MY_LIST_NAME_INPUT, folder_name,
                                            'Cannot put text into articles folder input', 5)
        self.wait_for_element_and_click(self.MY_LIST_OK_BUTTON,
                                        'Cannot press OK button', 5)

    def add_article_to_my_existing_list(self, folder_name):
        existing_list_xpath = self.get_result_search_element(folder_name)
        self.wait_for_element_and_click(self.OPTIONS_BUTTON, 'Cannot find the options button', 5)
        self.wait_for_element_and_click(self.OPTIONS_ADD_TO_MY_LIST_BUTTON,
                                        'Cannot find the option to add article to reading list', 5)
        self.wait_for_element_and_click((By.XPATH, existing_list_xpath),
                                        'Cannot find existing reading list', 5)

    def close_article(self):
        self.wait_for_element_and_click(self.CLOSE_ARTICLE_BUTTON, 'Cannot press close button', 5)



