import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a fixture for the Selenium WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Adjust the WebDriver path if necessary
    driver.implicitly_wait(10)   # Adding an implicit wait for element loading
    yield driver
    driver.quit()

# Error Scenario 1: Element Not Found
def test_element_not_found(driver):
    driver.get("https://www.example.com")
    
    # Trying to locate an element that doesn't exist
    try:
        non_existent_element = driver.find_element(By.ID, "nonExistentElement")
    except NoSuchElementException:
        print("Caught NoSuchElementException as expected")

# Error Scenario 2: Timeout Exception
def test_timeout_exception(driver):
    driver.get("https://www.example.com")
    
    # Trying to wait for an element that doesn’t appear within a short timeout
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "delayedElement"))
        )
    except TimeoutException:
        print("Caught TimeoutException as expected")

# Error Scenario 3: Incorrect Assertion
def test_incorrect_assertion(driver):
    driver.get("https://www.wikipedia.org/")
    
    # Searching for "Python" but asserting wrong title
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)
    
    # Deliberately incorrect assertion to simulate an error
    assert "JavaScript" in driver.title  # This will fail

# Error Scenario 4: Stale Element Reference
def test_stale_element_reference(driver):
    driver.get("https://www.wikipedia.org/")
    
    # Find and store a reference to an element
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium")
    
    # Refresh the page, causing the element reference to become stale
    driver.refresh()
    
    # Attempt to interact with the stale element
    try:
        search_box.send_keys(Keys.RETURN)
    except StaleElementReferenceException:
        print("Caught StaleElementReferenceException as expected")

# Error Scenario 5: Element Not Interactable
def test_element_not_interactable(driver):
    driver.get("https://www.wikipedia.org/")
    
    # Attempt to interact with an element before it becomes interactable
    try:
        footer_link = driver.find_element(By.CLASS_NAME, "footer-places-about")
        footer_link.click()  # This might fail if the element is not yet interactable
    except Exception as e:
        print(f"Caught Exception as expected: {e}")
