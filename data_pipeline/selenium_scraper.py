# THIS IS FOR TESTING STUFF
# ONLY MIGRATE TO REDDIT_SCRAPER.PY IF IT WORKS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome (non-headless for this demo)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Go to Google
    driver.get("https://www.google.com")

    # Step 2: Accept cookies if needed (optional)
    try:
        agree_button = driver.find_element(By.XPATH, '//button[contains(text(), "Accept")]')
        agree_button.click()
    except:
        pass  # No cookie prompt

    # Step 3: Enter search query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("charmander")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Wait for results to load
    time.sleep(2)

    # Step 5: Click the first result
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    first_result.click()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Optional: keep browser open for inspection
    time.sleep(10)
    driver.quit()
