def test_get_started(welcome_page):
    welcome_page.wait_for_more_text()
    welcome_page.click_next_button()
    welcome_page.wait_for_new_way_to_explore_text()
    welcome_page.click_next_button()
    welcome_page.wait_for_add_or_edit_preferred_lang_text()
    welcome_page.click_next_button()
    welcome_page.wait_for_learn_more_about_data_collected_text()
    welcome_page.click_get_started_button()

