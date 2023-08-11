from selenium.webdriver.common.by import By

class TestData:
    CHROME_EXECUTABLE_PATH = "C:\\Users\\sbasi\\AppData\\Local\\Programs\\Python\\Python311\\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:\\Users\\sbasi\\AppData\\Local\\Programs\\Python\\Python311\\geckodriver.exe"
    # LOGIN DATA
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    INVALID_PASSWORD = "password"
    LOGIN_PAGE_TITLE = HOME_PAGE_TITLE = "OrangeHRM"
    DASHBOARD_TEXT = "Dashboard"
    INVALID_TEXT = "Invalid credentials"
    # PIM 1
    FIRST_NAME = "Ajith"
    LAST_NAME = "Kumar"
    EMPLOYEE_ID_NO = "4563"
    EMPLOYEE1_ID_NO = "0786"
    EMPLOYEE_OTHER_ID_NO = "27486312"
    LICENSE_NUMBER = "110579"
    LICENSE_EXPIRY_DATE_NO = "2032-12-10"
    EMPLOYEE_DOB_NO = "1992-01-05"
    EMPLOYEE_NAME = "Ajith Kumar"
    # PIM 2
    UPDATED_EMPLOYEE_ID_NO = "4565"
    UPDATED_EMPLOYEE_OTHER_ID = "355"
    UPDATED_LICENSE_NUMBER = "0528"
    UPDATED_LICENSE_EXPIRY_DATE_NO = "1995-12-10"
    
    # PIM 3
    NO_RECORDS_FOUND = "No Records Found"
    TEXT = "(1) Record Found"

class WebLocators:
    # Login Locators
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOGIN = (By.XPATH, '//button[@type="submit"]')
    DASHBOARD = (By.XPATH, '//div[1]/span/h6')
    INVALID_LOGIN = (By.XPATH, '//div[1]/p')

    # TEST PIM 1
    # click PIM module
    PIM_MODULE = (By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"][2]//a')
    # click add button
    ADD_BUTTON = (By.XPATH, '//div[@class="orangehrm-header-container"]//button')
    # fill the personal details
    EMPLOYEE_FIRSTNAME = (By.XPATH, '//input[@name="firstName"]')
    EMPLOYEE_LASTNAME = (By.XPATH, '//input[@name="lastName"]')
    # clear default employee id and adding new employee id
    SELECT_ALL = "Keys.CONTROL, 'a'"
    DELETE = "Keys.DELETE"
    EMPLOYEE_ID = (By.XPATH, '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]//input[@class="oxd-input oxd-input--active"]')
    # click save button
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    # editing the employee information (Personal details)
    EMPLOYEE1_ID = (By.XPATH, '//form/div[2]/div[1]/div[1]/div/div[2]/input')
    EMPLOYEE_OTHER_ID = (By.XPATH, '//div[@class="oxd-form-row"][2]/div[1]/div[2]/div//input')
    EMPLOYEE_DRIVER_LICENSE_NUMBER = (By.XPATH, '//div[@class="oxd-form-row"][2]//div[2]//div[@class="oxd-grid-item oxd-grid-item--gutters"][1]//input')
    EMPLOYEE_LICENSE_EXPIRY_DATE = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
    EMPLOYEE_NATIONALITY = (By.XPATH, '//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
    INDIAN_NATIONALITY = (By.XPATH, '//form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]/span')
    EMPLOYEE_MARITAL_STATUS = (By.XPATH, '//form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')
    SINGLE_MARITAL_STATUS = (By.XPATH, '//form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span')
    EMPLOYEE_DOB = (By.XPATH, '//form//div[3]//div[2]//div[1]//div//div[2]//div//div//input[@class="oxd-input oxd-input--active"]')
    EMPLOYEE_GENDER = (By.XPATH, '//form//div[3]//div[2]//div[2]//div//div[2]//div[1]//div[2]//div//label//span')
    SAVE1_BUTTON = (By.XPATH, '//form/div[5]/button')
    USER_GENERATED = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 --strong"]')

    # TEST PIM 2
    EMPLOYEE_SEARCH = (By.XPATH, '//div/div[1]/div/div[2]/div/div/input')
    EDIT_BUTTON = (By.XPATH, '//div[9]/div/button[2]')
    LIST_BUTTON = (By.XPATH, '//li[2]//a[@class="oxd-topbar-body-nav-tab-item"]')
    EDITED_ID = (By.XPATH, '//div[3]/div/div[2]/div/div/div[2]/div')

    # TEST PIM 3
    ONE_RECORD_FOUND = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span')
    DELETE_BUTTON = (By.XPATH, '//button[@class="oxd-icon-button oxd-table-cell-action-space"][1]')
    DELETE_ALERT = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')
    CONFIRM_NO_RECORDS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span')
