from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://google.com')

link = driver.find_element_by_css_selector('div#SIvCob a')# пробел обозначает вложиность
link.click()
el = driver.find_element(By.NAME, "q") # равносильно el = driver.find_element_by_name("q")

el.click()
el.send_keys('Python')
sleep(1)
button = driver.find_element_by_class_name('gNO89b')
button.click()

sleep(1)
links = driver.find_elements_by_partial_link_text('Python')
driver.close()
print(len(links))
