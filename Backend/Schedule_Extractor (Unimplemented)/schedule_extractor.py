from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_schedule(user, passw):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://aspen.cpsd.us/aspen/logon.do")

    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(passw)
    driver.find_element(By.ID, "logonButton").click()

