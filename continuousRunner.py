#!/usr/bin/env/python

import signal
import sys

class ContinuousRunner():
	
	def __init__(self, start, stop):
		self.startHandler = start
		self.stopHandler = stop
		
	def destroy(self):
		self.stopHandler()
		sys.exit(0)
	
	def exit_handler(self, signal, frame):
		self.destroy()
		
	def start(self):
		signal.signal(signal.SIGTERM, self.exit_handler)
		self.startHandler()
		try:
			while True:
				continue
		except(KeyboardInterrupt):
			self.destroy()