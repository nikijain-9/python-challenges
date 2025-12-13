# Word Frequency in a Sentence
sentence = "python is easy and python is powerful"

# Length approach
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)
        
# Shorter approach
from collections import Counter

freq = Counter(sentence.split(" "))
print(dict(freq))