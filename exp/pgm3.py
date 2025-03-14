from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import ne_chunk
text="Barack Obama was the 44th president of united states."
tokens=word_tokenize(text)
pos_tags=pos_tag(tokens)
named_entities=ne_chunk(pos_tags)
print("Named Entities:",named_entities)
