from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# opens the FUT web app home page where there is just a button that says "login"
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")
driver.maximize_window()

# wait for the "Login" button to load 
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
    )
    print("Reached login page!")
except:
    print("Couldn't reach login page :(")

# click Login button once it loads
buttons = driver.find_elements("xpath", "//button[text()='Login']")
buttons[0].click()

# wait for user to login into FUT web app
try:
    element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
    )
    print("Reached home page!")
except:
    print("Timed out waiting for the home page to load...")

