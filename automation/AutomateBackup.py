import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


username = "testemail@gmail.com"

chromedriver = "C:/windows/chromedriver.exe"
driver = webdriver.Chrome(chromedriver) 
driver.get("https://onedrive.live.com/about/en-us/signin/")

wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"SignIn")))

email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.form-group > input.form-control")))
email.send_keys("test@etst.test")


# user = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/div[2]/div/input"))
user.send_keys(username)