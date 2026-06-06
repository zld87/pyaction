from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time


def chengzhong(driver):
    Intelligent_butler = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div')
    Intelligent_butler.click()
    new_Intelligent_butler = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[7]/div')
    new_Intelligent_butler.click()
    time.sleep(5)




