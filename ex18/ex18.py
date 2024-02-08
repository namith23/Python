#spliting a sentence
sentence = input()
result = {word: len(word) for word in sentence.split()}
print(result)
