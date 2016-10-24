#Register new account. Name from database. Phone from keyboard
#Return birthday and account id to database 
#Created by Tuan

from selenium import webdriver
from random import randint
import sys
import time

#exmaple. Real info will take from database

birthday = [] #dd mm yyyy format
custom_id = 0

#fill text
def fillName(drv, keys, name):
    text_space = drv.find_element_by_name(name)
    text_space.click()
    text_space.send_keys(keys)
    #time.sleep(1)

#select birthday
def fillDate(drv, keys, indext):
    button = drv.find_element_by_id(indext)
    button.click()
    all_options = button.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("value") == str(keys):
            #print(option.get_attribute("value"))
            option.click()
            #time.sleep(1)
            break

def process(driver, name, phone_number):
    #name is a list of string
    #driver is a webdirver of firefox

    #fill name
    driver.get("http://www.facebook.com")
    fillName(driver, name[1], "firstname")
    fillName(driver, name[0], "lastname")
    fillName(driver, "InfoRe2811", "reg_passwd__")
    fillName(driver, str(phone_number), "reg_email__")
    fillName(driver, str(phone_number), "reg_email_confirmation__")

    #fill birthday
    month = randint(1, 12) 
    fillDate(driver, month, "month")
    day = randint(1, 28)
    fillDate(driver, day, "day")
    year = randint(1996, 1998)
    #year = 2016
    fillDate(driver, year, "year")
    birthday.append([day, month, year]) #return to database

    #fill gender
    gender = driver.find_element_by_name("sex")
    gender.click()
    #time.sleep(1)

    #finish
    complete_reg = driver.find_element_by_name("websubmit")
    complete_reg.click()

    return birthday
    #not yet get id
    #custom_id = 0 





