from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("standard_user")

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    ).send_keys("secret_sauce")

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    ).click()

    wait.until(
        EC.url_contains("inventory.html")
    )


def test_checkout_page_opens(driver):

    login(driver)

    wait = WebDriverWait(driver, 15)

    # Add product
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(
        EC.url_contains("cart.html")
    )

    # Click checkout
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    ).click()

    # Verify checkout page
    wait.until(
        EC.url_contains("checkout-step-one.html")
    )

    # Verify First Name field
    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    assert first_name.is_displayed()