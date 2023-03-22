from selenium import  webdriver
ChromeDriver = "D:\Development\chromedriver.exe"
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_executable = Service(executable_path= ChromeDriver, log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# for time in event_times:
#     print(time.text)
events_location = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
# for ev in events:
#     print(ev.text)
event= {}
for n in range(len(event_times)):
    event[n] = {
        "time": event_times[n].text,
        "location": events_location[n].text
    }
print(event)



# driver = webdriver.Chrome(executable_path= ChromeDriver)
# driver.get("https://www.amazon.com/")
# driver.get("https://www.amazon.com/dp/B01NBKTPTS/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B01NBKTPTS&pd_rd_w=XeB0I&")
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# print(myDiv.get_attribute("outerHTML"))
# print(price.text)
# title = driver.find_element(By.ID,"productTitle")
# title = driver.find_element(By.XPATH,"path")
# print(title.text)
# driver.close()
driver.quit()
