from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
# link = "https://suninjuly.github.io/selects1.html" code works on both pages
link = "https://suninjuly.github.io/selects2.html"

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    # get text between two html tags of the selected element
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)
    z = str(x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
