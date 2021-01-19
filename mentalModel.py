from collections import ChainMap
class Instance:
  def __init__(self, sentence, context, dateTime, emotion, Intensity):
    self.sentence = sentence
    self.context = context #all the keywords
    self.dateTime = dateTime #recorded by system
    self.emotion = emotion #from the analysis step
    self.Intensity = Intensity #from the analysis step
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

def updateModel(sentence, keywords, dateTime, emotion,Intensity):
  # use created instance
  for word in keywords:
    if word in mentalModel.keys():
      mentalModel[word].append(Instance(sentence,keywords,dateTime,emotion,Intensity))
    else:
      mentalModel[word] = [Instance(sentence,keywords,dateTime,emotion,Intensity)]
  for x in mentalModel.values():
    for y in x:
      print(y.display())


updateModel("I have a dog",['have','dog'],"1/13/2021 11:58","happy","5")
updateModel("I have a cat",['have','cat'],"1/13/2021 11:58","happy","5")
