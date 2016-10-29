import os, random
import time
from random import randint

def upStatus(drv, photo, cap):
        try:
            dir_path_photo = photo + random.choice(os.listdir(photo))
            dir_path_cap = cap + random.choice(os.listdir(cap))

            uploadImage = drv.find_element_by_name("composer_photo[]")
            uploadImage.send_keys(dir_path_photo)

            fileCaption = open(dir_path_cap, "r")
            writeCaption = drv.find_element_by_xpath("//*[@name='xhpc_message']")
            writeCaption.click()
            caption = fileCaption.read()
            writeCaption.send_keys(caption)

            time.sleep(10)
            postbutton = drv.find_element_by_xpath("//*[text()='Post']")
            postbutton.click()
        except:
            pass