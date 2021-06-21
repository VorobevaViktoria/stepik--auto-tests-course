from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name('firstname')
    name.send_keys('Vika')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Vorobeva')
    email = browser.find_element_by_name('email')
    email.send_keys('Vorobeva@gmail.com')
	
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson8.txt')
	 
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

     
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
