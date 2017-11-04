vowel = ["A", "E", "I", "O","U"]
x = 0
newsent = ""
message = input("enter a message to code into PigLatin")
splitsent = message.split()
print("original message: " + message)
coded = list()
#here i am spliting the string into a list of strings 
for element in splitsent:
#splitting a word into a list of letters
    letters = element.split()
#checking if the the first letter is a vowel and then 
    word = letters[0]
    if word[x].upper() in vowel:
#taking the correct action
        codedword = word +"ay"
        newsent = newsent + codedword + " "
            
    else:
#if it is not then the program takes the appropriate action
        firstletter = word[0]
        letterslist = list()
        for i in word:
            letterslist.append(i)
        letterslist.pop(x)
        letterslist.append(firstletter)
        letterslist.append("a")
        letterslist.append("y")
#i then add the words to a new sentance
        for i in letterslist:
            newsent = newsent + i
        newsent = newsent + " "
print("PigLatin coded message: " + newsent)
            
