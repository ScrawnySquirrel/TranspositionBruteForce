#!/usr/bin/python3.5

# Detect English module
# Provides all of the functions needed to find dictionary words

# returns True or False
# Uses a "dictionary.txt" file in the current directory with English words in it, one word per line. 
UpperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alphabet = UpperCase + UpperCase.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open ('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None   # the very last item is "none" -> no match
    dictionaryFile.close()
    return englishWords


# breaks the string up into individual words and matches them agains the dictionary to find the number of matches
def getWordCount (message):
    WordList = loadDictionary()
    message = message.upper()
    message = removeNonLetters (message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # no matches found

    matches = 0
    for word in possibleWords:
        if word in WordList:
            matches += 1
    return float (matches) / len (possibleWords)
    


# Remove all the non-letter characters from the string
def removeNonLetters (message):
    lettersOnly = []
    for symbol in message:
        if symbol in Alphabet:
            lettersOnly.append (symbol)
    return ''.join (lettersOnly)



# Given the thersholds, return true of false for a wordmatch and a letter match
def FindEnglish (message, wordPercentage = 20, letterPercentage = 85):
    
    wordsMatch = getWordCount (message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters (message))
    messageLettersPercentage = float (numLetters) / len (message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
