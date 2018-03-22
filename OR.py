import os
dir = os.path.dirname(os.path.realpath(__file__))

Graph=eval(open(dir+"\close.txt").read())
Hur=(eval(open(dir+"\heuristic.txt").read()))

class node:    
    def __init__(self,n=None,prev=None):
        self.name=n
        self.prev=prev
        self.value=Hur[self.name]
CLOSED={}
start,goal=input("Enter the start and goal:")
start=start.upper()
goal=goal.upper()
current=node(start)
OPEN={}
l={current.name:current}
OPEN.update(l)
while OPEN:
    lk=500
    for key,val in OPEN.items():
        if val.value<lk:
            lk=val.value
            low=val.name        
    current=OPEN.pop(low)   
    current=[current.name,current]
    print("Current node:",current[0]) 
    if(current[0]==goal):
        print("goal",current[0])
        current=current[1]
        l=[]
        while current.prev!=None:
            l.append(current.name)
            current=current.prev
        l.append(current.name)  
        l.reverse()
        print("PATH:") 
        input("->".join(l))		
        quit()
    else:
        for i in Graph[current[0]]:            
            n=node(i)
            n.prev=current[1]            
            if n.name not in OPEN and n.name not in CLOSED:
                OPEN[n.name]=n                         
        CLOSED[current[0]]=current[1]  
        print("open:")
        for i,j in OPEN.items():            
            print(i,j.value,end=' ')
        print("\nclosed")
        for i,j in CLOSED.items():
            print(i,j.value,end=" ")  
        input("\nPress Enter to continue...")
print("NO PATH FOUND ")


        
            
        
    

    



