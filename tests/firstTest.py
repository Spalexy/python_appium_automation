import unittest
from appium import webdriver


class WikipediaTest(unittest.TestCase):
    "Class to run tests against the Wikipedia app"

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Honor 10',
            'platformVersion': '9',
            'app': '/users/admin/Desktop/python_appium_automation/apks/org.wikipedia.apk',
            'appActivity': '.main.MainActivity',
            'automationName': 'Appium'

        }

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        print('First test run')
        pass
