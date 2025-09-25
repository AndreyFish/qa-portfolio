-- ==================================================
-- SQL Examples for QA: Data Validation Queries
-- Created by Andrei Bogoliubskii (QA Trainee)
-- Purpose: Verify backend data integrity during testing
-- ==================================================

-- TC-01: Validate new user registration
-- Check that a user with email 'test_user@example.com' exists and is active
SELECT user_id, email, is_active, created_at
FROM users
WHERE email = 'test_user@example.com';

-- TC-02: Verify order total after applying discount
-- Ensure the final price reflects the 10% promo code
SELECT order_id, total_amount, discount_applied, final_price
FROM orders
WHERE promo_code = 'WELCOME10'
  AND user_id = 12345;

-- TC-03: Check product inventory after purchase
-- Confirm stock decreased by 1 after an order
SELECT product_id, name, stock_quantity
FROM products
WHERE product_id = 789;

-- TC-04: List all failed login attempts in the last hour (security test)
-- Useful for testing brute-force protection
SELECT ip_address, attempt_count, last_attempt_time
FROM login_attempts
WHERE last_attempt_time >= NOW() - INTERVAL 1 HOUR
  AND attempt_count >= 3;
