import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Рекомендуем также выносить очистку данных и памяти в фикстуру,
# вместо того чтобы писать это в шагах теста:
# финализатор выполнится даже в ситуации, когда тест упал с ошибкой.

# Для фикстур можно задавать область покрытия фикстур.
# Допустимые значения: “function”, “class”, “module”, “session”.
# Соответственно, фикстура будет вызываться один раз для тестового метода,
# один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии.
# Пример:
# @pytest.fixture(scope="function")

