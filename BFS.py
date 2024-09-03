from collections import defaultdict

class Node:
    def __init__(self, name, par=None) -> None:
        self.name = name  # Value
        self.par = par    # Parent

    def display(self):
        print(self.name)

data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']

def equal(O, G):  # Check equality
    return O.name == G.name

def checkInArray(tmp, Open):  # Check if a node is in a list
    for x in Open:
        if equal(x, tmp):
            return True
    return False

def path(O):  # Display the path from the root to the current node
    if O.par is not None:
        path(O.par)
    print(O.name, end=' ')

def BFS(S=Node('A'), G=Node('M')):
    Open = []

    Close = []
    Open.append(S)  # Add the root node
    print("duyet")
    while True:
        if len(Open) == 0:  # Check if Open is empty
            print("That bai")
            return
        O = Open.pop(0)  # Remove the first element from Open
        Close.append(O)  # Add it to Close
        print(O.name)
        if equal(O, G):
            print("Thanh cong")
            path(O)
            return
        for x in data[O.name]:
            tmp = Node(x, O)
            if not checkInArray(tmp, Open) and not checkInArray(tmp, Close):
                Open.append(tmp)

BFS()
