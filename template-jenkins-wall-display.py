#!/usr/bin/env/python

from wallDisplay import WallDisplay

def exit_handler(signal, frame):
	global display
	display.close()
	sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

display = WallDisplay("%JENKINS_URL%", "%JENKINS_USER%", "%JENKINS_API_KEY%", "%VIEW_ID%")

display.show()

while True:
	continue
	
