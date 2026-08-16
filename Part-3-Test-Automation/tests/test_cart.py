from selenium.webdriver.common.by import By


def login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_add_product_to_cart(driver):
    """
    AT-05
    TC-028: Add one product to cart
    """

    # Login
    login(driver)

    # Add Sauce Labs Backpack
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    # Verify cart badge
    cart_badge = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert cart_badge.text == "1"


def test_remove_product_from_cart(driver):
    """
    AT-06
    TC-053: Remove product
    """

    # Login
    login(driver)

    # Add product
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    # Open cart
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Remove product
    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    # Verify cart is empty
    cart_items = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(cart_items) == 0