import pytest
from Config.config import TestData, WebLocators
from Pages.LoginPage import LoginPage
from Tests.testBase import BaseTest


class TestLogin(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        header = self.loginPage.get_element_value(WebLocators.DASHBOARD)
        assert header == TestData.DASHBOARD_TEXT
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=TestData.USERNAME, password=TestData.PASSWORD))

    def test_invalid_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.INVALID_PASSWORD)
        text = self.loginPage.get_element_value(WebLocators.INVALID_LOGIN)
        assert text == TestData.INVALID_TEXT
        print("SUCCESS # ERROR LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=TestData.USERNAME, password=TestData.INVALID_PASSWORD))
