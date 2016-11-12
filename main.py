from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import ConfigParser
import time
import sys
from DataInteract.BotInfo import BotInfo
from DataInteract import BotDB
from Settings import LoadProfile
from Settings import ProxyChange
from Settings import SaveDeadProxy
from Settings import SaveProfile
from Settings import SetEnglish
from MakeBotProfile import UpImage
from MakeBotProfile import LikePage
from MakeBotProfile import Details
from MakeBotProfile import SendFriendRqs
from MakeBotProfile import FacebookRegister
from MakeBotProfile import FirstStatus
#config parameter 

config = ConfigParser.SafeConfigParser()
config.read('config.ini')
name = config.get('folder_path','name')
image = config.get('folder_path','img')
caption = config.get('folder_path', 'caption')
path = config.get('folder_path','profile')
ip = config.get('folder_path','PROXY_HOST')
port = config.get('folder_path','PROXY_PORT')

#new bot
bot = BotInfo()
bot.ProxyIp = ip
bot.ProxyPort = port

#load and install pro5
pro5 = LoadProfile.loadFFPro5(path)
pro5 = ProxyChange.install_proxy(pro5,ip,port)
driver = webdriver.Firefox(firefox_profile=pro5)
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")

#written by tuan
name = [sys.argv[2], sys.argv[3]] #last name, first name 
phone_number = sys.argv[1]
FacebookRegister.process(driver, name, phone_number)
time.sleep(4)
#   hoangminh.le12302@gmail.com
# hoangminh12302
SaveDeadProxy.save_dead_proxy(driver, ip, port)
time.sleep(120)

#
# email = driver.find_element_by_id('email')
# passw = driver.find_element_by_id('pass')
# email.send_keys('hoangminh.le12302@gmail.com')
# passw.send_keys('hoangminh12302')
# loginbtn = driver.find_element_by_id('loginbutton')
# loginbtn.click()

while(True):
    try:
        driver.find_element_by_class_name("_2s25")
        break
    except:

        time.sleep(5)
        continue


#set english        
SetEnglish.setting(driver)
time.sleep(2)
#get id 
while(True):
    try:
        name =  driver.find_element_by_class_name("_2s25")
        img = driver.find_element_by_xpath(".//img").get_attribute("id")
        id = img.split('_')[3]
        name.click()
        driver.get("www.facebook.com/" + id)
        break
    except:
        continue

#up anh 
UpImage.upimage(driver,image,id)
time.sleep(2)
#overview 
driver.get("wwww.facebook.com/" + id + "/about")
time.sleep(1)
Details.Overview(driver)
time.sleep(4)
#like movies, music, etc
LikePage.do_like(driver,id)
time.sleep(3)
#first status
driver.get("www.facebook.com")
FirstStatus.upStatus(driver, image, caption)
time.sleep(2)
#send reques
# SendFriendRqs.sendRequest(driver)
time.sleep(2)
SendFriendRqs.likeFanpage(driver)
#save pro5 after finish registering 
#SaveProfile.saveProfile(driver,path)

