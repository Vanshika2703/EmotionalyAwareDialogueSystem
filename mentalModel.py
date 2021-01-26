from collections import ChainMap
import nltk
#import wordnet.py as wn

emotionalState = 000
keywords = []
sentence = ""
dateTime = None


def setKeywords(keywordList):
  print(keywordList)
  keywords = keywordList


def setSentence(line):
  print(line)
  sentence = line

 
def setEmotionalState(detectedState):
  emotionalState = detectedState 

def setDateTime(time):
  print(time)
  dateTime = time

class Instance:
  def __init__(self, sentence, context, dateTime, emotionalState):
    self.sentence = sentence
    self.context = context #all the keywords
    self.dateTime = dateTime #recorded by system
    self.emotionalState = emotionalState #from analysis step
    self.duration = 0 #will be initialized to zero ad updated when there is an emotion change
    self.changedEmotion = None #will be initialized to null
    self.instanceChanged = None #will be initialized to null
  
  def display(self):
      print("sentence: "+ self.sentence +", context: ")
      print(self.context)

  def updateDuration(self, duration):
    self.duration = duration
  
  def updateChangedEmotion(self, changedEmotion):
    self.changedEmotion = changedEmotion

  def updateInstanceChanged(self, instanceChanged):
    self.instanceChanged = instanceChanged  
    
mentalModel = {}

def updateModel():
  # use created instance
  for word in keywords:
    if word in mentalModel.keys():
      mentalModel[word].append(Instance(sentence,keywords,dateTime,emotionalState))
    else:
      mentalModel[word] = [Instance(sentence,keywords,dateTime,emotionalState)]
  for x in mentalModel.values():
    for y in x:
      print(y.display())