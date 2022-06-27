from selenium import webdriver
from selenium.webdriver.common.by import By

import time


#Configure ChromeDriver
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/harryoconnor/Desktop/PeakShaving/Data/Demand"}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

# Send a get request to the url, and wait for the page to load
driver.get('https://www.eirgridgroup.com/how-the-grid-works/system-information/')
time.sleep(20)
print('Loading Web Page')

#Open the Demand Table
driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[1]/div/div/div[1]/div/a').click()
print('Opened Demand Chart')
time.sleep(2)

#Travel to Yesterday (Need a full days data)
driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div[2]/div/div[2]/a[1]').click()
print('Opened Yesterdays Data')
time.sleep(2)

#Download .csv file
driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div[4]/div/button').click()
print('Opened Demand Chart')
time.sleep(2)


print("\033[92m Done, Downloaded yesterdays demand data")