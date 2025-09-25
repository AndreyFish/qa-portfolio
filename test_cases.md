# Test Cases Examples

This document contains sample test cases created during my QA self-study.  
All cases follow a standard structure: **ID, Preconditions, Test Steps, Expected Result**.

---

## TC-01: User Registration via Email

| Field            | Description |
|------------------|-------------|
| **ID**           | TC-01 |
| **Preconditions**| - User is on the registration page<br>- Email is not previously registered |
| **Test Steps**   | 1. Enter a valid email address<br>2. Enter a strong password<br>3. Click "Sign Up" |
| **Expected Result** | - User receives a confirmation email<br>- Account is created and user is redirected to the dashboard |

---

## TC-02: Login with Invalid Credentials

| Field            | Description |
|------------------|-------------|
| **ID**           | TC-02 |
| **Preconditions**| - User is on the login page |
| **Test Steps**   | 1. Enter an unregistered email<br>2. Enter any password<br>3. Click "Login" |
| **Expected Result** | - Error message appears: "Invalid email or password"<br>- User remains on the login page |

---

## TC-03: Password Reset Request

| Field            | Description |
|------------------|-------------|
| **ID**           | TC-03 |
| **Preconditions**| - User is on the login page<br>- Account exists |
| **Test Steps**   | 1. Click "Forgot password?"<br>2. Enter registered email<br>3. Click "Send reset link" |
| **Expected Result** | - Success message: "Password reset link sent"<br>- User receives an email with reset instructions |

---

> 💡 These test cases were designed to practice clear, reproducible, and atomic test design — a core QA skill.
