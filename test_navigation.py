import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

def setup():
    global driver
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
# Optional argument, if not specified will search path.
#driver = webdriver.Chrome()


def test_navigation_bbc():
    #setup()

    driver.get('file://C:/work/selenium-task/practice_page.html')

    homePageURL = driver.current_url
    bbcElement = driver.find_element_by_id("bbc")
    bbcElement.click()
    bbcActualLocation = driver.current_url
    bbcExpectedLocation = "https://www.bbc.com/news"
    assert bbcActualLocation == bbcExpectedLocation
    driver.get(homePageURL)
    homePageActual = driver.current_url
    assert homePageActual == homePageURL
    
    driver.quit()

def test_navigation_qa():
    #setup()

    driver.get('file://C:/work/selenium-task/practice_page.html')

    homePageURL = driver.current_url
    qaLink = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "qa")))
    qaExpectedLocation = qaLink.get_attribute("href")
    qaLink.click()
    qaActualLocation = driver.current_url
    
    assert qaActualLocation == qaExpectedLocation
    driver.get(homePageURL)
    homePageActual = driver.current_url
    assert homePageActual == homePageURL
    
    driver.quit()