import pytest
from appium import webdriver

from tests.lib.ui.search_page_object import SearchPageObject
from tests.lib.ui.article_page_object import ArticlePageObject
from tests.lib.ui.my_lists_page_object import MyListsPageObject
from tests.lib.ui.welcome_page_object import WelcomePageObject
from tests.lib.ui.navigation_ui import NavigationUI


appium_url = 'http://0.0.0.0:4723/wd/hub'


@pytest.fixture(autouse=True)
def driver():
    desired_caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone SE',
        'platformVersion': '12.4',
        'app': '/Users/admin/Desktop/python/python_appium_automation/apks/Wikipedia.app',
        'orientation': 'PORTRAIT'
    }

    driver = webdriver.Remote(appium_url, desired_caps)

    yield driver

    driver.quit()


@pytest.fixture
def search_page(driver):
    return SearchPageObject(driver)


@pytest.fixture
def article_page(driver):
    return ArticlePageObject(driver)


@pytest.fixture
def navigation_ui(driver):
    return NavigationUI(driver)


@pytest.fixture
def my_lists_page(driver):
    return MyListsPageObject(driver)


@pytest.fixture
def welcome_page(driver):
    return WelcomePageObject(driver)


