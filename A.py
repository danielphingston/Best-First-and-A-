import os
dir = os.path.dirname(os.path.realpath(__file__))

Graph=eval(open(dir+"\close.txt").read())
Hur=(eval(open(dir+"\heuristic.txt").read()))
path=(eval(open(dir+"\path.txt").read()))

Hur=dict(sorted(Hur.items(),key=lambda x:x[1],reverse=True))
class node:    
    def __init__(self,n=None,prev=None,path=0):
        self.name=n
        self.prev=prev
        self.value=Hur[self.name]
        self.path=path
        
    def update(self,wt):
        s1=self.prev.name+self.name      
        if s1 not in path:
            s1=s1[::-1]        
        s1=path[s1]
        self.value=round(s1+self.value+wt,4)
        self.path=s1+wt

CLOSED={}
start,goal=input("Enter the start and goal no space:")
start=start.upper()
goal=goal.upper()
print(type(start))
goal.upper()
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
            n.update(current[1].path)
            if n.name not in OPEN and n.name not in CLOSED:
                OPEN[n.name]=n
            elif n.name in OPEN and n.value< OPEN[n.name].value:
                OPEN[n.name]=n
            elif n.name in CLOSED and n.value<CLOSED[n.name].value:                
                OPEN[n.name]=n
                CLOSED.pop(n.name)                      
        CLOSED[current[0]]=current[1]  
        print("open:")
        for i,j in OPEN.items():            
            print(i,j.value,end=' ')
        print("\nclosed")
        for i,j in CLOSED.items():
            print(i,j.value,end=" ")  
        input("\nPress Enter to continue...")
print("NO PATH FOUND ")


        
            
        
    

    



