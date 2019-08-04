from selenium.webdriver.common.by import By

from .main_page_object import MainPageObject


class MyListsPageObject(MainPageObject):

    FOLDER_XPATH_TPL = '// *[@text=\'{FOLDER_NAME}\']'
    ARTICLE_XPATH_TPL = '//*[@text=\'{ARTICLE_NAME}\']'

    def get_folder_xpath_by_name(self, folder_name):
        return self.FOLDER_XPATH_TPL.replace('{FOLDER_NAME}', folder_name)

    def get_article_xpath_by_name(self, article_name):
        return self.ARTICLE_XPATH_TPL.replace('{ARTICLE_NAME}', article_name)

    def open_folder_by_name(self, folder_name):
        folder_name_xpath = self.get_folder_xpath_by_name(folder_name)
        self.wait_for_element_and_click((By.XPATH, folder_name_xpath),
                                        'Cannot find folder by name', 5)

    def delete_article_by_name(self, article_name):
        element_xpath = self.get_article_xpath_by_name(article_name)
        self.swipe_element_to_left((By.XPATH, element_xpath))

    def check_article_not_in_list_by_name(self, article_name):
        element_xpath = self.get_article_xpath_by_name(article_name)
        self.wait_for_element_not_present((By.XPATH, element_xpath), 'Article is still present', 5)

