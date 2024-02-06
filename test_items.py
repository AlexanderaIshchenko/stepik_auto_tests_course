import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button_from_the_product_page_displayed(browser):
    browser.get(link)
    browser.implicitly_wait(7)

    assert browser.find_element(By.CLASS_NAME, "btn-primary"), "Button is missing"
    time.sleep(30)

