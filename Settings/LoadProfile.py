from selenium import webdriver

#load profile from folder and return profile
#path is the profile's link Eg: '/media/cloud/Work/InfoRe/test_profile'
def loadFFPro5(path):
    pro5 = webdriver.FirefoxProfile(path)
    return pro5