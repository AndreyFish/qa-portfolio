# Bug Report Examples

This document contains sample bug reports created during my QA practice.  
Each report follows industry standards: **Summary, Steps to Reproduce, Actual vs Expected Result, Severity, Environment**.

---

## BR-01: Login Button Not Responding After Password Reset

| Field               | Description |
|---------------------|-------------|
| **Summary**         | "Login" button becomes unclickable after password reset flow |
| **Steps to Reproduce** | 1. Go to login page<br>2. Click "Forgot password?"<br>3. Enter valid email and submit<br>4. Return to login page (via browser back button)<br>5. Enter email and new password<br>6. Click "Login" |
| **Actual Result**   | Button appears disabled; no response on click |
| **Expected Result** | User logs in successfully after password reset |
| **Severity**        | High |
| **Environment**     | Chrome 128, Windows 11, Web App v2.3 |

---

## BR-02: Incorrect Total Price in Cart with Discount

| Field               | Description |
|---------------------|-------------|
| **Summary**         | Cart total does not reflect 10% discount for promo code "WELCOME10" |
| **Steps to Reproduce** | 1. Add any product to cart<br>2. Go to checkout<br>3. Apply promo code "WELCOME10"<br>4. Observe total price |
| **Actual Result**   | Total price remains unchanged |
| **Expected Result** | Total price is reduced by 10% |
| **Severity**        | Medium |
| **Environment**     | Firefox 129, macOS Sonoma, Mobile Web |

---

> 💡 A good bug report saves developer time and accelerates fixes. I focus on clarity, reproducibility, and relevant context.
