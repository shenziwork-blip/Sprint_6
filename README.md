# Sprint_6 — автотесты Яндекс.Самокат

UI-тесты учебного сервиса  
https://qa-scooter.education-services.ru/

## Стек
- Python 3
- pytest
- Selenium
- Allure
- Firefox

## Структура
- `pages/` — Page Object (BasePage, MainPage, OrderPage)
- `tests/` — тесты по функциональности + conftest
- `data/` — URL и тестовые данные

## Что покрыто
- Вопросы о важном: каждый вопрос отдельно (параметризация)
- Позитивный заказ: две точки входа (кнопка сверху и снизу) и два набора данных
- Логотип Самоката → главная
- Логотип Яндекса → новое окно (Дзен / Яндекс)

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests -v --alluredir=allure_results
allure generate allure_results -o allure-report --clean
allure open allure-report
```
