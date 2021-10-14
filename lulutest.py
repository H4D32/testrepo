class Node:

    def __init__(self, element, parent = None,  left = None, right = None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right

class LBTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def add_root(self,e):
        self.size = 1
        self.root = Node(e)
        return self.root
    
    def add_left(self,p,e):
        self.size += 1
        p.left = Node(e,p)
        return p.left

    def add_right(self, p, e):
        self.size += 1
        p.right = Node(e, p)
        return p.right

def DFSearch(t):
    if t:
        print(t.element)
    if(t.left is None) and (t.right is None):
        return
    else:
        if t.left is not None:
            DFSearch(t.left)
        if t.right is not None:
            DFSearch(t.right)

def main (): 
    t = LBTree() 
    t.add_root(10) 
    t.add_left(t.root,20)
    t.add_right(t.root,30) 
    t.add_left(t.root.left, 40) 
    t.add_right(t.root.left, 50) 
    t.add_left(t.root.right, 60) 
    t.add_right(t.root.left.left, 70) 
    # print (t.root.element) 
    # print (t.root.left.element) 
    # print (t.root.right.element) 
    # print (t.root.left.right.element)

    DFSearch(t.root)



main()
