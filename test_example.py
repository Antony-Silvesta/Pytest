import pytest
from selenium import webdriver
# Define a fixture for the Selenium WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title