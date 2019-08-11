from selenium.webdriver.common.by import By

from .main_page_object import MainPageObject


class WelcomePageObject(MainPageObject):

    STEP_LEARN_MORE_LINK = (By.ID, 'Learn more about Wikipedia')
    STEP_NEW_WAYS_TO_EXPLORE_LINK = (By.ID, 'New ways to explore')
    STEP_ADD_OR_EDIT_PREFERRED_LANG_LINK = (By.ID, 'Add or edit preferred languages')
    STEP_LEARN_MORE_ABOUT_DATA_COLLECTED_LINK = (By.ID, 'Learn more about data collected')
    NEXT_LINK = (By.ID, 'Next')
    GET_STARTED_BUTTON = (By.ID, 'Get started')

    def wait_for_more_text(self):
        self.wait_for_element_present(self.STEP_LEARN_MORE_LINK, 'Error', 5)

    def click_next_button(self):
        self.wait_for_element_and_click(self.NEXT_LINK, 'Error', 5)

    def wait_for_new_way_to_explore_text(self):
        self.wait_for_element_present(self.STEP_NEW_WAYS_TO_EXPLORE_LINK, 'Error', 5)

    def wait_for_add_or_edit_preferred_lang_text(self):
        self.wait_for_element_present(self.STEP_ADD_OR_EDIT_PREFERRED_LANG_LINK, 'Error', 5)

    def wait_for_learn_more_about_data_collected_text(self):
        self.wait_for_element_present(self.STEP_LEARN_MORE_ABOUT_DATA_COLLECTED_LINK, 'Error', 5)

    def click_get_started_button(self):
        self.wait_for_element_and_click(self.GET_STARTED_BUTTON, 'Error', 5)

