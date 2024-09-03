from collections import defaultdict

class Node:
    def __init__(self,name,par=None) -> None:
        self.name=name
        self.par=par
    def display(self):
        print (self.name)

data=defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']

def equal(A,O):     #kiem tra gia tri
    return A.name==O.name

def checkInArray(tmp,list):     # ktra ton tai trong list
    for i in list:
        if equal (tmp,i):
            return True
    return False

def path(A):
    print (A.name)
    if (A.par!= None):
        path(A.par)

def DFS(S=Node('A'),G=Node('M')):
    Open=[]
    Close=[]
    Open.append(S)
    print ("duyet")
    while True:
        if len(Open)==0:
            print("Loi")
            return
        O=Open.pop(0)
        Close.append(O)
        print (O.name)
        if equal(O,G):
            print ("Thanh cong")
            path(O)
            return
        pop=0
        for x in data[O.name]:
            tmp=Node(x,O)
            if not checkInArray(tmp, Open) and not checkInArray(tmp, Close):
                Open.insert(pop,tmp)
                pop+=1

DFS()
    