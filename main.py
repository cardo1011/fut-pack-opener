from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def findButtons(xpath):
    return driver.find_elements(By.XPATH, xpath)

def button_to_be_clicked(list_of_buttons: list, innerHTML_of_button: str):
    for button in list_of_buttons:
        if innerHTML_of_button in button.get_attribute('innerHTML'):
            button.click()
            return
    print(f"No button found containing: {innerHTML_of_button}")

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

# finds all the button elements on the home page that are children of a nav element and clicks on the button with the text that contains "Store"
home_buttons = findButtons('//nav/button')
button_to_be_clicked(home_buttons, "Store")

# Wait for the store to load and give us the tile that shows if there is any "Unassigned items"
packs_tile = driver.find_element(By.XPATH,  "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]")

time.sleep(5)
# clicks on the Packs tile
packs_tile.click()

time.sleep(3)

packs = findButtons("//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]")

while packs:
    # opens pack
    packs[0].click()

    time.sleep(10)

    # clicks on ellipsis button in the pack to handle the contents of the pack
    ellipsis_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'ut-image-button-control') and contains(@class, 'ellipsis-btn')]")
    ellipsis_btn.click()

    time.sleep(3)
    #clicks button to store all contents of 
    store_in_club_btns = findButtons('//button')
    button_to_be_clicked(store_in_club_btns, "Store All in Club")

    time.sleep(3)
    # If there are duplicate items that can't be stored, we will quick sell them
    ellipsis_btns = driver.find_elements(By.XPATH, "//button[contains(@class, 'ellipsis-btn')]")

    if ellipsis_btns:
        ellipsis_btn = ellipsis_btns[0]
        ellipsis_btn.click()

        time.sleep(1)
        quick_sell_duplicates_btns = findButtons('//button')
        button_to_be_clicked(quick_sell_duplicates_btns, "Quick Sell")

        ok_btns = findButtons('//button')
        button_to_be_clicked(ok_btns, "Ok")

    time.sleep(3)
    pack_items_cleared = driver.find_elements(By.XPATH, "//h2[normalize-space()='You have no unassigned items.']")

    if pack_items_cleared:
        home_buttons = findButtons('//nav/button')
        button_to_be_clicked(home_buttons, "Store")


    # must check if any duplicate items or items that can't be sent to the still need to be either quick sold or delt with
    # if len(driver.find_elements(By.TAG_NAME, 'li')) > 0:
    #         # click ellipsis button to quick sell everything 
    #         ellipsis_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'ut-image-button-control') and contains(@class, 'ellipsis-btn')]")
    #         ellipsis_btn.click()

    #         time.sleep(3)
            
    #         quick_sell_btns = findButtons("//button[.//span[contains(text(), 'Quick Sell untradeable iteqms for')]]")
    #         quick_sell_btns[0].click()

    #         ok_btns = findButtons('//button')
    #         button_to_be_clicked(ok_btns, "Ok")
    # click on the store button again once all contents of pack have been sent to the club

    # click on the packs tile to in order to click on the next pack to open
    packs_tile = driver.find_element(By.XPATH,  "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]")
    time.sleep(5)
    # clicks on the Packs tile
    packs_tile.click()
      
    # update packs to reflect the new amount of packs to be opened before the next iteration condition check 
    packs = findButtons("//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]")


