from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open Flipkart
driver.get("https://www.flipkart.com")
 
# Close login popup
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass
time.sleep(2)

# Search for mobiles
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Mobiles')
time.sleep(1)
search_box.submit()
time.sleep(3)

# Loop through 10 pages
all_mobiles = []
all_prices = []
all_ratings=[]

for page in range(1, 16):
    print(f"\n--- Page {page} ---")

    time.sleep(3)

    # Wait for products to load
    mobiles = driver.find_elements(By.CSS_SELECTOR, "div.KzDlHZ")  # Product names
    prices = driver.find_elements(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR")  # Product prices
    ratings = driver.find_elements(By.CSS_SELECTOR, "div.XQDdHH")  # Product rating


    for phone, price, rating in zip(mobiles, prices,ratings):
        name = phone.text.strip()
        price_text = price.text.strip()
        ratin=rating.text.strip()
        print(f"{name} ---> {price_text}-->{ratin}")
        all_mobiles.append(name)
        all_prices.append(price_text)
        all_ratings.append(ratin)

    # Go to next page
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, '_9QVEpD') and span[text()='Next']]")
        driver.execute_script("arguments[0].click();", next_button)
    except Exception as e:
        print("No more pages found or error occurred:", e)
        break


# Close the browser
driver.quit()

# Optionally save to CSV
import pandas as pd
df = pd.DataFrame({
    "Mobile Name": all_mobiles,
    "Price": all_prices,
    "Rating":all_ratings
})
df.to_csv("flipkart_mobiles.csv", index=False)
df.to_excel("flipkart_mobiles.xlsx", index=False)

print(df)

# //*[@id="container"]/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]/span