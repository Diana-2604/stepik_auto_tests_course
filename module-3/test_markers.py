# Как регистрировать метки:
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
# Текст после знака ":" является поясняющим — его можно не писать

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_markers.py

# Инверсия
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию.
# Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
# pytest -s -v -m "not smoke" test_markers.py

# Объединение тестов с разными маркировками
# Для запуска тестов с разными метками можно использовать логическое ИЛИ.
# Запустим smoke и regression-тесты:
# pytest -s -v -m "smoke or regression" test_markers.py

# Выбор тестов, имеющих несколько маркировок (логическое И)
# pytest -s -v -m "smoke and regression" test_markers.py


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Так же можно маркировать целый тестовый класс.
# В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.
