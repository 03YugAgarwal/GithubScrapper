from selenium import webdriver
from selenium.webdriver.common.by import By

import time

repository_url = 'https://github.com/apache/dubbo/commits/3.2'
driver = webdriver.Chrome()

loop = True

try:
    driver.get(repository_url)
    while loop:
        time.sleep(1)
        print(driver.current_url)
        time.sleep(1)
        if driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a') and driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a').text == 'Older':
            element = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a')
            element.click()
        elif driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a[2]') and driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a[2]').text == 'Older':
            element = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[4]/div/a[2]')
            element.click()
        else:
            loop = False
finally:
    driver.quit()