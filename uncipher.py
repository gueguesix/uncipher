import argparse
import string


parser = argparse.ArgumentParser()
parser.add_argument('caesarString', type=str)
parser.add_argument('--dict', dest='path')

args = parser.parse_args()



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']


d = open(args.path, 'r').read().split("\n")
transAlphabet = {}

def createDict(shift):
    for i in range(0,26):
        letter = alphabet[i]
        transAlphabet[letter]=alphabet[(i+shift)%26]


def decodeMessage(message):
    total = 0
    cypherText = ''
    for letter in message:
        if letter in transAlphabet:
            cypherText = cypherText + transAlphabet[letter]
        else:
            cypherText = cypherText + letter
    t = cypherText.split()
    for word in t:
        if word in d:
            total = total+1
    b = total/len(t)
    if b >0.3:
        print(cypherText)

for i in range(0,26):
    createDict(i)
    decodeMessage(args.caesarString.lower())
