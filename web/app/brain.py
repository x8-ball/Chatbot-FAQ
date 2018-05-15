from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import sys

model_directory = "../../modell/projects/default/model_20180515-115936"
interpreter = Interpreter.load(model_directory, RasaNLUConfig("../../modell/config_chatbot_spacy.json"))

def calcResponse(question):
	return interpreter.parse(str(question).decode(sys.stdin.encoding))['intent_ranking'][0]
	#print(answer['name'],answer['confidence'])