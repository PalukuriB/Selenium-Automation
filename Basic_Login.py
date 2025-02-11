from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

while True:
    try:
        Browser = input("Enter which browser you want (e.g., Chrome or Edge): ")

        if not Browser.isalpha():
            raise ValueError("Please give only string text, not numbers or decimals.")

        if Browser not in ['Chrome', 'Edge']:
            raise ValueError("Invalid browser choice. Please enter 'Chrome' or 'Edge'.")

        break  # If everything is fine, exit the loop

    except ValueError as e:
        print(e) 


if Browser == 'Chrome':

    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


if Browser == 'Edge':

    from selenium.webdriver.edge.service import Service as EdgeService
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

SauceDemo = driver.get("https://www.saucedemo.com/")
sleep(3)

Maximize_screen = driver.maximize_window()
sleep(2)

username = driver.find_element(By.XPATH, "//input[contains(@id, 'user')]").send_keys('visual_user')
sleep(3)

password = driver.find_element(By.XPATH, "//input[contains(@id, 'pass')]").send_keys('secret_sauce')
sleep(3)

login_button = driver.find_element(By.XPATH, "//input[contains(@id, 'login')]").click()
sleep(3)

Tshirt = driver.find_element(By.XPATH, "//button[contains(@data-test, 't-shirt')]").click()
sleep(2)

# Scroll down the page after login
driver.execute_script("window.scrollBy(0, 300);")  # Adjust the number if you need to scroll more
sleep(2)

Jacket = driver.find_element(By.XPATH, " //button[contains(@data-test, 'jacket') and contains(., 'Add')]").click()
sleep(3)

cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
sleep(4)

cart_quantity = driver.find_element(By.XPATH, "//*[contains(@class, 'badge')]").text
print(cart_quantity)

check_out = driver.find_element(By.NAME, 'checkout').click()
sleep(5)

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Bhashwanth')
sleep(2)

Last_name = driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys('Palukuri')
sleep(2)

pincode = driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys('523001')
sleep(3)

# Scroll down the page after login
driver.execute_script("window.scrollBy(0, 900);")  # Adjust the number if you need to scroll more
sleep(2)

done = driver.find_element(By.XPATH, "//*[@id='continue']").click()
sleep(5)

tax = driver.find_element(By.CLASS_NAME, 'summary_tax_label').text
print("Products (GST and CGST)", tax)
total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text 
print("Total Amount", total)

# Scroll down the page after login
driver.execute_script("window.scrollBy(0, 1000);")  # Adjust the number if you need to scroll more
sleep(2)

Finish = driver.find_element(By.XPATH, "//*[@id='finish']").click()
sleep(5)

placed_order = driver.find_element(By.XPATH, "//*[ text()='Thank you for your order!']").text
print(placed_order)

back_home = driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()
sleep(5)

refreshing_page = driver.refresh()
sleep(2)

driver.execute_script("window.scrollBy(0, -1000);")  # Scroll up by 1000 pixels (negative value)
sleep(2)

menu_button = driver.find_element(By.ID, 'react-burger-menu-btn').click()
sleep(2)

Logout = driver.find_element(By.LINK_TEXT, 'Logout').click()
sleep(3)

print("Logged out successfully")

driver.close()

