#Rihard Raba 20.12.2020
#OSA1 mängust
#Kasutaja sisestab kuhu panna punktid ja salvestab need eraldi faili,kui fail eksisteerib siis loeb sealt atribuudid.






#impordib vajalikud moodulid
import json
import os.path
import random
#muutajad mida on hiljem vaja
name = ""
save = ""
#dictionary milles on vajalikud atribuudid
attributes = {"health":0,"strength":0,"speed":0,"magic attack":0}

#loob definitsiooni
def createCharacter(name, attributes):
    #küsib kasutjalt nime
    name = input("Enter your name: ")
    #punktide arv mida saab muuta vajadusel
    skill=20
   #vaatab kas kasutaja sisestatud nimega fail eksisteerib,kui mitte siis loob uue kasutaja
    if os.path.isfile(f"{name}.txt"):
        with open(f"{name}.txt") as f:
            data = f.read()
        attributes = json.loads(data)
        #prindib attribuudi et näha kas loeb faili õieti,saab eemaldada kui mäng valmis
        print(attributes["health"])
        return attributes
    else:
        
    
    #kuni punkte on üle 0 siis küsib kasutajalt kuhu punkte kulutada
        while skill>0:
            if skill<20:
                choice = int(input("(1.Health/2.Strength/3.Speed/4.Magic attack):"))
            else:
                choice = int(input("You can now use your skill points,Choose carefully as it affects your fighting ability: (1.Health/2.Strength/3.Speed/4.Magic attack)"))
            points = int(input(f"How many points would you like to add to that skill?(You have {skill} remaining): "))
        
        
        
        #lisab punktid valitud atribuudile,kui kasutaja tahab lisada rohkem punkte kui tal on siis see lisab kõik punktid mis alles
            if points>skill:
                if choice == 1:
                    attributes["health"] += skill
                elif choice == 2:
                    attributes["strength"] += skill
                elif choice == 3:
                    attributes["speed"] += skill
                elif choice == 4:
                    attributes["magic attack"] += skill
            else:
        
                if choice == 1:
                    attributes["health"] += points
                elif choice == 2:
                    attributes["strength"] += points
                elif choice == 3:
                    attributes["speed"] += points
                elif choice == 4:
                    attributes["magic attack"] += points
                else:
                    print("Error")
            skill -= points
            
        #salvestab punktid uute faili
        json.dump(attributes, open(f"{name}.txt", "w"))
        #funktsioon tagastab attribuudid
        return attributes



#def mäng prindib createCharacter nime ja attribuudid et näha kas kõik töötab
def game(character):
    print(character)
    dmg = character["strength"]*2
    magdmg = character["strength"]*3
    
    hp = character["health"]*10
    score= 0
    lvl= 1
    ehp = 40+(lvl*10)
    
    alive = 1
    while alive == 1:
        print(ehp)
        print(hp)
        while ehp>=0 and hp>=0:
            hit= random.randint(1,4)
            
            if hit > 1:
                damtype = random.randint(1,4)
                if damtype == 1:
                    ehp = ehp-magdmg
                    print(f"Enemy HP: {ehp}")
                else:
                    ehp = ehp-dmg
                    print(f"Enemy HP: {ehp}")
            else:
                print("Missed")
        
            ehit = random.randint(1,2)
            
            if ehit == 1:
                hp = hp - lvl
                print(f"HP remaining : {hp}")
            else:
                print("Dodged enemy attack")
        
        if hp>0:
            print(f"Level cleared | +{lvl} score")
            score = score + lvl
            lvl = lvl + 1
        else:
            print(f"You lose | Final score {score}")
            alive = 0
            
        ehp = 40+(lvl*10)
        hp = character["health"]*10
    
   
    
    
myCharacter = createCharacter(name, attributes)

game(myCharacter)