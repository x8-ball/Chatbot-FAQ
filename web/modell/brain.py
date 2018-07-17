import aiml
import os
import sys
from inspect import getsourcefile
import os.path
sys.path.append('.')

kernel = aiml.Kernel()
current_path = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
print current_path
aimlPath = current_path+'/aiml/'
kernel.bootstrap(learnFiles = aimlPath + "std-startup.xml", commands = "LOAD AIML B")
print "aimlPath: " + aimlPath + "std-startup.xml"

def loadBrain():
	if os.path.isfile(aimlPath+"bot_brain.brn"):
	    kernel.bootstrap(brainFile = aimlPath+ "bot_brain.brn")
	else:
		kernel.bootstrap(learnFiles = aimlPath + "std-startup.xml", commands = "LOAD AIML B")
		kernel.saveBrain(aimlPath+"bot_brain.brn")

def calcResponse(question):
	return kernel.respond(question)