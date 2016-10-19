import os 
import time

def upStatus(drv):
    #make 2 folder: "photos" and "captions" 
    picname = "cartoon-duck-free.png"
    piccap = "0.txt"
    dir_path_name = os.path.dirname(os.path.realpath("photos/" + picname))
    dir_path_cap = os.path.dirname(os.path.realpath("captions/" + piccap))
    uploadImage = drv.find_element_by_name("composer_photo[]")
    uploadImage.send_keys(dir_path_name + "/" + picname)
    fileCaption = open(dir_path_cap + "/" + piccap, "r")
    writeCaption = drv.find_element_by_xpath("//*[@name='xhpc_message']")
    writeCaption.click()
    caption = fileCaption.read()
    writeCaption.send_keys(caption)
    time.sleep(10)
    postbutton = drv.find_element_by_xpath("//*[text()='Post']")
    postbutton.click()