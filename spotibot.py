from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import random

EMAIL = " "
PASSWORD = " "
PLAYLIST = " "

driver = webdriver.Chrome()
	
driver.maximize_window()
	
driver.get("https://accounts.spotify.com/en/login")
	
time.sleep(10)
	
user = driver.find_element(By.ID, "login-username")
password = driver.find_element(By.ID, "login-password")
	
user.send_keys(EMAIL)
password.send_keys(PASSWORD)
	
login = driver.find_element(By.CLASS_NAME, "Button-sc-qlcn5g-0.otMlU")

time.sleep(5)
	
login.click()
	
time.sleep(5)
	
print("[*] Login Succesfully")
	
driver.get(PLAYLIST)
	
time.sleep(30)

while True:

	checkPlay = random.randint(1100,1800)	
	
#	firstSong = driver.find_element(By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.gYqKuy.t_yrXoUO3qGsJS4Y6iXX.standalone-ellipsis-one-line")
	
#	actionChains = ActionChains(driver)
	
#	actionChains.double_click(firstSong).perform()
	
	
	play = driver.find_element(By.CLASS_NAME, "Button-sc-qlcn5g-0.jqMzOG")
	
	play.click()
	
	
	streamTime = driver.find_element(By.CLASS_NAME, "poz9gZKE7xqFwgk231J4")
	
	hours = streamTime.text.split(" ")
	
	print("[*] Playlist time Lenght: "+ hours[1] + "hours")
	
	seconds = int(hours[1]) * 3600
	
	titlePlaylist = driver.find_element(By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.bZdlXz")
	
	print("[*] Playing now >> " + titlePlaylist.text)
	
	time.sleep(checkPlay)
	
	driver.refresh()
