from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input").send_keys("user@email.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    return browser.find_element(By.TAG_NAME, "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration1 failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration2 failed")


if __name__ == "__main__":
    unittest.main()
