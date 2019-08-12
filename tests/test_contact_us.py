from selenium import webdriver
import HtmlTestRunner
import pytest
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chrome_driver.exe")
    driver.set_page_load_timeout("10")
    driver.maximize_window()


# Проверка функционала "Contact us"
@pytest.mark.parametrize('em, message',
                         [
                             ('tech_tech_tech@mail.ru', 'Help me'),
                             ('', 'I find a bug'),
                             ('failed@gmail.com', ''),
                             ('xxxralphlaurenxxx@gmail.com', 'I need contact you')
                         ]
                         )
def test_contact_us(em, message):
    driver.get("http://automationpractice.com/index.php?controller=contact")
    driver.find_element_by_name("id_contact").send_keys("Customer service")
    driver.find_element_by_name("from").send_keys(em)
    driver.find_element_by_name("message").send_keys(message)
    driver.find_element_by_name("submitMessage").click()
    time.sleep(3)
    # Проверка теста
    assert "Your message has been successfully sent to our team" in driver.page_source


def test_teardown():
    driver.close()
    driver.quit()
