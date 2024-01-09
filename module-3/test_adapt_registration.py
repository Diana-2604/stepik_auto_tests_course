import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestReg(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input3.send_keys("user@email.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        required_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, required_text, "Should be equal to the required string")
        browser.quit()

    def test_registration2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input3.send_keys("user@email.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        required_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, required_text, "Should be equal to the required string")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
