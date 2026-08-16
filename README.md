# 🧪 SauceDemo QA Testing Project

## 📌 Project Overview

This project is a complete **Software Quality Assurance (QA) Testing Project** performed on the **SauceDemo** web application.

The project covers the complete testing lifecycle, including:

- Manual Test Case Design
- Functional Testing
- Bug Reporting
- Selenium UI Test Automation
- Pytest Test Execution
- API Testing
- Response Status Code Validation
- Response Body Schema Validation
- Git & GitHub Project Management

The objective of this project is to demonstrate practical QA skills through both **Manual Testing and Automation Testing**.

---

# 🌐 Application Under Test

**SauceDemo**

Application URL:

https://www.saucedemo.com/

SauceDemo is a demo e-commerce web application used for practicing software testing and automation.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Create structured manual test cases.
- Execute functional test scenarios.
- Identify and document application defects.
- Create professional bug reports.
- Automate selected test cases using Selenium.
- Execute automated tests using Pytest.
- Perform API testing using Python and Requests.
- Validate HTTP status codes.
- Validate API response body structure.
- Organize the project using a professional QA project structure.
- Maintain the complete project on GitHub.

---

# 📚 Project Parts

This project is divided into four major parts:

| Part | Testing Area | Status |
|---|---|---|
| Part 1 | Manual Test Cases | ✅ Completed |
| Part 2 | Bug Reporting | ✅ Completed |
| Part 3 | UI Test Automation | ✅ Completed |
| Part 4 | API Testing | ✅ Completed |

---

# 📋 Part 1 — Manual Testing

## Objective

The first part of the project focuses on designing and executing manual test cases for the SauceDemo application.

The test cases cover important application functionality such as:

- User Login
- Product Listing
- Product Sorting
- Add Product to Cart
- Remove Product from Cart
- Checkout
- Form Validation
- Negative Test Scenarios

## Test Case Information

Each test case includes:

- Test Case ID
- Test Scenario
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Actual Result
- Status

## Example Test Scenarios

| Test Case | Scenario |
|---|---|
| TC-001 | Login with valid credentials |
| TC-002 | Login with invalid credentials |
| TC-003 | Login with locked user |
| TC-004 | Verify product listing |
| TC-005 | Add product to cart |
| TC-006 | Remove product from cart |
| TC-007 | Checkout with valid information |
| TC-008 | Validate checkout form |

---

# 🐞 Part 2 — Bug Reporting

## Objective

The second part focuses on identifying defects in the SauceDemo application and documenting them professionally.

The testing was performed using different SauceDemo user accounts, including accounts with intentionally seeded problematic behavior.

## Bug Report Includes

Each bug report contains:

- Bug ID
- Bug Title
- Severity
- Priority
- Environment
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Screenshot
- Bug Status






## Bug Reporting Process

```text
Execute Test Case
       ↓
Identify Unexpected Behavior
       ↓
Reproduce the Issue
       ↓
Document Bug
       ↓
Capture Screenshot
       ↓
Assign Severity & Priority
       ↓
Create GitHub Issue

---

# Part 3 — Test Automation

## 📌 Overview

Part 3 contains the **UI Test Automation** implementation for the SauceDemo web application.

The test automation framework is developed using **Python, Selenium WebDriver, and Pytest**.

A total of **8 functional test cases** have been automated from the manual test cases created in Part 1.

---

## 🛠️ Technology Stack

- Python 3.11
- Selenium WebDriver
- Pytest
- Google Chrome
- ChromeDriver
- Git & GitHub

---

## 🌐 Application Under Test

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com/

SauceDemo is a demo e-commerce application used for practicing functional testing and test automation.

---

## 🎯 Automated Test Coverage

The following 8 test cases are automated:

### 🔐 Login Tests

| Test Case | Description |
|---|---|
| `test_login_valid_credentials` | Verify login using valid credentials |
| `test_login_locked_user` | Verify locked user cannot log in |
| `test_login_using_enter_key` | Verify login using Enter key |

### 🛍️ Product Tests

| Test Case | Description |
|---|---|
| `test_product_listing` | Verify products are displayed |
| `test_product_sorting_low_to_high` | Verify products can be sorted by price |

### 🛒 Cart Tests

| Test Case | Description |
|---|---|
| `test_add_product_to_cart` | Verify product can be added to cart |
| `test_remove_product_from_cart` | Verify product can be removed from cart |

### 💳 Checkout Tests

| Test Case | Description |
|---|---|
| `test_checkout_page_opens` | Verify checkout page opens successfully |

---

## 📂 Part 3 Project Structure

```text
saucedemo-qa-testing/
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── api_tests/
│   └── test_reqres_api.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

----


# Part 4 — API Testing | ReqRes

## 📌 Overview

Part 4 contains automated **API tests** for the ReqRes API.

The API automation is implemented using **Python, Requests, and Pytest**.

The test suite covers successful API requests, invalid/missing data, and a 404 Not Found scenario.

---

## 🌐 API Under Test

**API:** ReqRes

**Base URL:**

https://reqres.in/api

---

## 🛠️ Technology Stack

- Python 3.11
- Requests
- Pytest
- REST API
- JSON
- Git & GitHub

---

## 🎯 Test Coverage

A total of **4 API test cases** have been automated.

| Test Case | HTTP Method | Scenario |
|---|---|---|
| `test_get_users_success` | GET | Verify users are retrieved successfully |
| `test_create_user_success` | POST | Verify a user can be created successfully |
| `test_login_missing_password` | POST | Verify validation when password is missing |
| `test_get_nonexistent_user` | GET | Verify 404 response for a non-existent user |

---

## 🔎 Assertions

The tests validate both:

### 1. HTTP Status Code

Examples:

```text
200 OK
201 Created
4xx Client Error
404 Not Found
