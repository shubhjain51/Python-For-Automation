class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:

    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root == None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if (new_node.value < temp.value):
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp= temp.left
                
            if (new_node.value> temp.value):
                if temp.right is None:
                    temp.right= new_node
                    return True
                temp=temp.right

            if (new_node.value == temp.value):
                return False



my_binary_tree= BinarySearchTree()
my_binary_tree.insert(2)
my_binary_tree.insert(1)
my_binary_tree.insert(3)

print(my_binary_tree.root.value)
print(my_binary_tree.root.left.value)
print(my_binary_tree.root.right.value)