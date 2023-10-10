from selenium import webdriver

# Initialize WebDriver (Assuming you're using Chrome)
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://booking.octopuspro.com/login?logout=1")

# Locate and fill in the username and password fields
username = driver.find_element("name", "email")  # Use ("name", "uid") instead of find_element_by_name
password = driver.find_element("name", "password")

username.send_keys("abdelrahman.mogebril@gmail.com")  # Enter valid UserId
password.send_keys("A123456!")     # Enter valid Password

# Locate and click the login button
login_button = driver.find_element("id", "subNewAccount")
login_button.click()

# Check if login was successful (assuming there's a welcome message or some indicator)
# welcome_message = driver.find_element("xpath", "//marquee[@class='heading3']")
# if welcome_message.text == "Welcome To Manager's Page of Guru99 Bank":
#     print("Login Successful")
# else:
#     print("Login Failed")

# Perform some actions after successful login (e.g., Logout)

# Locate and click the logout link
logout_link = driver.find_element("partial link text", "Log out")
logout_link.click()

# Close the browser
driver.quit()
