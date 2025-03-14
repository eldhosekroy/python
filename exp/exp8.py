import nltk

from nltk.corpus import treebank

from nltk.tag import hmm

# Step 1: Download required NLTK datasets (run once)

nltk.download('treebank')

nltk.download('universal_tagset')
train_data = treebank.tagged_sents(tagset='universal')[:3000] # 

#First 3000 sentences for training

test_data = treebank.tagged_sents(tagset='universal')[3000:3100] 

# Next 100 sentences for testing

# Step 3: Initialize the HMM Trainer

trainer = hmm.HiddenMarkovModelTrainer()

# Step 4: Train the HMM POS Tagger

hmm_tagger = trainer.train(train_data)

# Step 5: Test the HMM POS Tagger on a sample sentence

sample_sentence = "The quick brown fox jumps over the lazy dog".split()

tagged_sentence = hmm_tagger.tag(sample_sentence)

# Step 6: Print the Tagged Sentence

print("POS Tagged Sentence:")

for word, tag in tagged_sentence:

 print(f"{word} → {tag}")
