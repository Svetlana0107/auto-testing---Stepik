from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link ="http://suninjuly.github.io/explicit_wait2.html"

def ex(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element_by_id("book")
    button.click()
    arg = browser.find_element_by_id("input_value")
    x = int(arg.text)
    y = ex(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    

finally:
    time.sleep(3)
    browser.quit()
    
    
