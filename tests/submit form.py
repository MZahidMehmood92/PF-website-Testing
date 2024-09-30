from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pageObjects.formElements import FormElements
import time


driver = webdriver.Chrome()
driver.get("https://pf.com.pk/job/senior-and-mid-level-backend-developer/")
driver.maximize_window()
time.sleep(3)


gender_radio_button = driver.find_element(By.XPATH, FormElements.gender)
gender_radio_button.click()
print("Gender selection button work")

dob = driver.find_element(By.XPATH, FormElements.dob)
driver.execute_script("arguments[0].removeAttribute('onkeydown')", dob)
dob.click()
driver.execute_script("arguments[0].value = '2001-10-01'", dob)
print("Date of birth field work")
time.sleep(2)

full_name = driver.find_element(By.XPATH, FormElements.full_name)
full_name.send_keys("Muhammad Awais")
print("Name field work")
time.sleep(2)

email = driver.find_element(By.XPATH, FormElements.email)
email.send_keys("m.awais01@gmail.com")
print("Email field work")
time.sleep(2)

cnic = driver.find_element(By.XPATH, FormElements.cnic)
cnic.send_keys("3520217322479")
print("CNIC field work")
time.sleep(2)

contact_number = driver.find_element(By.XPATH, FormElements.contact_number)
contact_number.send_keys("03394567899")
print("Contact Number field work")
time.sleep(2)

address = driver.find_element(By.XPATH, FormElements.address)
address.send_keys("Johar Town")
print("Address field work")
time.sleep(2)

city = driver.find_element(By.XPATH, FormElements.city)
city.send_keys("Lahore")
print("City Number field work")
time.sleep(2)

qualification_dropdown = driver.find_element(By.XPATH, FormElements.qualification)
select = Select(qualification_dropdown)
select.select_by_visible_text('BSIT')
print("Select Qualification field work")
time.sleep(2)

completion_dropdown = driver.find_element(By.XPATH, FormElements.comp_year)
select = Select(completion_dropdown)
select.select_by_visible_text('2022')
print("Select Completion Year field work")
time.sleep(2)

university = driver.find_element(By.XPATH, FormElements.university)
university.send_keys("Bahria University")
print("University field work")
time.sleep(2)

cgpa = driver.find_element(By.XPATH, FormElements.cgpa)
cgpa.send_keys("3.0")
print("CGPA field work")
time.sleep(2)

work_radio_button = driver.find_element(By.XPATH, FormElements.work)
work_radio_button.click()
print("Work radio button work")
time.sleep(2)

expected_salary = driver.find_element(By.XPATH, FormElements.exp_salary)
expected_salary.send_keys("80000")
print("Expected Salary field work")
time.sleep(2)

expected_date = driver.find_element(By.XPATH, FormElements.exp_date)
driver.execute_script("arguments[0].removeAttribute('onkeydown')", expected_date)
expected_date.click()
driver.execute_script("arguments[0].value = '2024-01-07'", expected_date)
print("Expected date of joining field work")
time.sleep(2)


hear_about_us = driver.find_element(By.XPATH, FormElements.hear_about_us)
hear_about_us.send_keys("from LinkedIn")
print("About us field work")
time.sleep(2)

experience_dropdown = driver.find_element(By.XPATH, FormElements.experience)
select = Select(experience_dropdown)
select.select_by_visible_text("1 Year")
print("Experience field work")
time.sleep(2)

send_resume = driver.find_element(By.XPATH, FormElements.send_resume)
send_resume.send_keys(r"C:\Users\Mr.laptop point\Desktop\Dummy form apply.pdf")
print("Send Resume field work")
time.sleep(2)

def test_click_button():
    button = driver.find_element(By.XPATH, FormElements.submit)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    print("Form submit successfully")
test_click_button()
time.sleep(12)


driver.quit()
