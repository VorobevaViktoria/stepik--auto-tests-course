from selenium import webdriver
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = int(browser.find_element_by_id('input_value').text)
    y = calc(x_element)

    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)

    browser.execute_script("window.scrollBy(0,150);")

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()
     
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
