from selenium import webdriver
import pytest
import HtmlTestRunner


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chrome_driver.exe")
    driver.set_page_load_timeout("10")
    driver.maximize_window()


# Проверка функционала "Login"
@pytest.mark.parametrize('em, pwd',
                         [
                             ('tech_tech_tech@mail.ru', '123456789'),
                             ('failed@mail.ru', '*24214422'),
                             ('failed@gmail.com', '@a2424244'),
                             ('xxxralphlaurenxxx@gmail.com', '123698745')
                         ]
                         )
def test_login(em, pwd):
    driver.get("http://automationpractice.com")
    driver.find_element_by_class_name("login").click()
    driver.find_element_by_name("email").send_keys(em)
    driver.find_element_by_name("passwd").send_keys(pwd)
    driver.find_element_by_name("SubmitLogin").click()
    # Проверка теста
    x = driver.title
    assert x == 'My account - My Store'


def test_teardown():
    driver.close()
    driver.quit()
