import nltk
import mentalModel as mm
import datetime

def extractInfo(sentence):
    mm.setDateTime(datetime.datetime.now())
    mm.setSentence(sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for (word, pos) in tagged if pos == 'NN' or pos == 'NNS' or pos == 'NNPS' or pos == 'PRP$' or pos == 'VBD']
    mm.setKeywords(nouns)
    mm.updateModel()



