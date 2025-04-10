import nltk

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

# Download necessary NLTK data (run once)

nltk.download('punkt')

nltk.download('stopwords')

# Define chatbot responses

responses = {

 "hello": "Hi there! How can I assist you?",

 "weather": "The weather is great today!",

 "name": "I'm ChatGPT's cousin, here to help you!",

 "bye": "Goodbye! Have a fantastic day!"

}

# Function to process user input

def nltk_chatbot():

 print("NLTK Chatbot: Hi! Ask me anything. Type 'bye' to exit.\n")
 while True:

    user_input = input("You: ").lower()

 

    if user_input == "bye":

        print("NLTK Chatbot:", responses["bye"])

        break

 # Tokenize and remove stopwords

    tokens = word_tokenize(user_input)

    filtered_words = [word for word in tokens if word not in 

    stopwords.words('english')]

 

    found = False

    for word in filtered_words:

        if word in responses:

            print("NLTK Chatbot:", responses[word])

            found = True

            break

        if not found:

            print("NLTK Chatbot: Sorry, I didn't quite get that. Try again!")

# Run chatbot

nltk_chatbot()
