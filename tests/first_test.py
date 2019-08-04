from tests.lib.ui.main_page_object import MainPageObject


def test_search(search_page):
    search_page.init_search_input()
    search_page.type_search_line('Python')
    search_page.wait_for_search_result('Family of nonvenomous snakes')


def test_search_field(driver, search_page):
    driver.orientation = 'LANDSCAPE'
    search_page.init_search_input()
    MainPageObject.wait_for_element_by_id_and_check_text(driver, 10, 'org.wikipedia:id/search_src_text', 'Search')


def test_articles_search(search_page):
    search_page.init_search_input()
    search_page.wait_for_cancel_button_to_appear()
    search_page.click_cancel_search()
    search_page.wait_for_cancel_button_to_disappear()


def test_word_in_search_results(search_page):
    search_page.init_search_input()
    search_page.type_search_line('Python')


def test_verify_each_search_result_contains_search_world(search_page):
    search_key_word = 'python'

    search_page.init_search_input()
    search_page.type_search_line(search_key_word)
    search_page.check_all_search_results_contains_word(search_key_word)


# ToDo: refactoring
def test_save_two_articles_remove_one(driver, search_page, article_page, navigation_ui, my_lists_page):
    first_search = 'Java'
    second_search = 'PyCharm'
    folder_name = 'Appium tests'

    search_page.init_search_input()
    search_page.type_search_line(first_search)
    search_page.click_by_article_with_substring(first_search)
    article_page.wait_for_title_element()
    article_page.add_article_to_my_list(folder_name)
    article_page.close_article()

    search_page.init_search_input()
    search_page.type_search_line(second_search)
    search_page.click_by_article_with_substring(second_search)
    article_page.wait_for_title_element()
    article_page.add_article_to_my_existing_list(folder_name)
    article_page.close_article()

    navigation_ui.click_my_lists()
    my_lists_page.open_folder_by_name(folder_name)
    my_lists_page.delete_article_by_name(first_search)
    my_lists_page.check_article_not_in_list_by_name(first_search)


def test_check_article_title_present(search_page, article_page):
    search_page.init_search_input()
    search_page.type_search_line('Python')
    search_page.click_by_article_with_substring('Family of nonvenomous snakes')
    article_title = article_page.get_article_title()

    assert 'Pythonidae' == article_title, 'We see unexpected title'


def test_swipe_article(search_page, article_page):
    search_page.init_search_input()
    search_page.type_search_line('Appium')
    search_page.click_by_article_with_substring('Appium')
    article_page.wait_for_title_element()
    article_page.swipe_to_footer()

