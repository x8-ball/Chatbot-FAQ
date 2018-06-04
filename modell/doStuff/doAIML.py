import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("aiml/bot_brain.brn"):
    kernel.bootstrap(brainFile = "aiml/bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("aiml/bot_brain.brn")

# kernel now ready for use
while True:
    print kernel.respond(raw_input("Enter your message >> "))