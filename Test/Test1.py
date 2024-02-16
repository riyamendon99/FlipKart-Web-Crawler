from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""creating the reference variable ‘driver’ of the WebDriver and create an instance of firefox with the path of the driver"""
driver = webdriver.Chrome(r"C:\Users\riyam\PycharmProjects\SeleniumTest\drivers\chromedriver.exe")

"""get method to open specific url"""
driver.get("https://www.flipkart.com/")
"""resize the window to max size"""
driver.maximize_window()
driver.implicitly_wait(100)
time.sleep(3)

"""done to remove any pop ups"""
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(3)

"""Search iPhone 8 on search bar"""
search_bar = driver.find_element_by_name("q")      #find the search bar element by name
search_bar.clear()                                  #clear contents of search bar
search_bar.send_keys("iPhone 8")                    #type in the string for searching
search_bar.send_keys(Keys.RETURN)                   #emulate the press of the Return key
search = driver.find_element_by_xpath("//button[@class='vh79eN']")        #find the element by xpath of search button
driver.execute_script("arguments[0].click();", search)                    #execute by clicking on the search button
driver.implicitly_wait(100)
time.sleep(3)

"""Select on Mobiles Category"""
driver.find_element_by_link_text("Mobiles").click()      #find element by xpath aand click
time.sleep(3)


"""Set the price greater than 35000"""
minprice = Select(driver.find_element_by_xpath("*//div[@class='_3Uy12X']/div[@class='_1qKb_B']/select[@class='fPjUPw']"))
minprice.select_by_value("30000")
time.sleep(3)


"""Check Brand Apple"""
brand = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/section[5]/div[2]/div/div/div/div/label/input")
time.sleep(3)
ActionChains(driver).move_to_element(brand).click(brand).perform()
time.sleep(3)

"""Check Flipkart Assured"""
checkbox = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/section[3]/div[1]/label/input")
time.sleep(3)
ActionChains(driver).move_to_element(checkbox).click(checkbox).perform()
time.sleep(3)


"""Scroll down to bottom of page"""
"""WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[25]/div/div/div")))
act = ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[25]/div/div/div"))
act.send_keys(Keys.PAGE_DOWN).perform()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") """

"""driver.execute_script("window.scrollBy(0,5000)")
time.sleep(4)
driver.implicitly_wait(100) """

"""Print the name,price,link to product detail page on console"""
details = []

#for value in driver.find_elements_by_class_name('col col-7-12') and driver.find_elements_by_class_name('_3wU53n'):
    #print(value.text)

#name = driver.find_element_by_class_name("_3wU53n").text
#details.append(name)
#driver.implicitly_wait(100)
#price = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]").text
#details.append(price)
#driver.implicitly_wait(100)
"""names = []
for name in driver.find_elements_by_class_name('_3wU53n'):
    names.append(name.text)
time.sleep(3)
prices = []
for price in driver.find_elements_by_class_name('_1vC4OE _2rQ-NK'):
    prices.append(price.text)
time.sleep(3) """
for a in driver.find_elements_by_class_name('_31qSD5'):
         #and driver.find_elements_by_class_name('_31qSD5'):
    details.append(a.get_attribute('href'))
    #if(a.getAttribute("class") != '_1UoZlX'):
#driver.implicitly_wait(100)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#print(names)
#print(prices)
print(details)
driver.close()