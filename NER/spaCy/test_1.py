# https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone ' \
     'market and ordered the company to alter its practices '


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


sent_1 = preprocess(ex)
# print(sent_1)
# this gives us a list of tuples containing the words and their associated part of speech:

# [('European', 'JJ'), ('authorities', 'NNS'), ('fined', 'VBD'), ('Google', 'NNP'), ('a', 'DT'), ('record', 'NN'),
# ('$', '$'), ('5.1', 'CD'), ('billion', 'CD'), ('on', 'IN'), ('Wednesday', 'NNP'), ('for', 'IN'), ('abusing', 'VBG'),
# ('its', 'PRP$'), ('power', 'NN'), ('in', 'IN'), ('the', 'DT'), ('mobile', 'JJ'), ('phone', 'NN'), ('market', 'NN'),
# ('and', 'CC'), ('ordered', 'VBD'), ('the', 'DT'), ('company', 'NN'), ('to', 'TO'), ('alter', 'VB'), ('its', 'PRP$'),
# ('practices', 'NNS')]

# Now we implement noun phrase chunking to identify named entities using a REGEX consisting of rules that indicate how
# sentences should be chunked - the pattern consists of one rule: a noun phrase (NP) should be formed whenever the
# chunker finds an optional determiner (DT) followed by any number of adjectives (JJ) followed by a noun (NN)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

# using this pattern we create a chunk parser and test it on our sentence

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent_1)
print(cs)



