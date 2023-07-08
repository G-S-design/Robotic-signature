from selenium import webdriver
import time
import requests

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Use appropriate WebDriver for your browser

# Open the Signature Generator website
driver.get("https://signature-generator.com/")

# Prompt the user to enter a name
name = input("Enter a name for the signature: ")

# Find the input field and submit the name
input_element = driver.find_element_by_css_selector('input[name="name"]')
input_element.send_keys(name)

# Wait for the signature to generate
time.sleep(3)  # Adjust the wait time if necessary

# Find the download link
download_link = driver.find_element_by_link_text("Download")

# Get the URL of the generated image
image_url = download_link.get_attribute("href")

# Download the image file
response = requests.get(image_url)
filename = "generated_signature.png"  # Specify the desired filename
with open(filename, "wb") as f:
    f.write(response.content)

# Close the WebDriver
driver.quit()

print(f"The signature image has been downloaded as '{filename}'.")
