from selenium import webdriver

def create_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver
