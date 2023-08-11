import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Pass multiple browser params for cross browser testing 
@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request) :
    if request.param == "chrome":
        options = Options()
        options.add_argument("start-maximized")
        web_driver = webdriver.Chrome(options=options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()