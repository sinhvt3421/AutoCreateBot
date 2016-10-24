from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import os,sys
import time

list_school = ["cau giay","su pham","tat thanh","duy tu","nguyen hue","quang trung","minh khai","luong the","kim lien","chu van"]  
about_you = ["","I'm so lonely <3","cha co gi dac sac","funny, lovely and love my life","want to chat with someone","so crazy with you ^^","so sad, so disapointed,... =(("]
nick_name = ["Cookie","Cun","Gau","Kute","Lonely","Ngay ngo","Nothing","meo meo","","So friendly","Waiting","Rainny","Miley","Socola"]

def Overview(drv):
    all_detail = drv.find_elements_by_xpath("//ul[@data-testid='info_section_left_nav']/li")
    #high school
    """all_detail[1].click()
    time.sleep(0.5)
    drv.execute_script("window.scrollTo(0,90)")
    high_school = drv.find_element_by_xpath("//a[@data-testid='add_highschool']")
    high_school.click()
    time.sleep(2)
    school = drv.find_element_by_xpath("//div/input[@name='school_text']")
    school.click()
    sch = list_school[randint(0, 9)]
    school.send_keys(sch)
    time.sleep(0.5)
    school.send_keys(Keys.DOWN)
    time.sleep(0.2)
    school.send_keys(Keys.ENTER)
    time.sleep(1)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    print(submit.get_attribute("innerHTML"))
    submit.submit()
    
    #place
    all_detail[2].click()
    time.sleep(0.5)
    current_city =  drv.find_element_by_xpath("//a[@data-testid='add_current_city']")
    current_city.click()
    time.sleep(2)
    city =  drv.find_element_by_xpath("//div/input[@class='inputtext textInput']")
    time.sleep(0.1)
    city.click()
    time.sleep(0.1)
    city.send_keys("japan")
    time.sleep(1)
    ran = randint(2,6)
    for i in range(0, ran):
        city.send_keys(Keys.DOWN)
        time.sleep(0.2)
    city.send_keys(Keys.ENTER)
    time.sleep(0.5)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    submit.submit()

    time.sleep(1)
    home_town = drv.find_element_by_xpath("//a[@data-testid='add_hometown']")
    home_town.click()
    time.sleep(2)
    home = drv.find_element_by_xpath("//div/input[@class='inputtext textInput']")
    home.click()
    time.sleep(0.1)
    home.send_keys("ha")
    time.sleep(1)
    home.send_keys(Keys.DOWN)
    time.sleep(0.2)
    home.send_keys(Keys.ENTER)
    time.sleep(0.5)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    submit.submit()
    time.sleep(2)
    """
    #relationship
    all_detail[4].click()
    time.sleep(0.5)
    rela = drv.find_element_by_xpath("//li/a[@data-testid='add_relationship']")
    rela.click()
    time.sleep(2)
    single = drv.find_element_by_xpath("//div/select/option[@value='1']")
    single.click()
    time.sleep(0.5)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    submit.submit()
    time.sleep(2)

    #Detail about
    all_detail[5].click()
    time.sleep(0.5)
    detail = drv.find_element_by_xpath("//a[@data-testid='add_details']")
    detail.click()
    time.sleep(2)
    write = drv.find_element_by_xpath("//div/texarea[@class='uiTextareaAutogrow _3egg']")
    ran = randint(0,5)
    write.send_keys(about_you[ran])
    time.sleep(0.5)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    submit.submit()
    time.sleep(2)
    
    nick = drv.find_element_by_xpath("//a[@data-testid='add_other_names'']")
    nick.click()
    time.sleep(2)
    name = drv.find_element_by_xpath("//div[@class='_pt5 _4bl7']/label/input")
    ran = randint(0,12)
    name.send_keys(nick_name[ran])
    time.sleep(0.5)
    check = drv.find_element_by_xpath("//div[@class='uiInputLabel clearfix'/label/input[@type='checkbox']")
    check.click()
    time.sleep(0.5)
    submit = drv.find_element_by_xpath("//div[@class='clearfix _ikh']/div/div/button[@name='__submit__']")
    submit.submit()
    time.sleep(2)

