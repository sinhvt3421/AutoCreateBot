#Register new account. Name from database. Phone from keyboard
#Return birthday to the database 
#Created by Tuan

from selenium import webdriver
from random import randint
import sys
import time

birthday = [] #dd mm yyyy format
custom_id = 0

def fillName(drv, keys, name):
    text_space = drv.find_element_by_name(name)
    text_space.click()
    text_space.send_keys(keys)
    time.sleep(2)

def fillDate(drv, keys, indext):
    button = drv.find_element_by_id(indext)
    button.click()
    all_options = button.find_elements_by_tag_name("option")
    time.sleep(2)
    for option in all_options:
        if option.get_attribute("value") == str(keys):
            option.click()
            break

def process(driver, name, phone_number):
    driver.get("http://www.facebook.com")
    
    year = randint(1996, 1998)
    fillDate(driver, year, "year")
    month = randint(1, 12) 
    fillDate(driver, month, "month")
    day = randint(1, 28)
    fillDate(driver, day, "day")
    time.sleep(1)
    
    birthday.append([day, month, year])

    fillName(driver, name[1], "firstname")
    fillName(driver, name[0], "lastname")
    fillName(driver, "InfoRe2811", "reg_passwd__")
    fillName(driver, str(phone_number), "reg_email__")
    fillName(driver, str(phone_number), "reg_email_confirmation__")

    gender = driver.find_element_by_name("sex")
    gender.click()
    time.sleep(1)
    #finish
    try:
        complete_reg = driver.find_element_by_name("websubmit")
        complete_reg.click()
    except:
        pass
    



