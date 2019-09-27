from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

def ex(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element_by_tag_name ("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep (1)
    el = browser.find_element_by_id("input_value")
    el_text = el.text
    rez = ex(el_text)
    answer = browser.find_element_by_id ("answer")
    answer.send_keys(rez)
    submit = browser.find_element_by_tag_name ("button")
    submit.click()
    

finally:
    time.sleep(5)
    browser.quit()
