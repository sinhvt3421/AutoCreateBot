import os
from selenium import webdriver
import sys
import tarfile

#save and compress firefox profile after finish running
#driver is the current driver used for running
#path is the profile's link used for load profile
#Eg: '/media/cloud/Work/InfoRe/test_profile'
# *.tar.gz file store at the same folder as main classy
def saveProfile(driver,path):
    pro5 = driver.firefox_profile.path #get the temporary pro5's path
    os.system("cp -R " + pro5 + "/* " + path ) #overwrite pro5
    #compress pro5
    with tarfile.open( os.path.basename(path) + ".tar.gz", "w:gz" ) as tar:
        tar.add(path, arcname=os.path.basename(path))

