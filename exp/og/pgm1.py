from nltk.tokenize import word_tokenize,sent_tokenize
text="Hello,world! This is a test sentense."
word_tokens=word_tokenize(text)
sent_tokens=sent_tokenize(text)
print("world tokens:",word_tokens)
print("sentence tokens:",sent_tokens)
