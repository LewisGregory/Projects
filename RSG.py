import random
subject = ["the dog", "the cat", "the person", "the blue chair", "Darthvader", "the city", "the grapes", "the grape", "Lewis", "the monkewy"]
action = ["climbed", "bullied", "fought", "saved", "visited" "painted"]
adjective = ["hurridly", "heroicly", "scardely", "sadly", "happily"]
subjecttwo = ["a mountain", "a drag queen", "the kitcken table", "the door", "A taxi driver"]
selectedSub = subject[random.randint(0, len(subject)-1)]
selectedAct = action[random.randint(0, len(action)-1)]
selectedAdj = adjective[random.randint(0, len(adjective)-1)]
selectedtwosub = subjecttwo[random.randint(0, len(subjecttwo)-1)]

sentence = selectedSub +" "+selectedAct +" " + selectedtwosub + " " + selectedAdj
print(sentence)
