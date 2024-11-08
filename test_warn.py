import warnings
from selenium import webdriver
def test_example():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    # Simulate an error with a warning
    if "Nonexistent Title" not in driver.title:
        warnings.warn("Simulated warning: Expected title not found.")
    # The test continues with the next steps
    driver.quit()