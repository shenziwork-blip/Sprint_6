import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()
    