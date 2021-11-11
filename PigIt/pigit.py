# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
def pig_it(text):
    splitText = text.split(" ")

    finalSentence = ""
    for i in splitText:
        firstletter = i[0]
        remainingLetters = i[1:]
        if i == "!" or i == "?":
            finalSentence += i
            break
        finalSentence += remainingLetters+firstletter+"ay"+" "
        
    if finalSentence[-1] == " ":
        finalSentence = finalSentence[:-1]
    return finalSentence

if __name__ == "__main__":
     assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay" 
     assert pig_it("This is my string") == "hisTay siay ymay tringsay" 