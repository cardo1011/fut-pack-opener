from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# finds ALL the buttons on the page
def findButtons(xpath):
    return driver.find_elements(By.XPATH, xpath)

# This method should be called right after using the findButtons() in order to click on the desired button. 
# The function takes the list of button elements present on the page as the first parameter, and the
# string that should be found within the button that is intended to be clicked is the second parameter
def button_to_be_clicked(list_of_buttons: list, innerHTML_of_button: str):
    for button in list_of_buttons:
        if innerHTML_of_button in button.get_attribute('innerHTML'):
            button.click()
            return True
    print(f"No button found containing: {innerHTML_of_button}")
    return False

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
    print("\nReached login page!\n")
except:
    print("\nCouldn't reach login page :(\n")

# click Login button once it loads
buttons = driver.find_elements("xpath", "//button[text()='Login']")
buttons[0].click()

# waits at most 120 seconds for user to login into FUT web app before moving on with the script
try:
    element = WebDriverWait(driver, 180).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'title'))
    )
    print("\nReached home page!\n")
except:
    print("\nTimed out waiting for the home page to load...\n")

# finds all the button elements on the home page that are children of a nav element and clicks on the button with the text that contains "Store"
home_buttons = findButtons('//nav/button')
button_to_be_clicked(home_buttons, "Store")

# Wait for the store to load and then clicks on the "Packs" tile
try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]")))
    driver.find_element(By.XPATH, "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]").click()
    print("\nClicked on \"Packs\" tile\n")
except:
    print("\nTimed out waiting for packs tile to load\n")

try:
    # searches for all buttons that would open a new pack to know if there are any packs that could be opened
    packs = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]")))
except:
    print("\nTimed out waiting for the button to open a pack to be clickable\n")

# while there are buttons that should open a new pack, the following code will execute
while packs: 
# clicks on the "Open Pack" button to open the first pack on the page
    driver.find_elements(By.XPATH, "//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]")[0].click()
    print("\nOpening a new pack!")

    #give time for the pack opening animation to play out 
    time.sleep(8)

    # quick sell all contents of pack that are under the H2 that contains the string "Duplicates"
    if driver.find_elements(By.XPATH, "//h2[contains(normalize-space(), 'Duplicates')]"):
        ellipsis_btn = driver.find_element(By.XPATH, "//h2[contains(text(), 'Duplicates')]/ancestor::header//button[contains(@class, 'ellipsis-btn')]")
        ellipsis_btn.click()

        # quick sell all duplicate contents of the pack
        quick_sell_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[@class='btn-text currency-coins' and contains(text(), 'Quick Sell')]]")))
        quick_sell_button.click()

        # confirm choice to quick sell all duplicate contents of the pack
        time.sleep(1)
        ok_btns = findButtons('//button')
        button_to_be_clicked(ok_btns, "Ok")

    # check to see if there are any remaining contents in the pack that need to be stored in club
    if driver.find_elements(By.XPATH, "//button[contains(@class, 'ellipsis-btn')]"):

        # clicks on ellipsis button in the pack to handle the contents of the pack
        ellipsis_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'ut-image-button-control') and contains(@class, 'ellipsis-btn')]")
        ellipsis_btn.click()

        #clicks button to store all contents of 
        time.sleep(1)
        store_in_club_btns = findButtons('//button')
        button_to_be_clicked(store_in_club_btns, "Store All in Club")

    time.sleep(2)
    pack_items_cleared = driver.find_elements(By.XPATH, "//h2[normalize-space()='You have no unassigned items.']")

    # if there are no more contents in the pack that need to be dealth with, the script will 
    # navigate to the store via the nav bar on the left and the Store button
    if pack_items_cleared:
        home_buttons = findButtons('//nav/button')
        button_to_be_clicked(home_buttons, "Store")

    # Wait for the store to load and then clicks on the "Packs" tile
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]")))
    driver.find_element(By.XPATH, "//div[contains(@class, 'packs-tile') and contains(@class, 'tile')]").click()
        
    # update packs to reflect the new amount of packs to be opened before the next iteration condition check 
    try:
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]"))
        )
    except:
        print("No more packs found. Ending loop.")
        break

    packs = findButtons("//button[contains(@class, 'currency') and contains(@class, 'call-to-action')]")


