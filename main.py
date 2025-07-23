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

# wait for the "Login" button to load and be clickable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
    )
    print("Reached login page!")
except:
    print("Couldn't reach login page :(")

# click Login button once it loads
buttons = driver.find_elements("xpath", "//button[text()='Login']")
buttons[0].click()

# waits at most 120 seconds for user to login into FUT web app before moving on with the script
try:
    element = WebDriverWait(driver, 180).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'title'))
    )
    print("Reached home page!")
except:
    print("Timed out waiting for the home page to load...")

# finds all the button elements that are children of a nav element
home_buttons = driver.find_elements(By.XPATH, "//nav/button")

# iterate through the elements of home_buttons to find the "Store" button and click on it when found 
for button in home_buttons:
    if "Store" in button.get_attribute('innerHTML'):
        button.click()
        print("Store button clicked")

# Wait for the store to load and give us the tile that shows if there is any "Unassigned items"
items_tile = driver.find_elements(By.XPATH,  "//div[contains(@class, 'ut-unassigned-tile-view') and contains(@class, 'tile')]")
# wait for the "unassigned items tile to appear"
time.sleep(5)
# clicks on the unassigned items tile
items_tile[0].click()
