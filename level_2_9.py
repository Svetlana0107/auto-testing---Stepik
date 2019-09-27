from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

def ex(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element_by_tag_name ("button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    arg = browser.find_element_by_id("input_value")
    x = int(arg.text)
    y = ex(x)
    answer =browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    time.sleep(5)
    browser.quit()
