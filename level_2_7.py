from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()


try:
    browser.get(link)
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Svetlana")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Kuliokva")
    e_mail = browser.find_element_by_name("email")
    e_mail.send_keys("svkulqa@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attach = browser.find_element_by_id("file")
    attach.send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(6)
    browser.quit()
