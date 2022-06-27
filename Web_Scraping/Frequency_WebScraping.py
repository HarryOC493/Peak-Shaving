from selenium import webdriver
from selenium.webdriver.common.by import By
from Merge import Merge
import time

counter = 1


chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/harryoconnor/Desktop/PeakShaving/Data/Frequency"}
#Chromedriver Path
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

# Send a get request to the url, and wait for the page to load
driver.get('https://smartgriddashboard.com/#roi/frequency')
time.sleep(20)
print('Loading Web Page')

#Open the table dropdown
driver.find_element(by=By.XPATH, value='//*[@id="frequencyChartCtr"]/section/div[2]/div[5]/h3/a').click()
print('Opened Table Dropdown')
time.sleep(2)

#Get the daterange, and convert to integer. For selecting yesterdays table
daterange = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[7]/div/section/div[2]/div[1]/nav/a[4]')
print('Getting Daterange')
time.sleep(2)
#print(daterange.text)

#Remove Whitespace from string
TimeToTravel = daterange.text
TimeToTravel = TimeToTravel.replace(" ", "")
#print(TimeToTravel)

#Remove everything but the Hour we need
TimeToTravel = TimeToTravel.rsplit('-')
print(TimeToTravel[1])
TimeToTravel = TimeToTravel[1][:-3]
print('Time to travel: ' + TimeToTravel)






print('Beginning Time Travel')
for x in range(0, int(TimeToTravel)):
    #Time travel, to the table for yesterday @ 23:00-00:00 as table starts at latest hour and we need a full days data
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[7]/div/section/div[2]/div[1]/nav/a[1]').click()
    time.sleep(1)
print('Time travel finished, beginning to get data!')
for x in range (0, 24):
    #Download csv of data for every hour in day
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="frequencyChartCtr"]/section/div[2]/div[5]/h3/a').click()
    #Tell the WebDriver to keep searching for 10 seconds, if it cannot immediately find specified element. Stops error due to slow internet
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[7]/div/section/div[2]/div[5]/div/div/div/a').click()
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[7]/div/section/div[2]/div[1]/nav/a[1]').click()
    driver.implicitly_wait(10)
    time.sleep(1)

#All files have been downloaded, formatting is weird though, time and data is in the same column but split using a comma
#Need to merge all files together and correct data formatting
#File name format: 
#Frequency_08.Jun.2022.08.00_08.Jun.2022.09.00.csv
#Frequency_08.Jun.2022.09.00_08.Jun.2022.10.00.csv

print('All files downloaded, successfully, merging ...')
Merge()

driver.quit()
print("\033[92m Done, all files merged and formatted!")