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



#Apply Now Button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.apply_now)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "apply-now" in driver.current_url, "Go to apply now page failed."
    print("Apply Now button click successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()


# Career Dropdown Option 1(Open Positions)
def career_dropdown_click_button():
    actions=ActionChains(driver)
    Career_button = driver.find_element(By.XPATH, HomePageElements.career)
    actions.move_to_element(Career_button).perform()
    Career_dropdown1 = driver.find_element(By.ID, HomePageElements.career_drop1)
    Career_dropdown1.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Careers option 1 Open positions click successfully and correct page open")
    else:
        print("Careers option 1 Open positions not work")
career_dropdown_click_button()
time.sleep(2)
driver.back()


# Career Dropdown Option 2(Send Resume)
def career_dropdown_click_button():
    actions = ActionChains(driver)
    Career_button = driver.find_element(By.XPATH, HomePageElements.career)
    actions.move_to_element(Career_button).perform()
    Career_dropdown2= driver.find_element(By.ID, HomePageElements.career_drop2)
    Career_dropdown2.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/apply-now/#popup1"
    if driver.current_url == expected_url:
        print("Careers option 2 Open positions click successfully and correct page open")
    else:
        print("Careers option 2 Open positions not work")
career_dropdown_click_button()
time.sleep(2)
driver.back()


# Resources Dropdown Option 1(Blogs)
def resources_dropdown_click_button():
    actions = ActionChains(driver)
    Resource_button = driver.find_element(By.XPATH, HomePageElements.resource)
    actions.move_to_element(Resource_button).perform()
    Resource_dropdown1 = driver.find_element(By.XPATH, HomePageElements.resource_drop1)
    Resource_dropdown1.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/blogs/"
    if driver.current_url == expected_url:
        print("Resources option 1 Blogs click successfully and correct page open")
    else:
        print("Resources option 2 Blogs not work")
resources_dropdown_click_button()
time.sleep(2)
driver.back()



# Resources Dropdown Option 2(News)
def resources_dropdown_click_button():
    actions = ActionChains(driver)
    Resource_button = driver.find_element(By.XPATH,HomePageElements.resource)
    actions.move_to_element(Resource_button).perform()
    Resource_dropdown2 = driver.find_element(By.XPATH,  HomePageElements.resource_drop2)
    Resource_dropdown2.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/news/"
    if driver.current_url == expected_url:
        print("Resources option 2 News click successfully and correct page open")
    else:
        print("Resources option 2 News not work")
resources_dropdown_click_button()
time.sleep(2)
driver.back()



#PF logo Clickable and redirect the homepage
def test_logo_click():
    button = driver.find_element(By.XPATH, HomePageElements.pf_logo)
    assert button.is_displayed(), "logo is visible on the page."
    button.click()
    assert "pf" in driver.current_url, "Redirect to home page failed."
    print("PF Logo click successfully and redirect the homepage")
test_logo_click()




#Life at PF Footer link is clickable and open correct page
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_life_at_pf)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    assert "life-at-pf" in driver.current_url, "Go to Life at PF page failed."
    print("Life at PF footer link click successfully and correct page loaded")
test_click_link()
time.sleep(2)
driver.back()



#Our Teammates link is clickable and open correct page
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_our_teammate)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    assert "about-us" in driver.current_url, "Go to our teammate page failed."
    print("Our Teammate footer link click successfully and correct page loaded")
test_click_link()
time.sleep(2)
driver.back()



#In House Privacy footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_in_house_privacy)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/privacypolicy/"
    if driver.current_url == expected_url:
        print("In House Privacy Policy footer link click successfully and correct page loaded")
    else:
        print("Go to Privacy Policy page failed")
test_click_link()
time.sleep(2)
driver.back()



#ISO Certifications footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_iso_certificates)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/iso_certified/"
    if driver.current_url == expected_url:
        print("ISO Certifications footer link click successfully and correct page loaded")
    else:
        print("Go to ISO certificate page failed.")
test_click_link()
time.sleep(2)
driver.back()



#Career footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_career)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/career/"
    if driver.current_url == expected_url:
        print("Career footer link click successfully and correct page loaded")
    else:
        print("Go to career page failed.")
