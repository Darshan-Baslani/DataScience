from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver executable
webdriver_service = Service('path/to/chromedriver')

# Launch the browser
driver = webdriver.Chrome(service=webdriver_service)
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="app"]')))

# Function to search for a person in the contacts
def search_contact(contact_name):
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    search_box.clear()
    search_box.send_keys(contact_name)
    # Wait for the search results to load
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="search"]')))
    # Perform any additional actions with the search results if needed

# Example usage
contact_name = "John Doe"
search_contact(contact_name)

# Close the browser
driver.quit()

