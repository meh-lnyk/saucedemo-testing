from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    page_url:str = None
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        if not self.page_url:
            raise ValueError("URL is not defined for this page")
        self.driver.get(self.page_url)

    def wait_for_url(self, url_part):
        self.wait.until(EC.url_contains(url_part))
