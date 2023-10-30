from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# from selenium.webdriver.chrome.dr
@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service_obj = Service("D:\Automation Learn Python\drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome()
    return driver
