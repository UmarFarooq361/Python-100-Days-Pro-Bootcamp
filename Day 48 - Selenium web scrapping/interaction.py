from selenium import  webdriver
ChromeDriver = "D:\Development\chromedriver.exe"
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_executable = Service(executable_path= ChromeDriver, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# articles.click()
# print(articles.text)
# link = driver.find_element(By.LINK_TEXT,"content portals")
# link.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Umar farooq")
search.send_keys(Keys.ENTER)