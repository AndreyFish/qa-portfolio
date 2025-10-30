import requests

<<<<<<< HEAD

def test_get_books(base_url):
    r = requests.get(f"{base_url}/posts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
=======
def test_create_order(base_url):
    # Шаг 1: Получить список книг
    response = requests.get(f"{base_url}/api/books")
    assert response.status_code == 200
    books = response.json()
    assert len(books) > 0

    # Шаг 2: Выбрать первую книгу
    book_id = books[0]["id"]

    # Шаг 3: Оформить заказ
    payload = {"bookId": book_id, "customerName": "Андрей"}
    response = requests.post(f"{base_url}/api/orders", json=payload)
    assert response.status_code == 201
    order = response.json()
    assert order["customerName"] == "Андрей"
    assert order["bookId"] == book_id

    # Шаг 4: Проверить, что заказ создан
    order_id = order["id"]
    response = requests.get(f"{base_url}/api/orders/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id   
>>>>>>> 1d807e8 (Fix conftest: clean fixtures and set base_url to jsonplaceholder)
