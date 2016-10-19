from selenium import webdriver

#check whether this account is disabled
def save_dead_proxy(driver, PROXY_HOST, PROXY_PORT):
    try: 
        #disabled sign
        driver.find_element_by_id("u_0_4")
        #open txt file and write at the end of the text file
        file = open("dead_proxy.txt","a")
        file.write(PROXY_HOST)
        file.write("\n")
        file.write(PROXY_PORT)
        file.write("\n")
    except:
        pass