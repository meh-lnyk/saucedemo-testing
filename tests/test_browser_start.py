def test_browser_start(driver):
    driver.get("https://www.saucedemo.com/")
    assert "saucedemo" in driver.current_url
