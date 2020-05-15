class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self, items=[]):
    self.root = None
    for item in items:
      self.append(item)
  
  def append(self, item):
    node = Node(item)
    if self.root == None: 
      self.root = node 
    else: 
      parent = self.find_parent_node(item)
      if item == parent.data: 
        return 
      if item < parent.data: 
        parent.left = node 
      else: 
        parent.right = node 
    
  # find parent of item or find item node
  def find_parent_node(self, item):
    current = self.root 
    while current != None: 
      # item already exists
      if item == current.data:
        return current
      if item < current.data: 
        # found solution
        if current.left == None: 
          return current
        # set to left node for iteration
        current = current.left 
      else: 
        if current.right == None: 
          return current 
        current = current.right 
  
  def print_tree(self, curr):
    if (curr == None):
      return
    
    self.print_tree(curr.left)
    print(curr.data)
    self.print_tree(curr.right)
  
  def __print__(self):
    self.print_tree(self.root)
    
# Search for given item k in a given BST
def search_in_BST(tree, item):
  # do something
  current = tree.root
  while current != None: 
    if item == current.data: 
      return True 
    elif item < current.data: 
      current = current.left 
    else: 
      current = current.right         
  return False
  
 

