import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from objects.homePageElements import HomePageElements


driver = webdriver.Chrome()
driver.get("https://pf.com.pk/")
time.sleep(4)


def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.expertise)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "expertise" in driver.current_url, "Go to expertise at PF page failed."
    print("Expertise button click successfully and correct page loaded")

test_click_button()
driver.back()


def test_click_button():
    button = driver.find_element(By.XPATH,HomePageElements.about_us)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "about-us" in driver.current_url, "Go to expertise at PF page failed."
    print("About Us Button click successfully and correct page loaded")


test_click_button()
driver.back()


def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.life_at_pf)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "life-at-pf" in driver.current_url, "Go to Life at PF page failed."
    print("Life at PF button click successfully and correct page loaded")
test_click_button()
driver.back()


def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.trainee_program)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "trainee-program" in driver.current_url, "Go to Graduate Gateway Program page failed."
    print("Graduate Gateway Program button click successfully and correct page loaded")
test_click_button()
driver.back()


def test_click_button():
    button = driver.find_element(By.XPATH,HomePageElements.career)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "career" in driver.current_url, "Go to career page failed."
    print("Career button click successfully and correct page loaded")
test_click_button()
driver.back()

def test_click_button():
    button = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/div[2]/div/nav/div/ul/li[8]/a")
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "apply-now" in driver.current_url, "Go to apply now page failed."
    print("Apply Now button click successfully and correct page loaded")
test_click_button()
driver.back()


action = ActionChains(driver)
pak_flag = driver.find_element(By.CLASS_NAME, "imgdiv")
uk_flag = driver.find_element(By.XPATH, "//*[@id='masthead']/div[1]/div[2]/p[2]/a")
action.move_to_element(pak_flag).perform()
action.move_to_element(uk_flag).click().perform()

if uk_flag.is_enabled():
    print("Button is clickable.")
else:
    print("Button is not clickable.")

time.sleep(3)

expected_url = "https://programmersforce.co.uk/"
current_url = driver.current_url

if current_url == expected_url:
    print("UK flag. Correct page loaded.")
else:
    print(f"UK flag. Current URL: {current_url}")


def test_logo_click():
    button = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/div[1]/div[1]/a/picture/img[2]")
    assert button.is_displayed(), "logo is visible on the page."
    button.click()
    assert "pf" in driver.current_url, "Redirect to home page failed."
    print("PF Logo click successfully and redirect the homepage")
test_logo_click()
driver.quit()