test_click_link()
time.sleep(2)
driver.back()



#Job Positions footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_job_position)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Job Positions footer link click successfully and correct page loaded")
    else:
        print("Go to Job Positions page failed")
test_click_link()
time.sleep(2)
driver.back()



#Send Resume footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_send_resume)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/#popup1"
    if driver.current_url == expected_url:
        print("Send Resume footer link click successfully and correct page loaded")
    else:
        print("Go to Send Resume page failed")
test_click_link()
time.sleep(2)
driver.back()



#Track your Application footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_track_application)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Track your Application footer link click successfully and correct page loaded")
    else:
        print("Go to Track your Application page failed")
test_click_link()
time.sleep(2)
driver.back()



# Ransomware footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_ransomware)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/ransomware-year-beware-you-may-be-the-next-target/"
    if driver.current_url == expected_url:
        print("Ransomware footer link click successfully and correct page loaded")
    else:
        print("Go to Ransomware page failed")
test_click_link()
time.sleep(2)
driver.back()



# FinTech footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_fintech)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/social-impact-of-fintech-solution-in-pakistan/"
    if driver.current_url == expected_url:
        print("FinTech footer link click successfully and correct page loaded")
    else:
        print("Go to FinTech page failed")
test_click_link()
time.sleep(2)
driver.back()



#Life-Changing footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_life_changing)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/is-it-a-life-changing-industry/"
    if driver.current_url == expected_url:
        print("Life-Changing footer link click successfully and correct page loaded")
    else:
        print("Go to Life-Changing page failed")
test_click_link()
time.sleep(2)
driver.back()



#AI Career footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_ai_career)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/ai-career-paths-and-future-market-trends-in-ai/"
    if driver.current_url == expected_url:
        print("AI Career footer link click successfully and correct page loaded")
    else:
        print("Go to AI Career page failed")
test_click_link()
time.sleep(2)
driver.back()



#Apply Now Footer link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_apply_now)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Apply Now footer link click successfully and correct page loaded")
    else:
        print("Go to Apply now page failed")
test_click_link()
time.sleep(2)
driver.back()



#PF footer logo Clickable and redirect the homepage
def test_logo_click():
    button = driver.find_element(By.XPATH, HomePageElements.pf_footer_logo)
    assert button.is_displayed(), "logo is visible on the page."
    button.click()
    assert "pf" in driver.current_url, "Redirect to home page failed."
    print("PF footer Logo click successfully and redirect the homepage")
test_logo_click()



#Facebook Logo Link
def test_logo_click():
    try:
        facebook_image_link = driver.find_element(By.XPATH, HomePageElements.facebook_link)
        facebook_image_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Facebook open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()



#LinkedIn Logo Link
def test_logo_click():
    try:
        linkedin_image_link = driver.find_element(By.XPATH, HomePageElements.linkedin_link)
        linkedin_image_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("LinkedIn open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()



#Instagram Logo Link
def test_logo_click():
    try:
        insta_image_link = driver.find_element(By.XPATH, HomePageElements.insta_link)
        insta_image_link.click()

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Instagram Open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()




#Youtube Logo Link
def test_logo_click():
    try:
        youtube_link = driver.find_element(By.XPATH, HomePageElements.youtube_link)
        youtube_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("YouTube Open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()



#Privacy Policy link in last
def test_logo_click():
    button = driver.find_element(By.XPATH, HomePageElements.privacy_policy_last)
    assert button.is_displayed(), "logo is visible on the page."
    button.click()
    expected_url = "https://pf.com.pk/privacypolicy/"
    if driver.current_url == expected_url:
        print("Privacy policy footer link click successfully and correct page loaded")
    else:
        print("Go to Life-Changing page failed")
test_logo_click()
time.sleep(2)
driver.back()



#Flag Changing Option
def test_click_button():
    actions = ActionChains(driver)
    Flag_button = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div[1]")
    actions.move_to_element(Flag_button).perform()
    Flag_dropdown = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div[2]/p[2]")
    Flag_dropdown.click()
    driver.implicitly_wait(5)
    expected_url = "https://programmersforce.co.uk/"
    if driver.current_url == expected_url:
        print("UK flag selected")
    else:
        print("Option work")
test_click_button()