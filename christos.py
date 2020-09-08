#if we both keep quiet 1 year each  // if both speak 2 years each // if only one you get 0 other gets 3 //
#percentage chance both keep quiet? --- 
#percentage chance both talks? ---
import random
#class type prisoner for experiment
class prisoner:
    def __init__(self, name, decisions,safe, c_decision):
        self.name = name
        self.decisions = [None,None]
        self.safe = False
        self.c_decision = None

#declare 2 prisoners with empty values
p1 = prisoner("p1",None,False,None)
p2 = prisoner("p2",None,False,None)

#list of the 2 possible choices
choices = ["keep quiet", "rat the other out"]
#empty win condition
winner = None
#counter of the rounds of the dilemma
counter = 0

#checks if a prisoners past two choices where to keep quiet 
def Check(prisoner):
    if prisoner.safe == False:
        if prisoner.decisions[-1] == "keep quiet" and prisoner.decisions[-2] == "keep quiet":
            prisoner.safe = True
            return True
        else:
            return False

#makes the choice for a prisoner, contains a check for the end and will return if so 
def make_choice(person, other,win):
    if win != None:
        return win
    else:
        if Check(other) != True:   
            Cd = choices[random.randint(0,1)]
            person.c_decision = Cd
            person.decisions.append(Cd)
            return None
        else:
            person.c_decision = "keep quiet"
            person.decisions.append("keep quiet")
            person.safe = True
            winner = f"{person.name} kept quiet twice and {other.name} learned"
            return winner

#loop for the dilemma to continue until one prisoner has learned to cooperate with the other to keeo quiet 
while True:
    #win condition check
    if p1.safe and p2.safe:
        print("-----------------------------------------\n")
        print(f"first person chose to finally keep quiet")
        print(f"second person chose to finally keep quiet")
        break
    #checking if someone has learned
    winner= make_choice(p1,p2,winner)
    winner= make_choice(p2,p1,winner)
    counter+=1
    #dilemma print outs per round 
    print(f"This is dilemma test {counter}\n")
    print(f"first person chose {p1.c_decision}")
    print(f"second person chose {p2.c_decision}\n")
#The final dilemma print outs 
print(winner)
print(f"The dilemma played out {counter} many times")
print("both kept quiet\n")
print(p1.decisions)
print(p2.decisions)
