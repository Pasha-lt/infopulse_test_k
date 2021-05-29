# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, y):
#         return self.x ** y
#
# a = A(10)
#
# b = A(2)
#
# print(a(5))
# print(a(9))
# print(b(10))


class present_of_elements_in_amount:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els
        else:
            return False


def present_of_18_menu_elements(driver):
    els = driver.find_elements(By.CSS_SELECTOR, "ul.ow_main_menu li")
    print(len(els))
    if len(els) == 18:
        return els
    else:
        return False


if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.expected_conditions import visibility_of_element_located

    dr = webdriver.Chrome()
    dr.get("https://demo.oxwall.com/")

    wait = WebDriverWait(dr, 5, poll_frequency=0.1)
    els = wait.until(present_of_elements_in_amount((By.CSS_SELECTOR, "ul.ow_main_menu li"), 18),
                     message="Not 18 menu elements")
    print(len(els))





