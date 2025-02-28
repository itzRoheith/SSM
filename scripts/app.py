from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Website URL (with authentication)
URL = "https://ssmetrust.in/SSM63/Parent_portal/parent_publish/circularboostrs.aspx?admno=1979&pwd=Sanjeev&year=2024-25"

# Configure Selenium to use headless mode (no UI)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the page
driver.get(URL)
time.sleep(3)  # Wait for JavaScript to load

# Find all PDF links
pdf_links = []
elements = driver.find_elements(By.TAG_NAME, "a")  # Find all <a> tags
for elem in elements:
    href = elem.get_attribute("href")
    if href and href.endswith(".pdf"):
        pdf_links.append(href)

# Close the browser
driver.quit()

# Print extracted PDF links
print("Extracted PDF Links:", pdf_links)

# Save to a file (if needed)
with open("pdf_links.txt", "w") as f:
    for link in pdf_links:
        f.write(link + "\n")
