from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
config = RasaNLUConfig("config_chatbot_spacy.json")
training_data = load_data('data/commands.json')
trainer = Trainer(config)
trainer.train(training_data)
# Returns the directory the model is stored in
model_directory = trainer.persist('./projects/')  

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory, config)

q1 = u"was ist arp?"
q2 = u"was ist ping?"
q3 = u"was ist ping"

a1 = interpreter.parse(q1)
a2 = interpreter.parse(q2)
a3 = interpreter.parse(q3)
print("\n\n#################################")
print(str(model_directory))
print("\n\n#################################")
print(q1)
obj1 = a1['intent_ranking'][0]
print("intent :" + str(obj1['name']) + " with " + str(obj1['confidence']))
print(a1)

print(q2)
obj2 = a2['intent_ranking'][0]
print("intent :" + str(obj2['name']) + " with " + str(obj2['confidence']))
print(a2)

print(q3)
obj3 = a3['intent_ranking'][0]
print("intent :" + str(obj3['name']) + " with " + str(obj3['confidence']))
print(a3)
