from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    page_url = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    USERNAME_LOCATOR = (By.ID, "user-name")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    LOGIN_ERROR_LOCATOR = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    LOCKED_OUT_USER_ERROR_LOCATOR =(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")

    def login(self, username:str, password:str) -> None:
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
