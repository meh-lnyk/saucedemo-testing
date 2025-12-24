from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    page_url = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    USERNAME_LOCATOR = (By.ID, "user-name")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    LOGIN_ERROR_LOCATOR = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    LOCKED_OUT_USER_ERROR_LOCATOR =(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")

    COMMON_PASSWORD = "secret_sauce"
    STANDARD_USERNAME = "standard_user"
    LOCKED_OUT_USERNAME = "locked_out_user"
    PERFORMANCE_GLITCH_USERNAME = "performance_glitch_user"
    WRONG_PASSWORD = "wrong_sauce"

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def has_login_error_message(self) -> bool:
        return self.driver.find_element(*self.LOGIN_ERROR_LOCATOR)

    def wait_for_elements(self) -> None:
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_LOCATOR))
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_LOCATOR))
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR))

    def login(self, username:str, password:str) -> None:
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

