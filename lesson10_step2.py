from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book = browser.find_element_by_id("book")
    book.click()

    browser.execute_script("window.scrollBy(0,200);")


    x = browser.find_element_by_id('input_value').text
    reg = str(math.log(abs(12*math.sin(int(x)))))
    ans = browser.find_element_by_id('answer').send_keys(reg)

    button = browser.find_element_by_id("solve")
    button.click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
