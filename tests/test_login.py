from pages.login_page import LoginPage


def test_login_page_opens(driver):
    site_obj = LoginPage(driver)
    site_obj.open()
    assert site_obj.driver.current_url == site_obj.page_url
