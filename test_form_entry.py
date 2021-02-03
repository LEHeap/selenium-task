import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def setup():
    global driver
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
# Optional argument, if not specified will search path.
#driver = webdriver.Chrome()


def test_names_with_capital():
    #setup()

    driver.get('file://C:/work/selenium-task/practice_page.html')
    
    firstnameElement = driver.find_element_by_id("firstname")
    firstnameElement.send_keys("laura")

    lastnameElement = driver.find_element_by_id("lastname")
    lastnameElement.send_keys("heap")

    usernameElement = driver.find_element_by_id("username")
    usernameElement.send_keys("heap1234")

    actualFirstname = firstnameElement.get_attribute("value")
    expectedFirstname = "Laura"

    actualLastname = lastnameElement.get_attribute("value")
    expectedLastname = "Heap"

    assert actualFirstname == expectedFirstname
    assert actualLastname == expectedLastname
    driver.quit()

   
def test_age_blank():
    #setup()

    driver.get('file://C:/work/selenium-task/practice_page.html')
    
    dobElement = driver.find_element_by_id("birthday")
    actualDob = dobElement.get_attribute("value")
    expectedDob = ''
    
    ageElement = driver.find_element_by_id("age")

    actualAge = ageElement.get_attribute("innerText") #stores the value found in the field
    expectedAge = "XXX"
    
    assert actualDob == expectedDob
    assert actualAge == expectedAge
    driver.quit()

def test_age_populated():
    #setup()

    driver.get('file://C:/work/selenium-task/practice_page.html')
    
    dobElement = driver.find_element_by_id("birthday")
    dobElement.send_keys("25-04-1985")
    
    ageElement = driver.find_element_by_id("age")

    actualAge = ageElement.get_attribute("innerText") #stores the value found in the field
    expectedAge = "35"
    
    assert actualAge == expectedAge
    driver.quit()