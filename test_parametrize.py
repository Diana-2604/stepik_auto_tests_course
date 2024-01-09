# PyTest позволяет запустить один и тот же тест с разными входными параметрами.
# Для этого используется декоратор @pytest.mark.parametrize().

# В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.
# В самом тесте наш параметр тоже нужно передавать в качестве аргумента.
# pytest -s -v test_parametrize.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
