from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
import os
import time

# this save starts in middle of cookie powerup:
# current_save = "Mi4wNDh8fDE2NTc0OTY2OTQ4NDg7MTY1NzQ5NjY5NDg0ODsxNjU4MjU4NDUyNzczO1NoaW55IFBhcnJvdDtjemt4ZXwxMTExMTEwMTEwMDEwMTEwMDEwMTAxMTAwMDF8Mjk5NTAyODk0NDk0Ny45NzQ7NTk3OTY1MTcyNTE1NjYuNjY0OzI3OTY2Nzs5ODsxNzcyMTY4MzU4Mzc5OS4xMDU7NTcxOzA7MDswOzA7MDswOzA7MDswOzk4OzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NzU7MDswOzI7ODsxNjU4MTk5MjkwOTI1OzA7MDs7NDE7MDswOzEwMjc3MTIzOTIuMTMzODc4Njs1MDt8MTY0LDE3Myw5NzU4MDk5Mjk1NTgsMywsMCwxNjQ7MTI3LDEyNywxMDM0OTg5ODY2MTYsMCwsMCwxMjc7MTAwLDEwMCwxNjMyNzcwMDM1NSwwLCwwLDEwMDs4Miw4MiwzMjYzNTczOTYyMCwwLCwwLDgyOzU3LDU3LDEwODQ2MTgzMzQwOCwwLCwwLDU3OzUyLDUyLDI0NDc5MzE4MDIzNCwwLCwwLDUyOzQ0LDQ0LDk2NjEzNzI5NDc0MiwwLCwwLDQ0OzM3LDM3LDM0ODQ2MjQxNzQ0NjYsMCwsMCwzNzsyNiwyNiw4ODQ3Nzc3MzMyNTkzLDAsLDAsMjY7MjIsMjIsMTA5ODEwNjkwNTIyMjEsMCwsMCwyMjs3LDcsMzc4NDI0NzI2MTg5NCwwLCwwLDc7MSwxLDE1NDk1MTUwNTcyMTksMCwsMCwxOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDt8MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDAxMTEwMDAxMDAwMDAxMTExMTExMTExMTExMTExMTExMTExMTEwMDExMTExMTExMDAwMDAwMDAxMTExMTAxMTExMTExMTExMTExMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMTEwMDExMTAwMDAwMDAwMDEwMDAxMDEwMTAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMTAxMDEwMDAwMDExMTEwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTExMDAwMDAxMTExMTEwMDAwMDAxMTExMTEwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfDExMTExMTExMDAwMDAwMDAxMTExMTExMTEwMDAwMDExMTExMTExMDAxMTExMTExMTAxMTAxMDAxMDAxMDAxMDAwMDAxMTEwMTExMTEwMTAwMDEwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMDAwMTAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMTAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8MCwyMzEwLDEyODQsNzt8%21END%21%21END%21"

link = "https://orteil.dashnet.org/cookieclicker"
DRIVER_PATH = os.getenv('DRIVER_PATH')  # your driver path

ser = Service(DRIVER_PATH)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.implicitly_wait(2)
driver.get(link)
english = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
english.click()
time.sleep(3)
cookie = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[15]/div[8]/button")

try:
    with open("current_save.txt", "r") as d:
        current_save = d.readlines()[0]

    get_options = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    get_options.click()
    time.sleep(2)
    get_import = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[2]")
    get_import.click()
    time.sleep(2)
    paste_save = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]/textarea")
    paste_save.send_keys(f"{current_save}{Keys.ENTER}")
    close_menu = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[1]")
    close_menu.click()

except FileNotFoundError:
    #at the start of a new game you need cookie clicks in ordr to unlock the golden cookie
    more_clicks = 'y'
    while more_clicks.capitalize() == 'Y':
        for i in range(500):
            cookie.click()
        more_clicks = input("Do you want 500 more clicks? type 'Y':")

##################catches cases where load starts with active cookie bonus: ##############################################

# try:
#     pie_timer = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[15]/div[7]/div/div')
#     golden_cookie_on = True
#     while golden_cookie_on:
#         for k in range(100):
#             cookie.click()
#         try:
#             pie_timer = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[15]/div[7]/div/div')
#         except NoSuchElementException:
#             golden_cookie_on = False
# except NoSuchElementException:
#     pass

##############################################################################################################

keep_going = True
while keep_going:
    # for i in range(1000):
    #     cookie.click()

    keep_clicking, golden_cookie_on = True, True
    ##check if user wants to end############################# (to end pull up the options tab and respond to console)
    try:
        get_export = driver.find_element(By.XPATH,
                                         "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
    except NoSuchElementException:
        pass
    else:
        want_end = input("would you like to end? Type 'Y' to stop: ")
        if want_end.capitalize() == "Y":
            keep_clicking, keep_going = False, False
        else:
            try:
                close_menu = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[1]")
                close_menu.click()
            except NoSuchElementException:
                pass

################################################################################################################

    while keep_clicking:

        try:
            golden_cookie = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/div")
            first_time = time.time()
            golden_cookie.click()

            while golden_cookie_on:
                for k in range(50):
                    cookie.click()
                try:
                    golden_cookie = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/div")
                    golden_cookie.click()
                except NoSuchElementException:
                    try:
                        pie_timer = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[15]/div[7]/div/div')
                    except NoSuchElementException:
                        golden_cookie_on = False
                        cookie.click()
        except NoSuchElementException:
            cookie.click()   ##keeps game thinking you are active to get more golden cookies
            keep_clicking = False
            time.sleep(3)

        except ElementClickInterceptedException:
            pass

#######################################################################################################

##Try loop catches situations where user X's out options tab before inputting want_end input:
try:
    get_export = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
    get_export.click()
    time.sleep(2)
except NoSuchElementException:
    get_options = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    get_options.click()
    time.sleep(2)
    get_export = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
    get_export.click()
    time.sleep(2)

text_of_save = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]/textarea")

with open("current_save.txt", "w") as d:
    data = d.write(text_of_save.text)
    print(data)
