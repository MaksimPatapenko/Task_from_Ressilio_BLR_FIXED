from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import HtmlTestRunner


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chrome_driver.exe")
    driver.set_page_load_timeout("10")
    driver.maximize_window()


# Проверка функционала "Forgot your password"
@pytest.mark.parametrize('em',
                         [
                             ('tech_tech_tech@mail.ru'),
                             ('xxxralphlaurenxxx'),
                             ('failed@gmail.com'),
                             ('sk8-boards@mail.ru')
                         ]
                         )
def test_forgot_your_password(em):
    driver.get("http://automationpractice.com/index.php?controller=password")
    driver.find_element_by_name("email").send_keys(em)
    driver.find_element_by_name("email").send_keys(Keys.ENTER)
    # Проверка теста
    assert "A confirmation email has been sent to your address: {}".format(em) in driver.page_source


def test_teardown():
    driver.close()
    driver.quit()
