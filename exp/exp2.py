import nltk

# Download the necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Read the content of the file and tokenize the text
with open('mydata.txt', 'r') as file:
    text_data = file.read()
    tokens = nltk.word_tokenize(text_data)
    text = nltk.Text(tokens)
    text.concordance("network", width=80, lines=10)

