from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Open Yahoo Search
driver.get("https://in.search.yahoo.com/")
time.sleep(2)

# Step 2: Search "Hello World"
search_box = driver.find_element(By.NAME, "p")
search_box.send_keys("Hello World")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Step 3: Scroll down to load more results
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Step 4: Scrape titles and links
results = driver.find_elements(By.CSS_SELECTOR, "h3.title a")
data = []

for result in results:
    title = result.text
    link = result.get_attribute("href")
    data.append({"Title": title, "Link": link})

# Close browser
driver.quit()

# Step 5: Save to CSV and Excel
df = pd.DataFrame(data)
df.to_csv("yahoo_search_results.csv", index=False)
df.to_excel("yahoo_search_results.xlsx", index=False)

print("✅ Exported to:")
print("  • yahoo_search_results.csv")
print("  • yahoo_search_results.xlsx")
