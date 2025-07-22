from selenium import webdriver
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

time.sleep(4)

buttons = driver.find_elements("xpath", "//button")
buttons[0].click()




