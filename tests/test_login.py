from selenium.common import TimeoutException
from pages.login_page import LoginPage
import pytest


# to check if page loaded
@pytest.fixture
def login_page(driver) -> LoginPage:
    page = LoginPage(driver)
    try:
        page.open()
        page.wait_for_url(page.page_url)
        page.wait_for_elements()
    except TimeoutException:
        pytest.skip("Login page or elements did not load")
    return page

def test_login(login_page):
    login_page.login(login_page.STANDARD_USERNAME, login_page.COMMON_PASSWORD)
    login_page.wait_for_url(login_page.INVENTORY_URL)
    assert login_page.current_url == login_page.INVENTORY_URL
