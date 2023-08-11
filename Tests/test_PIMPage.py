import pytest
from Config.config import TestData, WebLocators
from Pages.LoginPage import LoginPage
from Pages.PIMPage import PIMPage1
from Tests.testBase import BaseTest


class TestLogin(BaseTest):
    def test_add_employee(self):
        # create instances of LoginPage and PIMPage1
        self.loginPage = LoginPage(self.driver)
        self.pimpage = PIMPage1(self.driver)

        # login to application
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        # click PIM module
        self.loginPage.do_click(WebLocators.PIM_MODULE)

        # click add button
        self.loginPage.do_click(WebLocators.ADD_BUTTON)

        # fill the personal details
        self.pimpage.fill_name(TestData.FIRST_NAME, TestData.LAST_NAME)
        # click save button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # editing the employee information (Personal details)
        self.pimpage.clear_default(WebLocators.EMPLOYEE1_ID)
        # change employee id
        self.pimpage.do_send_keys(WebLocators.EMPLOYEE1_ID, TestData.EMPLOYEE1_ID_NO)

        # add all personal details
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_OTHER_ID, TestData.EMPLOYEE_OTHER_ID_NO)
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_DRIVER_LICENSE_NUMBER, TestData.LICENSE_NUMBER)
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_LICENSE_EXPIRY_DATE, TestData.LICENSE_EXPIRY_DATE_NO)
        self.loginPage.do_click(WebLocators.EMPLOYEE_NATIONALITY)
        self.loginPage.do_click(WebLocators.INDIAN_NATIONALITY)
        self.loginPage.do_click(WebLocators.EMPLOYEE_MARITAL_STATUS)
        self.loginPage.do_click(WebLocators.SINGLE_MARITAL_STATUS)
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_DOB, TestData.EMPLOYEE_DOB_NO)
        self.loginPage.do_click(WebLocators.EMPLOYEE_GENDER)

        # click save button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # assert new employee added successfully
        employee_name = self.loginPage.get_element_value(WebLocators.USER_GENERATED)
        assert employee_name == TestData.EMPLOYEE_NAME
        print("SUCCESS # EMPLOYEE {employee_name} ADDED".format(
        employee_name = TestData.EMPLOYEE_NAME.upper()))

    def test_edit_employee(self):
        # create instances of LoginPage and PIMPage1
        self.loginPage = LoginPage(self.driver)
        self.pimpage = PIMPage1(self.driver)

        # login to application
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        # click PIM module
        self.loginPage.do_click(WebLocators.PIM_MODULE)

        # search existing employee added earlier ("Ajith Kumar")
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_SEARCH, TestData.EMPLOYEE_NAME)

        # click search button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # click edit employee button
        self.loginPage.do_click(WebLocators.EDIT_BUTTON)

        # editing the employee information (Personal details)
        self.pimpage.clear_default(WebLocators.EMPLOYEE1_ID)
        # change employee id
        self.pimpage.do_send_keys(WebLocators.EMPLOYEE1_ID, TestData.UPDATED_EMPLOYEE_ID_NO)

        self.pimpage.clear_default(WebLocators.EMPLOYEE_OTHER_ID)
        # change employee id
        self.pimpage.do_send_keys(WebLocators.EMPLOYEE_OTHER_ID, TestData.EMPLOYEE_OTHER_ID_NO)

        self.pimpage.clear_default(WebLocators.EMPLOYEE_DRIVER_LICENSE_NUMBER)
        # change employee id
        self.pimpage.do_send_keys(WebLocators.EMPLOYEE_DRIVER_LICENSE_NUMBER, TestData.LICENSE_NUMBER)

        self.pimpage.clear_default(WebLocators.EMPLOYEE_LICENSE_EXPIRY_DATE)
        # change employee id
        self.pimpage.do_send_keys(WebLocators.EMPLOYEE_LICENSE_EXPIRY_DATE, TestData.LICENSE_EXPIRY_DATE_NO)

        # click save button
        self.loginPage.do_click(WebLocators.SAVE1_BUTTON)

        # verifying employee details edited or not
        # click employee list button
        self.loginPage.do_click(WebLocators.LIST_BUTTON)

        # search existing employee edited now ("Ajith Kumar")
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_SEARCH, TestData.EMPLOYEE_NAME)

        # click search button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # assert employee id equals to edited employee id
        employee_no = self.loginPage.get_element_value(WebLocators.EDITED_ID)
        assert employee_no == TestData.UPDATED_EMPLOYEE_ID_NO
        print("SUCCESS # EMPLOYEE {employee_name} DETAILS EDITED".format(
        employee_name = TestData.EMPLOYEE_NAME.upper()))


    def test_delete_employee(self):
        # create instances of LoginPage and PIMPage1
        self.loginPage = LoginPage(self.driver)
        self.pimpage = PIMPage1(self.driver)

        # login to application
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        # click PIM module
        self.loginPage.do_click(WebLocators.PIM_MODULE)

        # search existing employee edited now ("Ajith Kumar")
        self.loginPage.do_send_keys(WebLocators.EMPLOYEE_SEARCH, TestData.EMPLOYEE_NAME)

        # click search button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # wait until employee selected
        flag = self.loginPage.text_present(WebLocators.ONE_RECORD_FOUND, TestData.TEXT)
        assert flag

        # click delete employee button
        self.loginPage.do_click(WebLocators.DELETE_BUTTON)

        # click delete confirmation alert
        self.loginPage.do_click(WebLocators.DELETE_ALERT)

        # verify deletion by again searching employee present or not
        # click search button
        self.loginPage.do_click(WebLocators.SAVE_BUTTON)

        # print employee deleted status
        # if no records found for that employee, then employee deleted
        no_records = self.loginPage.get_element_value(WebLocators.CONFIRM_NO_RECORDS)
        assert no_records == TestData.NO_RECORDS_FOUND
        print("SUCCESS # EMPLOYEE {employee_name} DETAILS DELETED".format(
        employee_name = TestData.EMPLOYEE_NAME.upper()))




