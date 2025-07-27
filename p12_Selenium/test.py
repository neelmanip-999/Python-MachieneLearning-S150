# Import the Selenium WebDriver module
from selenium import webdriver

# Import the time module to add delays in the script
import time

# Step 1: Launch the Chrome browser
# This line opens a new Chrome browser window using the default ChromeDriver in your PATH
driver = webdriver.Chrome()

# Step 2: Define the URL you want to open
url = "https://www.google.com"

# Step 3: Use the driver to open the specified URL
driver.get(url)  # Opens Google's homepage

# Step 4: Wait for 10 seconds
# This allows time for the page to load or for you to manually observe the page
time.sleep(10)

# Optional: Close the browser after waiting (not included in your code, but good practice)
driver.quit()  # Closes the browser and ends the WebDriver session
