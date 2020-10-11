import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

user = sys.argv[1]
passw = sys.argv[2]

chromedriver = "C:/windows/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
NEXTBUTTON = (By.ID, "idSIButton9")
driver.get("https://portal.office365.com")

username = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("i0116"))
username.send_keys(user)

NEXTBUTTON = (By.ID, "idSIButton9")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

password = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("i0118"))
password.send_keys(passw)

NEXTBUTTON = (By.ID, "idSIButton9")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()


AfterLog = (By.ID, "idSubmit_ProofUp_Redirect")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AfterLog)).click()


SelectDropdown = (By.ID, "PreferredOptionProofList")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SelectDropdown)).click()

#SwitchDropDown = (By.Value, "PhoneAppNotification")
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SwitchDropDown)).click()
