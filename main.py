from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import DataInterac
import Settings
import MakeBotProfile
import ConfigParser
import sys
from MakeBotProfile import FacebookRegister
from Settings import LoadProfile
from Settings import ProxyChange
from Settings import SaveDeadProxy
from Settings import SaveProfile

"""driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://wwww.facebook.com")
email =  driver.find_element_by_id("email")
passw = driver.find_element_by_id("pass")
email.send_keys("hoangminh.le12302@gmail.com")
passw.send_keys("hoangminh12302")
time.sleep(0.5)
btn = driver.find_element_by_id("u_0_l")
btn.click()
time.sleep(0.5)
#setEnglish.setting(driver)
"""
"""name =  driver.find_element_by_class_name("_2s25")
img = driver.find_element_by_xpath(".//img").get_attribute("id")
id = img.split('_')[3]
print(id)
name.click()
driver.get("www.facebook.com/" + id + "/" + "about")
details.Overview(driver)"""
#sendFriendRq.sendRequest(driver)
#sendFriendRq.likeFanpage(driver)
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
name = config.get('folder_path','name')
img = config.get('folder_path','img')
path = config.get('folder_path','profile')
ip = config.get('folder_path','PROXY_HOST')
port = config.get('folder_path','PROXY_PORT')
print(name)
print(img)
print(path)
print(ip)
print(port)

#load and install pro5
pro5 = LoadProfile.loadFFPro5(path)
pro5 = ProxyChange.install_proxy(pro5,ip,port)
driver = webdriver.Firefox(firefox_profile=pro5)

#written by tuan
name = ["Nguyen", "Minh Thuy"] #last name, first name 
phone_number = sys.argv[1]
FacebookRegister.process(driver, name, phone_number)

#check weather pro5 was blocked
SaveDeadProxy.save_dead_proxy(driver, ip, port)

#save pro5 after finish registering 
SaveProfile.saveProfile(driver,path)
