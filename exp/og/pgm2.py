from nltk.tokenize import word_tokenize
from nltk import pos_tag
text="NLTK is a powerful library for NLP."
tokens=word_tokenize(text)
pos_tags=pos_tag(tokens)
print("POS Tag:",pos_tags)
