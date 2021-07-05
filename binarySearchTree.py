class node():
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value


class binarySearchTree():
    def __init__(self):
        self.main = None

    def insertNode(self, value):
        if self.main == None:
            self.main = node(value)
        else:
            self.insertRecursive(value, self.main)
            
    def insertRecursive(self, value, lastRoot):
        if value > lastRoot.val:
            if lastRoot.right != None:
                self.insertRecursive(value, lastRoot.right)
            else:
                lastRoot.right = node(value)
        elif value < lastRoot.val:
            if lastRoot.left != None:
                self.insertRecursive(value, lastRoot.left)
            else:
                lastRoot.left = node(value)

    def inorder(self):
        print("In-order search;")
        self.inorderRec(self.main)

    def inorderRec(self, root):
        if root == None:
            return
        self.inorderRec(root.left)
        print(root.val)
        self.inorderRec(root.right)

    def preorder(self):
        print("Pre-order search;")
        self.preorderRec(self.main)

    def preorderRec(self, root):
        if root == None:
            return
        print(root.val)
        self.preorderRec(root.left)
        self.preorderRec(root.right)

    def findValue(self, value):
         if self.main == None:
            return(0)
         else:
            root = self.findValueRec(value, self.main)

    def findValueRec(self, value, root):
        if value == root.val:
            print("Found it!")
            return(root)
        elif value > root.val:
            if root.right != None:
                self.findValueRec(value, root.right)
            else:
                print("Did not find it . . . ")
                return(0)
        elif value < root.val:
            if root.left != None:
                self.findValueRec(value, root.left)
            else:
                print("Did not find it . . . ")
                return(0)





r = binarySearchTree()
r.insertNode(12)
r.insertNode(13)
r.insertNode(11)
r.insertNode(6)
r.insertNode(16)
r.insertNode(9)


r.inorder()
print("")
r.preorder()

r.findValue(6)
r.findValue(5)
r.findValue(13)
r.findValue(4)