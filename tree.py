#basic tree creation,finding height
#traversing tree in inorder,preorder,postorder
#level order traversal
#searching in tree
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,data):
        if not self.data:
            self.data=Node(data)
        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        elif data>self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def printTree_desc(self):
        if self.right:
            self.right.printTree_desc()
        print(self.data)
        if self.left:
            self.left.printTree_desc()

    def search(self,data):
        if data==self.data:
            return "item founded"
        elif data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return "item is not founded in the tree"
        elif data>self.data:
            if self.right:
                return self.right.search(data)
            else:
                return "item is not founded in the tree"
        else:
            return "item is not founded in the tree"

            
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def levelordertraversal(root):
    h=height(root)
    for i in range(0,h+1):
        def printlevelorder(root,level):
            if root is None:
                return 
            elif level==0:
                print(root.data,end=" ")
            elif level>0:
                printlevelorder(root.left,level-1)
                printlevelorder(root.right,level-1)
        printlevelorder(root,i)

#another way for level order traversal
def levelOrder(root):
    queue=[]
    queue.append(root)
    while len(queue)>0:
        current=queue.pop(0)
        print(current.data,end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def height(root):
    if root is None:
        return -1
    else:
        lheight=height(root.left)
        rheight=height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1


root=Node(int(input("Enter value of root node:")))
root.insert(8)
root.insert(4)
root.insert(9)
root.insert(30)
root.insert(17)
root.insert(36)
#root.printTree()
#inorder(root)
#print(root.search(8))
#root.printTree_desc()
#print(height(root))
#print(findheight(root))
#levelordertraversal(root)
levelOrder(root)