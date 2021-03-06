import nltk
data = open('input.txt', encoding="utf8").read()
# Applying Tokenization
w_tokens = nltk.word_tokenize(data)
print("\n WORD-TOCKENIZATION\n")
print(w_tokens)
s_tokens = nltk.sent_tokenize(data)
print("\n SENTENCE-TOCKENIZATION\n")
print(s_tokens)
# Applying Stemming
print("\n STREMING\n")
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
p_Stemmer = PorterStemmer()
l_Stemmer = LancasterStemmer()
s_Stemmer = SnowballStemmer('english')
n1 = 0
for t in w_tokens:
    n1 = n1 + 1
    if n1 < 4:
        print(p_Stemmer.stem(t), l_Stemmer.stem(t), s_Stemmer.stem(t))
# POS
# Applying Lemmatization
print("\n POS / LEMMATIZATION\n")
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
n1 = 0
for t in w_tokens:
    n1 = n1 + 1
    if n1 < 6:
        print("Lemmatizer:", l.lemmatize(t), ", With POS=a:", l.lemmatize(t, pos="a"))
# Trigram
print("\n TRIGRAM \n")
from nltk.util import ngrams
token = nltk.word_tokenize(data)
n = 0
for s in s_tokens:
    n = n + 1
    if n < 2:
        token = nltk.word_tokenize(s)
        bigrams = list(ngrams(token, 2))
        trigrams = list(ngrams(token, 3))
        print("The text:", s, "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)
#Applying Named Entity Recognition
print("\n Named Entity Recognition\n")
from nltk import word_tokenize, pos_tag, ne_chunk
n = 0
for s in s_tokens:
    n = n + 1
    if n < 2:
        print(ne_chunk(pos_tag(word_tokenize(s))))