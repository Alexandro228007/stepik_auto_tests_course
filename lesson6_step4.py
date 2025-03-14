from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализация браузера
browser = webdriver.Chrome()
try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем, пока цена не станет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Ждем некоторое время, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
