import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import pim_data
import pytest


class TestLogin:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # login to orangeHRM webpage
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_username).send_keys(pim_data.LoginData.username)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_password).send_keys(pim_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_login).click()
        yield
        self.driver.close()
    
    def test_pim1(self, launch_driver):
        # click PIM module
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_module).click()

        # click add button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_add_button).click()

        # fill the personal details
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_firstname).send_keys(pim_data.PersonalDetails.first_name)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_lastname).send_keys(pim_data.PersonalDetails.last_name)

        # clear default employee id and adding new employee id
        send_employee_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_id)
        send_employee_id.send_keys(Keys.CONTROL, "a")  # <--- Using ctrl+A key combination to delete default values --->
        send_employee_id.send_keys(Keys.DELETE)
        send_employee_id.send_keys(pim_data.PersonalDetails.employee_id)

        # click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # editing the employee information (Personal details)
        send_employee1_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee1_id)
        send_employee1_id.send_keys(Keys.CONTROL, "a")
        send_employee1_id.send_keys(Keys.DELETE)
        send_employee1_id.send_keys(pim_data.PersonalDetails.employee1_id)

        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_other_id).send_keys(
            pim_data.PersonalDetails.employee_other_id)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_driver_license_number).send_keys(
            pim_data.PersonalDetails.license_number)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_license_expiry_date).send_keys(
            pim_data.PersonalDetails.license_expiry_date)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_nationality).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_indian_nationality).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_marital_status).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_single_marital_status).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_dob).send_keys(
            pim_data.PersonalDetails.employee_dob)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_gender).click()

        # click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save1_button).click()

        # assert new employee added successfully
        name = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_user_generated).text
        assert name == "Ajith Kumar"
        print("SUCCESS # EMPLOYEE \"{first_name} {last_name}\" ADDED".format(
            first_name=pim_data.PersonalDetails.first_name.upper(),
            last_name=pim_data.PersonalDetails.last_name.upper()))

    def test_pim2(self, launch_driver):
        # click PIM module
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_module).click()

        # search existing employee added earlier ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # click edit employee button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_edit_button).click()

        # editing the employee information (Personal details)
        send_updated_employee_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee1_id)
        send_updated_employee_id.send_keys(Keys.CONTROL, "a")  # <--- Using ctrl+A key combination to delete default values --->
        send_updated_employee_id.send_keys(Keys.DELETE)
        send_updated_employee_id.send_keys(pim_data.PersonalDetails.updated_employee_id)

        send_employee_other_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_other_id)
        send_employee_other_id.send_keys(Keys.CONTROL, "a")
        send_employee_other_id.send_keys(Keys.DELETE)
        send_employee_other_id.send_keys(pim_data.PersonalDetails.updated_employee_other_id)

        send_employee_driver_license_number = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_driver_license_number)
        send_employee_driver_license_number.send_keys(Keys.CONTROL, "a")
        send_employee_driver_license_number.send_keys(Keys.DELETE)
        send_employee_driver_license_number.send_keys(pim_data.PersonalDetails.updated_license_number)

        send_employee_license_expiry_date = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_license_expiry_date)
        send_employee_license_expiry_date.send_keys(Keys.CONTROL, "a")
        send_employee_license_expiry_date.send_keys(Keys.DELETE)
        send_employee_license_expiry_date.send_keys(pim_data.PersonalDetails.updated_license_expiry_date)

        # click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save1_button).click()

        # verifying employee details edited or not
        # click employee list button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_list_button).click()

        # search existing employee edited now ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # assert employee id equals to edited employee id
        fetch = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_edited_id).text
        assert fetch == pim_data.PersonalDetails.updated_employee_id
        print("SUCCESS # EMPLOYEE \"{first_name} {last_name}\" DETAILS EDITED".format(
            first_name=pim_data.PersonalDetails.first_name.upper(),
            last_name=pim_data.PersonalDetails.last_name.upper()))

    def test_pim3(self, launch_driver):
        # click PIM module
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_module).click()

        # search existing employee added earlier ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # wait until employee selected
        wait = WebDriverWait(self.driver, 10)
        one_record_found = wait.until(EC.text_to_be_present_in_element((By.XPATH, pim_data.ElementLocators.xpath_one_record_found), text_="(1) Record Found"))

        # click delete employee button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_delete_button).click()

        # click delete confirmation alert
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_delete_alert).click()

        # verify deletion by again searching employee present or not
        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # print employee deleted status
        # if no records found for that employee, then employee deleted
        no_records = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_confirm_no_records).text
        assert no_records == "No Records Found"
        print("SUCCESS # EMPLOYEE \"{first_name} {last_name}\" DETAILS DELETED".format(
            first_name=pim_data.PersonalDetails.first_name.upper(),
            last_name=pim_data.PersonalDetails.last_name.upper()))
