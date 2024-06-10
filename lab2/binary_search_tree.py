class Tree:

    def __init__(self,val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    
    def isempty(self):
        return (self.value == None)
    
    def insert(self,data):
      
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
            
        elif data < self.value:
            self.left.insert(data)
            return
          
        elif data > self.value:
            self.right.insert(data)
            
        elif data == self.value:
            return

    def find(self, v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

# Example usage
t = Tree(20)
t.insert(15)
t.insert(25)
t.insert(8)
t.insert(16)
print(t.find(33))
print(t.inorder())
