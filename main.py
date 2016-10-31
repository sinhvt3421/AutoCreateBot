from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ConfigParser
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

#config parameter 
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
name = config.get('folder_path','name')
img = config.get('folder_path','img')
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
driver.get("http://www.facebook.com")

#written by tuan
name = ["Nguyen", "Thuy Linh"] #last name, first name 
phone_number = sys.argv[1]
FacebookRegister.process(driver, name, phone_number)
#   hoangminh.le12302@gmail.com
# hoangminh12302
time.sleep(120)
while(True):
    try:
        driver.find_element_by_class_name("_2s25")
        break
    except:
        SaveDeadProxy.save_dead_proxy(driver, ip, port)

        time.sleep(5)
        continue


#set english        
SetEnglish.setting(driver)
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
UpImage.upimage(driver,img,id)
#overview 
driver.get("wwww.facebook.com/" + id + "/about")
Details.Overview(driver)
time.sleep(4)
#like movies, music, etc
LikePage.do_like(driver,id)
time.sleep(3)
#first status
FirstStatus.upStatus(driver, img, caption)
time.sleep(2)
#send reques
SendFriendRqs.sendRequest(driver)
time.sleep(2)
SendFriendRqs.likePage(driver)
#save pro5 after finish registering 
SaveProfile.saveProfile(driver,path)

