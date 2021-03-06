#!/usr/bin/env python
text = input()

words = text.split(" ")
reversedWords = [word[::-1] for word in words]
reversedText = " ".join(reversedWords)

print(reversedText)
