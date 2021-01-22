from tkinter import *
import random
skoor= 0
skoor2=0

def arvuti():
    global skoor2
    taring= random.randint(1,6)
    print(taring)
    louend2.create_rectangle(30,30,230,230,fill="white",outline="black")
   
    if taring ==1:
        skoor2 +=1
        louend2.create_oval(120,120,140,140,fill="black",outline="black")
    elif taring==2:
        louend2.create_oval(70,70,90,90,fill="black",outline="black")
        louend2.create_oval(170,170,190,190,fill="black",outline="black")
        skoor2+=2
    elif taring==3:
        louend2.create_oval(70,70,90,90,fill="black",outline="black")
        louend2.create_oval(170,170,190,190,fill="black",outline="black")
        louend2.create_oval(120,120,140,140,fill="black",outline="black")
        skoor2+=3
    elif taring==4:
        louend2.create_oval(70,70,90,90,fill="black",outline="black")
        louend2.create_oval(170,170,190,190,fill="black",outline="black")
        louend2.create_oval(170,70,190,90,fill="black",outline="black")
        louend2.create_oval(70,170,90,190,fill="black",outline="black")
        skoor2+=4
    elif taring==5:
        louend2.create_oval(70,70,90,90,fill="black",outline="black")
        louend2.create_oval(170,170,190,190,fill="black",outline="black")
        louend2.create_oval(170,70,190,90,fill="black",outline="black")
        louend2.create_oval(70,170,90,190,fill="black",outline="black")
        louend2.create_oval(120,120,140,140,fill="black",outline="black")
        skoor2+=5
    elif taring==6:
        louend2.create_oval(70,70,90,90,fill="black",outline="black")
        louend2.create_oval(170,170,190,190,fill="black",outline="black")
        louend2.create_oval(170,70,190,90,fill="black",outline="black")
        louend2.create_oval(70,170,90,190,fill="black",outline="black")
        louend2.create_oval(170,120,190,140,fill="black",outline="black")
        louend2.create_oval(70,120,90,140,fill="black",outline="black")
        skoor2+=6
    print(skoor)
    silt= Label(aken, text=f"{skoor2}")
    silt.grid(row=3,column=1)
    
def roll():
    global skoor
    taring= random.randint(1,6)
    print(taring)
    louend.create_rectangle(30,30,230,230,fill="white",outline="black")
   
    if taring ==1:
        skoor +=1
        louend.create_oval(120,120,140,140,fill="black",outline="black")
    elif taring==2:
        louend.create_oval(70,70,90,90,fill="black",outline="black")
        louend.create_oval(170,170,190,190,fill="black",outline="black")
        skoor+=2
    elif taring==3:
        louend.create_oval(70,70,90,90,fill="black",outline="black")
        louend.create_oval(170,170,190,190,fill="black",outline="black")
        louend.create_oval(120,120,140,140,fill="black",outline="black")
        skoor+=3
    elif taring==4:
        louend.create_oval(70,70,90,90,fill="black",outline="black")
        louend.create_oval(170,170,190,190,fill="black",outline="black")
        louend.create_oval(170,70,190,90,fill="black",outline="black")
        louend.create_oval(70,170,90,190,fill="black",outline="black")
        skoor+=4
    elif taring==5:
        louend.create_oval(70,70,90,90,fill="black",outline="black")
        louend.create_oval(170,170,190,190,fill="black",outline="black")
        louend.create_oval(170,70,190,90,fill="black",outline="black")
        louend.create_oval(70,170,90,190,fill="black",outline="black")
        louend.create_oval(120,120,140,140,fill="black",outline="black")
        skoor+=5
    elif taring==6:
        louend.create_oval(70,70,90,90,fill="black",outline="black")
        louend.create_oval(170,170,190,190,fill="black",outline="black")
        louend.create_oval(170,70,190,90,fill="black",outline="black")
        louend.create_oval(70,170,90,190,fill="black",outline="black")
        louend.create_oval(170,120,190,140,fill="black",outline="black")
        louend.create_oval(70,120,90,140,fill="black",outline="black")
        skoor+=6
        
def k():
    roll()
    arvuti()
    
    print(skoor)
    silt= Label(aken, text=f"{skoor}")
    silt.grid(row=3,column=0)
    
    
aken = Tk()
aken.geometry("1000x500")
aken.title("Hasartmäng")
louend = Canvas(aken, width=300, height=300)
louend.grid(row=1,column=0)
louend2 = Canvas(aken, width=300, height=300)
louend2.grid(row=1,column=1)

nupp = Button(aken, text="Veereta",command=k)
nupp.grid(row=0,column=0)

silt1= Label(aken, text=f"Skoor:")
silt1.grid(row=2,column=0)

silt1= Label(aken, text=f"Arvuti skoor:")
silt1.grid(row=2,column=1)



