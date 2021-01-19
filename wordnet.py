
#%%import nltk 
# %%
from nltk.corpus import wordnet as wn
# %%
wn.synset('dog.n.01')
# %%
print(wn.synset('dog.n.01'))
# %%
dog = wn.synset('dog.n.01')
# %%
dog
# %%
import nltk
# %%
nltk.download('wordnet')
# %%
animal = wn.synset('animal.n.01')
cat = wn.synset('cat.n.01')
# %%
animal.path_similarity(cat)
# %%

# %%
