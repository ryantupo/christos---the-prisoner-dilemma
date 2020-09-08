#if we both keep quiet 1 year each  // if both speak 2 years each // if only one you get 0 other gets 3 //
import random
#percentage chance both keep quiet? --- 


#percentage chance both talks? ---
class prisoner:
    def __init__(self, name, decisions,safe, c_decision):
        self.name = name
        self.decisions = [None,None]
        self.safe = False
        self.c_decision = None


#percentage chance only 1 talks --- 
p1 = prisoner("p1",None,False,None)
p2 = prisoner("p2",None,False,None)

choices = ["keep quiet", "rat the other out"]

def Check(prisoner):
    if prisoner.safe == False:
        if prisoner.decisions[-1] == "keep quiet" and prisoner.decisions[-2] == "keep quiet":
            prisoner.safe = True
            return True
        else:
            return False



count = 0

while True:
    
    if p1.safe and p2.safe:
        print(f"first person chose to finally keep quiet")
        print(f"second person chose to finally keep quiet")
        break
    


    if Check(p2) != True:   
        p1_CD = choices[random.randint(0,1)]
        p1.c_decision = p1_CD
        p1.decisions.append(p1_CD)
    else:
        p1.c_decision = "keep quiet"
        p1.decisions.append("keep quiet")
        p1.safe = True
        winner = "p2 kept quiet twice and p1 learned"
        

    if Check(p1) != True:
        p2_CD = choices[random.randint(0,1)]
        p2.c_decision = p2_CD
        p2.decisions.append(p2_CD)
    else:
        p2.c_decision = "keep quiet"
        p2.decisions.append("keep quiet")
        p2.safe = True
        winner = "p1 kept quiet twice and p2 learned"

        

    count +=1
    print(f"first person chose {p1.c_decision}")
    print(f"second person chose {p2.c_decision}")
    print("")

print("")
print(winner)
print(count)
print("both kept quiet")
print(p1.c_decision)
print(p2.c_decision)
print()

print(p1.decisions)
print(p2.decisions)
