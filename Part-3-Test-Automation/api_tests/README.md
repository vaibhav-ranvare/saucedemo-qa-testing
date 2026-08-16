# Part 4 — API Testing | ReqRes

## 📌 Overview

This section contains the **API Test Automation** implementation for the ReqRes API.

The API tests are developed using:

- **Python**
- **Requests**
- **Pytest**
- **ReqRes API**

A total of **4 API test cases** have been automated.

---

## 🌐 API Under Test

**API:** ReqRes

**Base URL:**

https://reqres.in/api

ReqRes is a REST API used for practicing API testing and automation.

---

# 🎯 Testing Objective

The objective of this API automation is to validate:

- Successful GET request
- Successful POST request
- Invalid/missing data request
- 404 Not Found request
- HTTP status codes
- Response body structure
- Response data fields

The tests validate both **status codes AND response body shape**, rather than checking only whether the API returned a successful status code.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming Language |
| Requests | API requests |
| Pytest | Test Framework |
| ReqRes | API Under Test |
| Git & GitHub | Version Control |

---

# 🧪 Automated Test Cases

| Test Case | Method | Scenario | Expected Result |
|---|---|---|---|
| AT-09 | GET | Get users successfully | 200 + valid response structure |
| AT-10 | POST | Create user successfully | 201 + user details |
| AT-11 | POST | Login with missing password | 400 + error response |
| AT-12 | GET | Get non-existent user | 404 + empty/not-found response |

---

# 📋 Test Case Details

## AT-09 — GET Users Successfully

**Endpoint:**

`GET /users?page=2`

### Validations

- Status code is `200`
- Response is a JSON object
- `page` exists
- `per_page` exists
- `total` exists
- `total_pages` exists
- `data` exists
- `data` is a list
- User object contains:
  - `id`
  - `email`
  - `first_name`
  - `last_name`
  - `avatar`

---

## AT-10 — Create User Successfully

**Endpoint:**

`POST /users`

### Request Body

```json
{
    "name": "Vaibhav",
    "job": "QA Engineer"
}
