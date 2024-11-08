import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Test 1: This will pass - the element exists
def test_pass(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")  # This element exists
    assert search_input is not None  # Assert the element is found


# Test 2: This will fail - the element does not exist
def test_fail(driver):
    driver.get("https://www.wikipedia.org/")
    driver.find_element(By.ID, "nonexistent-element")  # This element doesn't exist



# Test 3: This will be skipped - using pytest.mark.skip
@pytest.mark.skip(reason="Skipping this test as an example")
def test_skipped(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.click()  # This will not be executed as the test is skipped


# Test 4: This will be an expected failure - using pytest.mark.xfail
@pytest.mark.xfail(reason="Expected failure due to invalid element interaction")
def test_expected_failure(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.click()  # This will fail, but pytest will mark it as expected failure


# Test 5: This will be an unexpected pass - using pytest.mark.xfail
@pytest.mark.xfail(reason="This is supposed to fail but we'll force it to pass")
def test_unexpected_pass(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.click()  # Expected to fail but marked as an expected failure

    assert False, "Forcing this test to pass unexpectedly."


# Test 6: This will cause an error - simulate WebDriverException
@pytest.mark.xfail(reason=" testing for error handling")
def test_error():
    try:
        driver.get("https://www.wikipedia.org/")
        driver.find_element(By.ID, "nonexistent-element")  # This will raise NoSuchElementException
        driver.quit()  # Forcing an error by calling quit after interaction
    except WebDriverException as e:
        print("Error occurred:", e)
        raise pytest.fail(f"Test failed due to an error: {e}")  # Force error to be reported as test failure


# Test 7: This will be rerun - using pytest-rerunfailures
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Retry the test 3 times with a 2-second delay
def test_rerun(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    assert search_input is None  # This will fail initially, triggering reruns



