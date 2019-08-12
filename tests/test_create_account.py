from selenium import webdriver
import pytest
# import HtmlTestRunner
import time


# Создадим списки для каждой необходимой переменной и приведем его в удобный для нас вид
with open("config") as config:
    email = config.readline().strip()[7:].split(', ')
    frst_n = config.readline().strip()[11:].split(', ')
    lst_n = config.readline().strip()[10:].split(', ')
    paswd = config.readline().strip()[10:].split(', ')
    street = config.readline().strip()[8:].split(', ')
    city = config.readline().strip()[6:].split(', ')
    state = config.readline().strip()[7:].split(', ')
    post = config.readline().strip()[10:].split(', ')
    phone = config.readline().strip()[14:].split(', ')


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chrome_driver.exe")
    driver.set_page_load_timeout("10")
    driver.maximize_window()


# Проверка функционала "Create account"
@pytest.mark.parametrize('em, fst_name, lst_name, pwd, strt, city, state, post, phone',
                         [
                             (email[0], frst_n[0], lst_n[0], paswd[0], street[0], city[0], state[0], post[0], phone[0]),
                             (email[1], frst_n[1], lst_n[1], paswd[1], street[1], city[1], state[1], post[1], phone[1])
                         ]
                         )
def test_create_account(em, fst_name, lst_name, pwd, strt, city, state, post, phone):
    driver.get("http://automationpractice.com")
    driver.find_element_by_class_name("login").click()
    driver.find_element_by_name("email_create").send_keys(em)
    driver.find_element_by_name("SubmitCreate").click()
    # Задержка между операциями, чтобы прогрузились страницы
    time.sleep(3)
    driver.find_element_by_name("customer_firstname").send_keys(fst_name)
    driver.find_element_by_name("customer_lastname").send_keys(lst_name)
    driver.find_element_by_name("passwd").send_keys(pwd)
    driver.find_element_by_name("address1").send_keys(strt)
    driver.find_element_by_name("city").send_keys(city)
    driver.find_element_by_name("id_state").send_keys(state)
    driver.find_element_by_name("id_state").click()
    driver.find_element_by_name("postcode").send_keys(post)
    driver.find_element_by_name("phone_mobile").send_keys(phone)
    driver.find_element_by_name("alias").send_keys(city)
    driver.find_element_by_name("submitAccount").click()
    time.sleep(3)
    # Проверка теста
    x = driver.title
    assert x == 'My account - My Store'


def test_teardown():
    driver.close()
    driver.quit()