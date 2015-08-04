#!/usr/bin/env/python

import signal
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WallDisplay :
	def __init__(self, jenkinsUrl, username, password, viewId):
		self.jenkinsUrl = jenkinsUrl
		self.username = username
		self.password = password
		self.viewId = viewId
	
	def show(self):
		driver = webdriver.Firefox()
		driver.get("{}/login".format(self.jenkinsUrl))
		nameField = driver.find_element_by_name("j_username")
		nameField.send_keys(self.username)
		passwordField = driver.find_element_by_name("j_password")
		passwordField.send_keys(self.password)
		loginButton = driver.find_element_by_id("yui-gen1-button")
		loginButton.click()
		driver.get("{}/user/{}/my-views/view/{}/".format(self.jenkinsUrl, self.username, self.viewId))
		driver.find_element_by_tag_name("body").send_keys(Keys.F11)
		self.driver = driver
		return

	def close(self):
		print "closing display"
		self.driver.close()
		return

def exit_handler(signal, frame):
	global display
	display.close()
	sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

display = WallDisplay("http://chekov", "geordi", "itb5geordi", "OSC%20Build%20Monitor")

display.show()

while True:
	continue
	
