from difflib import SequenceMatcher

def removePunctuation(text):
    result = ""
    punctuation = [",", ".", "!", "?", "(", ")", ":", ";", "-"]
    for character in text: 
        if character not in punctuation: 
            result += character
    return result

def lowerCase(text):
    result = ""
    text = removePunctuation(text)
    for character in text: 
        if ord(character) >= 65 and ord(character) <= 90: 
            result += chr(ord(character) + 32)
        else: 
            result += character
    return result

def tokenizer(text): 
    text = lowerCase(text)
    result = []
    notValid = ["", " ", "\n", "\t", "\b" "\r"]
    temp = ""
    i = 0 
    while i < len(text): 
        if text[i] in notValid:
            if temp != "":
                result.append(temp)
            temp = ""
        else: 
            temp += text[i]
        i+=1 
    # To get the last word
    if temp != "":
        result.append(temp)
    return result

def checkSimilarity(input1, input2): 
    output = SequenceMatcher(None, input1, input2).ratio()
    return str("%.2f" % (output*100))

def readFile(file):
    open('file', 'r')


print(checkSimilarity("\n \t Bob!       The Builder? can we fix it? no. we can't, hahahah     ", "Bob the builder"))



