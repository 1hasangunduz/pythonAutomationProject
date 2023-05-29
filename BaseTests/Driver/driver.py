import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver():
    service = Service('C:\\Users\\User\\PycharmProjects\\Qlub\\TestSteps\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
