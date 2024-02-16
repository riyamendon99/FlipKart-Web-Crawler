from selenium import webdriver
import time
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# creating the reference variable ‘driver’ of the WebDriver and create an instance of firefox with the path of the driver
driver = webdriver.Firefox(executable_path=r"C:\Users\riyam\PycharmProjects\SeleniumTest\drivers\geckodriver.exe")

#get method to open specific url
driver.get("https://www.flipkart.com/")
#resize the window to max size
driver.maximize_window()
driver.implicitly_wait(100)

#done to remove any pop ups
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()


"""Search iPhone 8 on search bar"""

search_bar = driver.find_element_by_name("q") #find the search bar element by name
search_bar.clear() #clear contents of search bar
search_bar.send_keys("iPhone 8")  #type in the string for searching
search_bar.send_keys(Keys.RETURN) #emulate the press of the Return key
search = driver.find_element_by_xpath("//button[@class='vh79eN']")  #find the element by xpath of search button
driver.execute_script("arguments[0].click();", search)    #execute by clicking on the search button
driver.implicitly_wait(100)
time.sleep(3)    #time period for browser wait

"""Select on Mobiles Category"""

driver.find_element_by_xpath("//a[@class='_3XS1AH _32ZSYo']").click() #find element by xpath aand click
time.sleep(3)

"""Set the price greater than 35000"""

minprice = Select(driver.find_element_by_xpath("*//div[@class='_3Uy12X']/div[@class='_1qKb_B']/select[@class='fPjUPw']")) #using selector class to select from dropdown list
minprice.select_by_value("30000")
time.sleep(3)

"""Check Flipkart Assured"""

checkbox1 = driver.find_element_by_xpath("//div[@class='_2kFyHg _1_fxb2']//input[@class='_3uUUD5']")
time.sleep(3)
ActionChains(driver).move_to_element(checkbox1).click(checkbox1).perform()
time.sleep(3)

"""Check Brand Apple"""

#to navigate to the specific element
def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
checkbox2 = driver.find_element_by_xpath('//section[5]//div[2]//div[1]//div[1]//div[1]//div[1]//label[1]//div[1]')
if 'firefox' in driver.capabilities['browserName']:
    scroll_shim(driver, checkbox2)
ActionChains(driver).move_to_element(checkbox2).click(checkbox2).perform()
time.sleep(4)

"""Scroll down to specific pixel"""
driver.execute_script("window.scrollBy(0,4000)", "")


"""Print the name,price,link to product detail page on console"""

name = driver.find_element_by_class_name("_3wU53n").text
print(name)
driver.implicitly_wait(100)
price = driver.find_element_by_xpath("//div[contains(text(),'52,999')]").text
print(price)
driver.implicitly_wait(100)
for a in driver.find_elements_by_class_name('_1UoZlX') and driver.find_elements_by_class_name('_31qSD5'):
    print(a.get_attribute('href'))
    #if(a.getAttribute("class") != '_1UoZlX'):
    break
driver.close()



