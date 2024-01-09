import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_login_link(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.XPATH, "//nav/a[2]")
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable(button))
    button.click()


def enter_login(browser):
    modal_window = browser.find_element(By.CSS_SELECTOR, "sign-form")
    WebDriverWait(browser, 12).until(EC.visibility_of(modal_window))
    login_field = browser.find_element(By.ID, "id_login_email")
    login_field.clear()
    login_field.send_keys(' ')


def enter_pass(browser):
    login_field = browser.find_element(By.ID, "id_login_password")
    login_field.clear()
    login_field.send_keys(' ')


def click_login_button(browser):
    browser.find_element(By.XPATH, "//button[@type='submit']").click()



class TestUfoScenario:
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"])
    def test_try_several_links(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = f"{links}"
        browser.get(link)
        time.sleep(7)

        text = browser.find_element(By.TAG_NAME, 'textarea')
        text.send_keys(answer)

        button = browser.find_element(By.CSS_SELECTOR, 'submit-submission')
        WebDriverWait(browser, 12).until(EC.element_to_be_clickable(button))
        button.click()

        correct_answer = "Correct!"
        hint = browser.find_element(By.CSS_SELECTOR, 'smart-hints__hint')
        WebDriverWait(browser, 12).until(EC.visibility_of_element_located(hint))
        received_answer = hint.text

        assert received_answer == correct_answer







