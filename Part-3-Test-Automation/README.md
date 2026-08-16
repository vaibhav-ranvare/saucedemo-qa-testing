# Part 3 — Test Automation | SauceDemo

## 📌 Overview

This section contains the **UI Test Automation** implementation for the SauceDemo web application.

The automation framework is developed using:

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Google Chrome**

A total of **8 functional test cases** have been automated from the manual test cases created in Part 1.

---

## 🌐 Application Under Test

**Application:** SauceDemo

**URL:** https://www.saucedemo.com/

SauceDemo is a demo e-commerce application used for practicing web application testing and test automation.

---

# 🎯 Automation Objective

The objective of this automation project is to:

- Automate functional test cases from Part 1
- Validate important SauceDemo user workflows
- Demonstrate Selenium WebDriver skills
- Use reliable element locators
- Use explicit waits
- Implement Pytest test execution
- Verify expected application behavior using assertions
- Create a maintainable and easy-to-run automation suite

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| Google Chrome | Browser |
| ChromeDriver | Browser Automation Driver |
| Git | Version Control |
| GitHub | Source Code Management |

---

# 📂 Project Structure

```text
Part-3-Test-Automation/
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
