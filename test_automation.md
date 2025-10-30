# Test Automation — Руководство и артефакты

Кратко: папка/файлы с автотестами и вспомогательными артефактами, инструкции по запуску и рекомендации по организации.

## Содержание
- Обзор и цель
- Структура репозитория (путь к тестам)
- Как запустить локально
- Запуск в CI (пример для GitHub Actions)
- Полезные советы и рекомендации

---

## Обзор
Этот файл собирает все материалы по автоматизации: примеры тестов на pytest, фикстуры, конфигурации и зависимости. Используйте его как инструкцию для быстрого старта и как навигацию по артефактам.

## Включённые файлы
Ниже — файлы автотестов и вспомогательные модули, уже находящиеся (или планируемые) в репозитории:

- [`test_bookstore.py`](test_bookstore.py) — тесты для магазина/книг (пример функциональных API-тестов)
- [`test_api.py`](test_api.py) — общие API-тесты
- [`conftest.py`](conftest.py) — фикстуры и вспомогательная настройка pytest
- [`math_utils.py`](math_utils.py) — вспомогательный модуль с математическими функциями (unit-тесты)
- [`test_math_utils.py`](test_math_utils.py) — тесты для math_utils.py
- [`test_math_utils1.py`](test_math_utils1.py) — дополнительный набор тестов для math_utils
- [`test_users.py`](test_users.py) — тесты для пользователей / endpoints пользователей


## Рекомендуемая структура (пример)
- pytest_example.py — простой односценарный пример в корне (demo)
- api_tests/ — коллекция модульных тестов (например, test_auth.py, test_users.py)
- automation/ — альтернативная папка для более крупных наборов тестов
- conftest.py — общие фикстуры (session, client, base_url, auth)
- requirements.txt — зависимости (requests, pytest, pytest-html и т.д.)
- README.md (в корне) — ссылка на этот файл


## Как запустить локально
1. Создать виртуальное окружение:
   python -m venv .venv
2. Активировать:
   - macOS / Linux: source .venv/bin/activate
   - Windows: .venv\Scripts\activate
3. Установить зависимости:
   pip install -r requirements.txt
4. Запустить:
   pytest -q
   pytest api_tests/ -q

Полезные опции:
- pytest -k "auth" — запустить тесты с ключевым словом
- pytest --maxfail=1 -q — fail fast
- pytest --html=report.html — генерировать HTML-отчёт (при установленном pytest-html)

## Запуск в CI — пример (GitHub Actions)
Пример простого workflow (создать .github/workflows/ci.yml):

```yaml
name: pytest

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
      - name: Run tests
        run: |
          . .venv/bin/activate
          pytest -q --maxfail=1 --disable-warnings
      - name: Upload pytest junit (optional)
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: report.xml
```


## Организация и хорошие практики
- Держите общие фикстуры в conftest.py, тесты — в отдельных файлах по функционалу.
- Пишите читаемые имена тестов и небольшие тестовые функции.
- Разделяйте интеграционные и быстрые unit-тесты по меткам (pytest.mark).
- Храните тестовые данные отдельно (fixtures/data/ или json/yaml).
- Добавьте basic README в папку с тестами, если их становится много.

## Что можно добавить позднее
- Примеры mock-ов/стабов
- Интеграция с тестовыми данными (fixtures, factories)
- Скрипты для локального поднятия тестовой среды (docker-compose)
- Примеры генерации отчётов (Allure / pytest-html)
