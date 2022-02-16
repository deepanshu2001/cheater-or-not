import random;

n=int(input("Enter the number who's multiplication number you need:"))
Wtable=[]
def DeepanshuMultiplication():
   
    randNo=random.randint(0,n*11)
    rano=random.randint(0,10)
    for i in range(1,11):
        Wtable.append(n*i)
    if rano%2==0:
        rand=random.randint(0,len(Wtable))
        Wtable[rand]=randNo
    elif rano%2!=0:
        pass
    
    print(Wtable)
   
        
def isCorrect():
    Ctable=[]
    for j in range(1,11):
        Ctable.append(n*j)
    

    for item in range(len(Ctable)):
        if Ctable[item]==Wtable[item]:
            print("Checking the table----")

            
            #print("Deepanshu table is right.He did not cheat")
        elif Ctable[item]!=Wtable[item]:
            print("Deepanshu's table is wrong.HE cheated")
            print(f"He gave the value of {Ctable[item]} wrong!")
            
            break


DeepanshuMultiplication()
isCorrect()
