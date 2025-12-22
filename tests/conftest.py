import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    path = ChromeDriverManager().install()

    driver_path = os.path.join(os.path.dirname(path), "chromedriver.exe")

    print("Using ChromeDriver at:", driver_path) # for debugging purposes

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
