import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('http://youtube.com')
driver.maximize_window()
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
wait = WebDriverWait(driver, 3)
searchbox.send_keys('For whom the bells Tolls')
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
wait = WebDriverWait(driver, 55)
visible = EC.visibility_of_element_located
wait.until(visible((By.XPATH,'//*[@id="contents"]/ytd-video-renderer[4]')))
linkButton = driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[4]')
linkButton.click()