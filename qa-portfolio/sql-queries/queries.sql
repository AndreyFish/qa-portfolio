-- Пример 1: все пользователи
SELECT * FROM users;

-- Пример 2: количество заказов у клиента
SELECT customer_id, COUNT(*) as order_count
FROM orders
GROUP BY customer_id;

-- Пример 3: топ-5 товаров по продажам
SELECT product_id, SUM(quantity) as total_sales
FROM order_items
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;
