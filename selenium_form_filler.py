from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()
file_path = os.getenv("FILE_PATH")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("johndoe@email.com")

male_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
male_label.click()

mobile_field = driver.find_element(By.ID, "userNumber")
mobile_field.send_keys("1234567890")

dob_field = driver.find_element(By.ID, "dateOfBirthInput")
dob_field.clear()
dob_field.send_keys("01 Jan 2000")

subjects_input_field = driver.find_element(By.ID, "subjectsInput")
subjects_input_field.send_keys("Maths")
time.sleep(1)

math_option = driver.find_element(By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and text()='Maths']")
math_option.click()
subjects_input_field.send_keys(Keys.ENTER)

checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")
driver.execute_script("arguments[0].click();", checkbox)

upload_element = driver.find_element(By.ID, "uploadPicture")
upload_element.send_keys(file_path)

address_field = driver.find_element(By.ID, "currentAddress")
address_field.send_keys("123 Main St, Springfield")

state_dropdown_opener = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].click();", state_dropdown_opener)
time.sleep(1)

state_option_ncr = driver.find_element(By.XPATH, "//div[contains(@id, 'react-select') and text()='NCR']")
state_option_ncr.click()

city_dropdown_opener = driver.find_element(By.ID, "city")
driver.execute_script("arguments[0].click();", city_dropdown_opener)
time.sleep(0.5)

city_option_delhi = driver.find_element(By.XPATH, "//div[contains(@id, 'react-select') and text()='Delhi']")
city_option_delhi.click()

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

time.sleep(5)
driver.quit()