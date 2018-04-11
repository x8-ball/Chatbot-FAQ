from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
config = RasaNLUConfig("config_chatbot_spacy.json")
training_data = load_data('data/faq_lab1.json')
trainer = Trainer(config)
trainer.train(training_data)
# Returns the directory the model is stored in
model_directory = trainer.persist('./projects/')  
print(model_directory)
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory, config)

print("\n\n#################################")
print(q1)
print(a1)

print(q2)
print(a2)