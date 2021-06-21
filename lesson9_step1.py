from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button")
    button.click()

    confirm = browser.switch_to.alert.accept()
    
    x = browser.find_element_by_id('input_value').text
    print(x)
    reg = str(math.log(abs(12*math.sin(int(x)))))

    ans = browser.find_element_by_id('answer').send_keys(reg)

    button = browser.find_element_by_css_selector("button")
    button.click()

    
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
