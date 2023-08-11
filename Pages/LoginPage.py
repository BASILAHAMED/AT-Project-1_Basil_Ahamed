from Pages.BasePage import BasePage
from Config.config import TestData, WebLocators


class LoginPage(BasePage) :
    # constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # this is used to get the page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # this is used to login to app
    def do_login(self, username, password):
        self.do_send_keys(WebLocators.USERNAME, username)
        self.do_send_keys(WebLocators.PASSWORD, password)
        self.do_click(WebLocators.LOGIN)
    
    # this is used to fetch text
    def get_element_value(self, locator):
        if self.is_visible(locator):
            return self.get_element_text(locator)
