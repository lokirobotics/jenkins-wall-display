#!/usr/bin/env/python

from wallDisplay import WallDisplay

display = WallDisplay("%JENKINS_URL%", "%JENKINS_USER%", "%JENKINS_API_KEY%", "%VIEW_ID%")

display.start()
