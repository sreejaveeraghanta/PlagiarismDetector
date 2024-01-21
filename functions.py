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
    words1 = tokenizer(input1)
    words2 = tokenizer(input2)
    ## want to check for similiarity in terms of continuous words rather tahn every single one

    count = 0
    for word in words1: 
        for word2 in words2: 
            if word == word2: 
                count+=1
                print(word)
    if len(words1) > len(words2): 
        return (count / len(words1)) * 100
    else: 
        return (count / len(words2)) * 100

def readFile(file):
    open('file', 'r')


print(tokenizer("bob the builder, can you fix it?"))
print(checkSimilarity("\n \t Bob bob!       The Builder? can we fix it? YES, we can!     ", "Bob the builder"))



