# Python program to generate word vectors using Word2Vec
# importing all necessary modules
from gensim.models import Word2Vec
import gensim
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
# nltk.download('punkt')
warnings.filterwarnings(action='ignore')

# Reads ‘alice.txt’ file
sample = open('p0f1.log', 'r+')
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", ".").replace("|", " ")
data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)
# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count=1, vector_size=100, window=5)
# Print results
print("a vector in cbow:\n", model1.wv['mod=syn'])
print("Cosine similarity between 'mod=syn' " + "and 'subj=cli' - CBOW : ",
      model1.wv.similarity('mod=syn', 'subj=cli'))
print("Cosine similarity between 'subj=cli' " + "and 'raw_mtu=1480' - CBOW : ",
      model1.wv.similarity('subj=cli', 'raw_mtu=1480'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(
    data, min_count=1, vector_size=100, window=5, sg=1)
# Print results
print("a vector in skip gram:\n", model2.wv['mod=syn'])
print("Cosine similarity between 'mod=syn' " +
      "and 'subj=cli' - Skip Gram : ", model1.wv.similarity('mod=syn', 'subj=cli'))
print("Cosine similarity between 'subj=cli' " + "and 'raw_mtu=1480' - Skip Gram : ",
      model1.wv.similarity('subj=cli', 'raw_mtu=1480'))
