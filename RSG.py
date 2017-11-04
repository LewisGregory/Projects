import random
subject = ["the dog", "the cat", "the person", "the blue chair", "Darthvader", "the city", "the grapes", "the grape", "Lewis", "the monkewy"]
action = ["climbed", "bullied", "fought", "saved", "visited" "painted"]
adjective = ["hurridly", "heroicly", "scardely", "sadly", "happily"]
subjecttwo = ["a mountain", "a drag queen", "the kitcken table", "the door", "A taxi driver"]
#here i am selecting a random subject
selectedSub = subject[random.randint(0, len(subject)-1)]
#here i am selecting a random action
selectedAct = action[random.randint(0, len(action)-1)]
#here i am selecting a random adjective
selectedAdj = adjective[random.randint(0, len(adjective)-1)]
#here i am selecting a second subjective
selectedtwosub = subjecttwo[random.randint(0, len(subjecttwo)-1)]
#here i have built a sentence using a basic outline of: subject1 + action + ssubject2 + adjective  
sentence = selectedSub +" "+selectedAct +" " + selectedtwosub + " " + selectedAdj
print(sentence)
