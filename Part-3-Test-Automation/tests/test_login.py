from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


def login(driver):
    """
    Common login helper
    """

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 15)

    # Enter username
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("standard_user")

    # Enter password
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    ).send_keys("secret_sauce")

    # Click Login
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    ).click()

    # Verify Products page
    wait.until(
        EC.url_contains("inventory.html")
    )


# ============================================================
# TC-001: Login with valid credentials
# ============================================================

def test_login_valid_credentials(driver):
    """
    TC-001: Login with valid credentials
    """

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 15)

    # Enter username
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("standard_user")

    # Enter password
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    ).send_keys("secret_sauce")

    # Click Login
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    ).click()

    # Verify successful login
    wait.until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url


# ============================================================
# TC-002: Login with locked user
# ============================================================

def test_login_locked_user(driver):
    """
    TC-002: Login with locked user
    """

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 15)

    # Enter locked username
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("locked_out_user")

    # Enter password
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    ).send_keys("secret_sauce")

    # Click Login
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    ).click()

    # Verify error message
    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "locked out" in error_message.text.lower()


# ============================================================
# TC-014: Login using Enter key
# ============================================================

def test_login_using_enter_key(driver):
    """
    TC-014: Login using Enter key
    """

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 15)

    # Enter username
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    username.send_keys("standard_user")

    # Enter password
    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    )

    password.send_keys("secret_sauce")

    # Press Enter instead of clicking Login
    password.send_keys(Keys.ENTER)

    # Verify successful login
    wait.until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url