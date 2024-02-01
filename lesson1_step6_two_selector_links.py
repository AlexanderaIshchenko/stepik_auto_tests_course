from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//div[1]/div[3]/input")
    input3.send_keys("ghjgjg@yande.ru")
    time.sleep(5)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла