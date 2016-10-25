from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from MakeBotProfile import FacebookRegister
from Settings import LoadProfile
from Settings import ProxyChange
from Settings import SaveDeadProxy
from Settings import SaveProfile
from Settings import SetEnglish
from MakeBotProfile import UpImage
from MakeBotProfile import LikePage
from MakeBotProfile import Details
from MakeBotProfile import SendFriendRqs
from LikePage import do_like
from FirstStatus import upStatus
# config = ConfigParser.SafeConfigParser()
# config.read('config.ini')
# name = config.get('folder_path','name')
# img = config.get('folder_path','img')
# caption = config.get('folder_path', 'caption')
# path = config.get('folder_path','profile')
# ip = config.get('folder_path','PROXY_HOST')
# port = config.get('folder_path','PROXY_PORT')

#load and install pro5
# pro5 = LoadProfile.loadFFPro5(path)
# pro5 = ProxyChange.install_proxy(pro5,ip,port)
# driver = webdriver.Firefox(firefox_profile=pro5)
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
#written by tuan
# name = ["Nguyen", "Minh Thuy"] #last name, first name 
# phone_number = sys.argv[1]
# FacebookRegister.process(driver, name, phone_number)
# hoangminh.le12302@gmail.com
# hoangminh12302
while(True):
    try:
        driver.find_element_by_class_name("_2s25")
        break
    except:
        time.sleep(5)
        continue
        
#set english        
# SetEnglish.setting(driver)
#get id 
while(True):
    try:
        name =  driver.find_element_by_class_name("_2s25")
        img = driver.find_element_by_xpath(".//img").get_attribute("id")
        id = img.split('_')[3]
        name.click()
        driver.get("www.facebook.com/" + id + "/" + "about")
        break
    except:
        continue

Details.Overview(driver)

#check weather pro5 was blocked
# SaveDeadProxy.save_dead_proxy(driver, ip, port)

#save pro5 after finish registering 
# SaveProfile.saveProfile(driver,path)

#like movies, music, etc
#do_like(driver)

#first status
#upStatus(driver, img, caption)