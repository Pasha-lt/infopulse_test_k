from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')



#search by css selector
button_1 = driver.find_element_by_css_selector('#mainContent > table:nth-child(15) > tbody > tr:nth-child(2) > td:nth-child(2) > button')
print(f'css selector: {button_1.text}')

#search by name
button_2 = driver.find_element_by_name('B1')
print(f'search by name: {button_2.text}')

#search by Xpath
button_3 = driver.find_element_by_xpath('//*[@id="mainContent"]/table[3]/tbody/tr[2]/td[2]/button')
print(f'search by Xpath: {button_3.text}')

#search by fullXpath
button_4 = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table[3]/tbody/tr[2]/td[2]/button')
print(f'search by fullXpath: {button_4.text}')




# button_4 = driver.fi
# button_2.click()


exit()
driver.get('https://google.com')

link = driver.find_element_by_css_selector('div#SIvCob a')  # пробел обозначает вложиность
link.click()
el = driver.find_element(By.NAME, "q")  # равносильно el = driver.find_element_by_name("q")

el.click()
el.send_keys('Python')
sleep(1)
button = driver.find_element_by_class_name('gNO89b')
button.click()

sleep(1)
links = driver.find_elements_by_partial_link_text('Python')
driver.close()
print(len(links))
