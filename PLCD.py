vowel = ["A", "E", "I", "O","U"]
x = 0
newsent = ""
message = input("enter a message to code into PigLatin")
splitsent = message.split()
print("original message: " + message)
coded = list()
for element in splitsent:
    letters = element.split()
    word = letters[0]
        
    if word[x].upper() in vowel:
        codedword = word +"ay"
        newsent = newsent + codedword + " "
            
    else:
        firstletter = word[0]
        letterslist = list()
        for i in word:
            letterslist.append(i)
        letterslist.pop(x)
        letterslist.append(firstletter)
        letterslist.append("a")
        letterslist.append("y")

        for i in letterslist:
            newsent = newsent + i
        newsent = newsent + " "
print("PigLatin coded message: " + newsent)
            
