# https://www.codingame.com/training/easy/text-formatting

import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

intext = input()

new_sentence = []
final_sentence = []

puncstr = string.punctuation

sentence = intext.lower().split(".")

for elem in sentence:
    for char in puncstr:
        for i in range(len(elem) - 1):
            if elem[i] == elem[i + 1] and elem[i] in puncstr:
                while elem[i] == elem[i + 1]:
                    elem = elem[:i] + elem[i + 1:] + " "
            if elem[i] == " " and elem[i + 1] in puncstr:
                elem = elem[:i] + elem[i + 1:] + " "
            if elem[i] == char and elem[i + 1] != " ":
                elem = elem[:i + 1] + " " + elem[i + 1:]
    new_sentence.append(elem)

new_sentence = [" ".join(elem.split()) for elem in new_sentence]
new_sentence = [elem.strip().lstrip().capitalize() for elem in new_sentence if elem != ""]


for elem in new_sentence:
    elem = elem + "." if len(elem.split()) > 1 else elem
    final_sentence.append(elem)

answer = " ".join(final_sentence)

print(answer)