from selenium import webdriver
import HtmlTestRunner


def test_logout():
    # setup
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chrome_driver.exe")
    driver.set_page_load_timeout("10")
    driver.maximize_window()
    # login
    driver.get("http://automationpractice.com")
    driver.find_element_by_class_name("login").click()
    driver.find_element_by_name("email").send_keys("xxxralphlaurenxxx@gmail.com")
    driver.find_element_by_name("passwd").send_keys("123698745")
    driver.find_element_by_name("SubmitLogin").click()
    # test_logout
    driver.find_element_by_class_name("logout").click()
    # Проверка теста
    x = driver.title
    assert x == 'Login - My Store'
    # teardown
    driver.close()
    driver.quit()
