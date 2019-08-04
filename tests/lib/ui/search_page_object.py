from .main_page_object import MainPageObject
from selenium.webdriver.common.by import By


class SearchPageObject(MainPageObject):

    SEARCH_INIT_ELEMENT = (By.ID, 'org.wikipedia:id/search_container')
    SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_CANCEL_BUTTON = (By.ID, 'org.wikipedia:id/search_close_btn')
    SEARCH_RESULT_XPATH = '//*[@resource-id=\'org.wikipedia:id/page_list_item_container\']//*[@text=\'{SUBSTRING}\']'
    SEARCH_RESULTS = (By.ID, 'org.wikipedia:id/page_list_item_title')
    SEARCH_RESULT_BY_TITLE_AND_DESCRIPTION_TPL = ('//android.widget.TextView[@text=\'{TITLE}\']'
                                                  '/following-sibling::android.widget.'
                                                  'TextView[@text=\'{DESCRIPTION}\']')

    def get_result_search_element(self, substring):
        return self.SEARCH_RESULT_XPATH.replace('{SUBSTRING}', substring)

    def get_search_result_by_title_and_description(self, title, description):
        return self.SEARCH_RESULT_BY_TITLE_AND_DESCRIPTION_TPL\
            .replace('{TITLE}', title)\
            .replace('{DESCRIPTION}', description)

    def init_search_input(self):
        self.wait_for_element_and_click(self.SEARCH_INIT_ELEMENT, 'Cannot find and click search container', 5)
        self.wait_for_element_present(self.SEARCH_INIT_ELEMENT, 'Cannot find search input after clicking search container', 5)

    def type_search_line(self, search_line):
        self.wait_for_element_and_send_keys(self.SEARCH_FIELD, search_line, 'Cannot find and type into search container', 5)

    def wait_for_search_result(self, substring):
        search_result_xpath = self.get_result_search_element(substring)
        self.wait_for_element_present((By.XPATH, search_result_xpath), 'Cannot find search result', 5)

    def wait_for_cancel_button_to_appear(self):
        self.wait_for_element_present(self.SEARCH_CANCEL_BUTTON, 'Cannot find search cancel button', 5)

    def wait_for_cancel_button_to_disappear(self):
        self.wait_for_element_not_present(self.SEARCH_CANCEL_BUTTON, 'Search cancel button is still present', 5)

    def click_cancel_search(self):
        self.wait_for_element_and_click(self.SEARCH_CANCEL_BUTTON, 'Cannot find and click search cancel button', 5)

    def click_by_article_with_substring(self, substring):
        search_result_xpath = self.get_result_search_element(substring)
        self.wait_for_element_and_click((By.XPATH, search_result_xpath), 'Cannot find and click search result with substring', 5)

    def clear_search_input(self):
        self.wait_for_element_and_clear(self.SEARCH_FIELD,
                                        'Cannot find and clear search container', 5)

    def check_all_search_results_contains_word(self, key_word):
        search_results = self.wait_for_elements(self.SEARCH_RESULTS, 'Cannot find search results', 5)
        for result in search_results:
            result_title = result.get_attribute('text')
            assert key_word in result_title.lower(), 'Key word was not found in the title of search results'

    def wait_for_element_by_title_and_description(self, title, description):
        search_result_xpath = self.get_search_result_by_title_and_description(title, description)
        self.wait_for_element_present((By.XPATH, search_result_xpath),
                                      'Cannot find result with title and description: ' + title + ', ' + description, 5)

