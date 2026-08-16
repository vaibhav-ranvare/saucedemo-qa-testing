from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait


def test_product_listing(driver):
    """
    Verify products are displayed after successful login.
    """

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(products) > 0


def test_product_sorting_low_to_high(driver):
    """
    Verify products can be sorted by price from low to high.
    """

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_value("lohi")

    prices = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    price_values = [
        float(price.text.replace("$", ""))
        for price in prices
    ]

    assert price_values == sorted(price_values)

    