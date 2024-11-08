import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Define a fixture for the Selenium WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Adjust the WebDriver path if necessary
    yield driver
    driver.quit()
def test_login(driver):
    # Open the login page
    driver.get("https://example.com/login")
    # Locate the username and password fields and the login button
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    # Send username and password to the fields
    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")
    # Click the login button
    login_button.click()
    # Assert that the login was successful by checking if the URL changes or some element appears
    assert "dashboard" in driver.current_url  # Replace with the actual condition for successful login






