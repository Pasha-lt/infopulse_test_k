from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(executable_path='./chromedriver')
# driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')
#
# # search by css selector
# button_1 = driver.find_element_by_css_selector('#mainContent > table:nth-child(15) > tbody > tr:nth-child(2) > td:nth-child(2) > button')
# print(f'css selector: {button_1.text}')
#
# # search by name
# button_2 = driver.find_element_by_name('B1')
# print(f'search by name: {button_2.text}')
#
# # search by Xpath
# button_3 = driver.find_element_by_xpath('//*[@id="mainContent"]/table[3]/tbody/tr[2]/td[2]/button')
# print(f'search by Xpath: {button_3.text}')
#
# # search by fullXpath
# button_4 = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table[3]/tbody/tr[2]/td[2]/button')
# print(f'search by fullXpath: {button_4.text}')


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# dr = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
#                       desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_element_present(driver, by, locator):
    try:
        driver.find_element(by, locator)
    except NoSuchElementException:
        return False
    return True

dr = webdriver.Chrome()
wait = WebDriverWait(dr, 2)
actions = webdriver.ActionChains(dr)
ta = webdriver.TouchActions(dr)

# dr.implicitly_wait(5)
dr.get("https://google.com")

assert is_element_present(dr, By.CLASS_NAME, "gNO89b")
dr.find_element()
# link = dr.find_element_by_css_selector("div#SIvCob a")
# link.click()

el = dr.find_element_by_css_selector('.gLFyf.gsfi[type="text"]')
el.clear()
el.send_keys("python")

el.send_keys(Keys.HOME)
# el.send_keys(Keys.ARROW_LEFT)
el.send_keys("sdfsdf")


# time.sleep(2)

# button = dr.find_element_by_class_name("gNO89b")

button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gNO89b")),
                    message="Can't find clicable element")

print(button.location)
print(button.size)

button.click()

time.sleep(2)
links = dr.find_elements_by_partial_link_text("Python")
print(len(links))

for link in links:
    print(link.text)


dr.find_elements_by_xpath("//a[contains(text(), 'google')]")
dr.find_element_by_xpath('//*[@id="gsr"]')



# dr.close()
# dr.quit()
