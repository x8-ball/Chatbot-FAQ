#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aiml
import os
import sys
from inspect import getsourcefile
import os.path
from random import randint
import time
import threading
sys.path.append('.')

current_path = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
aimlPath = current_path+'/aiml/'
brains = {}
MAX_CAP = 1
DELETE_AFTER_X_MIN = 0.3
CHECK_EVERY_X_SEC = 1

class Brain:
	def __init__(self, ip):
		self.kernel = aiml.Kernel()
		self.kernel.bootstrap(brainFile = aimlPath+ "bot_brain.brn")
		self.lastUsed = time.time()
		self.ip = ip

	def answer(self,question):
		print "old timestamp: " + str(self.lastUsed)
		self.lastUsed = time.time()
		print "updated " + self.ip + " with new timestamp: " + str(self.lastUsed)
		return self.kernel.respond(question)


def generateBrain():
	kernel = aiml.Kernel()	
	kernel.bootstrap(learnFiles = aimlPath + "std-startup.xml", commands = "LOAD AIML B")
	kernel.saveBrain(aimlPath+"bot_brain.brn")	

def deleteOldBrains():
	threading.Timer(CHECK_EVERY_X_SEC, deleteOldBrains).start()
	for brain in brains.keys():
		checkedObject = brains[brain]
		diffMinutes = (time.time() - checkedObject.lastUsed)/60 
		if diffMinutes > DELETE_AFTER_X_MIN:
			print time.time()
			print checkedObject.lastUsed
			print diffMinutes
			print DELETE_AFTER_X_MIN
			deleteBrain(checkedObject.ip)

def loadBrain(ip):
	response = ""
	print MAX_CAP , len(brains) 
	if len(brains) < MAX_CAP:
		if ip not in brains:
			brains[ip] = Brain(ip)
			print "created brain for "+ ip
		else:
			print "brain already exists"
		return True
	else:
		return False

def deleteBrain(ip):
	if ip in brains:
		del brains[ip]
		print "ip " + ip +" deleted"

def calcResponse(question,ip):
	print "answer for " + ip
	print brains
	if ip in brains:
		return brains[ip].answer(question)
	else: 
		return "Robi ist gerade sehr beschäftigt und hat keine Zeit"

generateBrain()
deleteOldBrains()