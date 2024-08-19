from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

option = Options()
#option.headless = True  # Enable headless mode
option.add_argument("--window-size=1920,1200")  # Set the window size


#service = Service(executable_path='chromedriver.exe')


driver = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element("name","q")
elem.send_keys("python")
elem.send_keys(Keys.RETURN)

elements = driver.find_elements("xpath","//*[h3]")
data = [element.text for element in elements]
print (data)
driver.close()

print ('dddd')