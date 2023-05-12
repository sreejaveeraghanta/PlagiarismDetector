from difflib import SequenceMatcher

def checkSimilarity(string_input1, string_input2): 
    output = SequenceMatcher(None, string_input1, string_input2).ratio()
    return str("%.2f" % (output*100))


