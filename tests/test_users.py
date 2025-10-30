
import pytest
# Фикстура: создаёт список пользователей
@pytest.fixture
def users():
    return [
        {"name": "Иссидора", "age": 25, "active": True},
        {"name": "Лаврентий", "age": 30, "active": False},
        {"name": "Зинаида", "age": 22, "active": True}
    ]

# Тест: проверяем количество активных пользователей
def test_active_users_count(users):
    active = [u for u in users if u["active"]]
    assert len(active) == 2

# Тест: средний возраст
def test_average_age(users):
    ages = [u["age"] for u in users]
    avg = sum(ages) / len(ages)
    assert round(avg, 1) == 25.7   