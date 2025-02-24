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
            
    def contains(self,value):
        temp=self.root
        while (temp is not None):
            if value<temp.value:
                temp= temp.left
            if value>temp.value:
                temp= temp.right
            else:
                return True
        return False



my_binary_tree= BinarySearchTree()
my_binary_tree.insert(47)
my_binary_tree.insert(21)
my_binary_tree.insert(76)
my_binary_tree.insert(18)
my_binary_tree.insert(27)
my_binary_tree.insert(52)
my_binary_tree.insert(82)



print(my_binary_tree.contains(27))
print(my_binary_tree.contains(17))

print(my_binary_tree.root.value)
print(my_binary_tree.root.left.value)
print(my_binary_tree.root.left.left.value)
print(my_binary_tree.root.left.right.value)
print(my_binary_tree.root.right.value)
print(my_binary_tree.root.right.left.value)
print(my_binary_tree.root.right.right.value)


