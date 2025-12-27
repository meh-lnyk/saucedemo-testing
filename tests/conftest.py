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

    if os.getenv("CI") or os.getenv("DOCKER"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # detecting if running in Docker
    if os.getenv("DOCKER"):
        driver_path = "/usr/bin/chromedriver"  # preinstalled in selenium/standalone-chrome
    else:
        # using webdriver manager for local environment
        driver_path = ChromeDriverManager().install()

    print("Using ChromeDriver at:", driver_path) # for debugging purposes

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
