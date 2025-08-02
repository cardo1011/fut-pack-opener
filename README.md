FUT Pack Opener Automation (Selenium Script)
This Python script automates the process of logging into the EA Sports FC Ultimate Team (FUT) web app and opening available packs. It is designed to handle duplicates, store items in the club, and loop through all available packs until none remain.

## 📋 Features

- Opens Chrome browser and navigates to the FUT Web App.

- Waits for user login manually (up to 3 minutes).

- Navigates to the Store section.

- Opens available packs.

- Handles duplicates via quick sell.

- Stores remaining items in the club.

- Repeats the process until all packs are opened.

## 🚀 Getting Started

**Prerequisites**
Ensure you have the following installed:

- Python 3.7+

- Google Chrome

- ChromeDriver (automatically handled by webdriver-manager)

Ensure you know your EA login information (that includes your password)

**Install Dependencies**
"pip install selenium webdriver-manager"
copy and paste command into terminal to download selenium

**How to Use**

1. Clone this repository or copy the script locally.

2. Run the script: "python main.py" (copy paste this command into your terminal or hit the run button in your IDE)

3. Log in manually when the FUT Web App login page opens. The script does not store your email address or password.

4. The script will take over and begin opening your packs automatically.

## Script Flow

1. Launch Chrome using Selenium and navigate to the FUT Web App.

2. Wait for the "Login" button, click it, and pause for the user to log in.

3. Once logged in, navigate to the Store and click the "Packs" tile.

4. For each pack:

- Open the pack.

- Wait for the animation.

- Quick sell duplicates, if any.

- Store remaining items in the club.

5. Repeat until there are no more packs left.

🛑 Notes

- The user must manually log into their FUT account after clicking the "Login" button. This is intentional, in order to avoid security concerns of anybody that may use the script

- A delay (time.sleep()) is used to allow animations to finish. You can adjust timing for faster or slower automation depending on system/browser speed. Simply change the number in between the two parenthesis to whatever amount of seconds you want the script to stall.

- If there is a welcome message from EA when first logging in, the script will crash. If encountered with this scenario, simply copy and paste the following commands (without the quotation marks) into your terminal one at a time and hit "enter" after pasting each command into your terminal:

1. "clear"
2. "python3 main.py"

You will have to login again. To avoid this anytime when using the script, log in before running the script and clear all welcome messages from EA and then run the script

🧠 Tips

- The script will crash if any draft token packs, player picks, or coin packs are opened since the script is not written to handle those scenarios. If encountered with this scenario, simply copy and paste the following commands (without the quotation marks) into your terminal one at a time and hit "enter" after pasting each command into your terminal:

1. "clear"
2. "python3 main.py"

- You will have to login again.

# ATTENTION

- The script does not save ANY duplicates. It does not matter if you pack a 99 overall or a -99 overall, the script will ALWAYS quick sell duplicates. Otherwise it will store any new contents to the club

🛠️ Tech Stack
Python

Selenium WebDriver

ChromeDriver (via webdriver-manager)
