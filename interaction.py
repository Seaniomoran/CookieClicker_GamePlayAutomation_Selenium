from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


ser = Service(r"C:\Users\Sean\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://python.org")
elements = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.split("\n")
driver.close()

b = 1
events = {}
for i in range(int(len(elements)/2)):
    events[i] = {
        "time": elements[i],
        "name": elements[b],
    }
    b += 1
print(events)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
element = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# driver.close()
print(element)

all_portals = driver.find_element(By.LINK_TEXT, 'About Wikipedia')
all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys(f"Super{Keys.ENTER}")

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

fname.send_keys("Sean")
lname.send_keys("Moran")
email.send_keys(f"seanio@gmail.com{Keys.ENTER}")
