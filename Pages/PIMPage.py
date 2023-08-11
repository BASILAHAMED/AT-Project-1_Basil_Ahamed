from Pages.BasePage import BasePage
from Config.config import TestData, WebLocators
from selenium.webdriver.common.keys import Keys


class PIMPage1(BasePage):
    # constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    # this is used to fill first name and last name
    def fill_name(self, firstname, lastname):
        self.do_send_keys(WebLocators.EMPLOYEE_FIRSTNAME, firstname)
        self.do_send_keys(WebLocators.EMPLOYEE_LASTNAME, lastname)

    # to get element and send keys to select and delete default text
    def clear_default(self, by_locator):
        self.do_send_keys(by_locator, (Keys.CONTROL, "a"))
        self.do_send_keys(by_locator, Keys.DELETE)
    
        
