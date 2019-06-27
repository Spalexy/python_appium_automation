import pytest

from appium import webdriver


@pytest.fixture()
def driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Honor 10',
        'platformVersion': '9',
        'app': '/users/admin/Desktop/python_appium_automation/apks/org.wikipedia.apk',
        'appActivity': '.main.MainActivity',
        'automationName': 'Appium'
    }

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    yield driver

    driver.close_app()
    driver.quit()


def test():
    print('First test run')
    pass
