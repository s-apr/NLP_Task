import spacy

print("""==========
extract 1
""")

nlp = spacy.load('en_core_web_md')

#word1 = nlp("cat")
#word2 = nlp("monkey")
#word3 = nlp("banana")

word1 = nlp("Keyboard")
word2 = nlp("Trainer")
word3 = nlp("Ring")

print(word1.similarity(word2))
print(word2.similarity(word3))
print(word3.similarity(word1))

print("""
==========
extract 2
""")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("""
==========
extract 3
""")

sentence_to_compare = "Why is my cat on the car"
print(f"Comparitive sentence: {sentence_to_compare}' \n")

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)