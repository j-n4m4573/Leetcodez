"""
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.

What clarifying questions would you ask?

Could you demonstrate what is meant by rotating the ll?
    What are the properties each node contains? 
    Is this a singly or doubly linked list?
    What are the given time and space constraints?

What reasonable assumptions could you state?
	That the ll can contain integers and strings. 
	That empty is a valid ll. 
	That the ll has a head and tail properties. 
What are 2-3 ways you can simplify the problem?
    We could simplify the problem by manually rotating values on a clock to see how number positions would change. 
    We could use a small number list(i.e three numbers). 

Brainstorm 2-3 ways to approach the problem.
	Take numbers in the ll and move tail to head n times. 
	Unpack the ll, and rotate the number positions.
	
Choose one idea and write pseudocode for it.
    Start at the head of the ll, figure out the number of rotations 
    Move the tail to the head k number of times
    Return ll. 

"""

class ListNode:
    def __init__(self, value=None):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0 

    # Time Complexity:
    # Auxiliary Space Complexity:
    def append(self, value):
        # create new node 
        new_node = ListNode(value)

        # Check if this linked list is empty
        if self.head is None:
            # Assign head to new node
            self.head = new_node
            self.length += 1
        else:
            self.head.next = new_node
            self.length += 1
        # Update tail to new node regardless
        self.tail = new_node
        # if last item set as tail

   
    def insert(self, value, index):
        for node in range(0, index): 
            node = node.next
            print(node) 
    
def rotate_ll(llist, k):
    ll_list = []
    new_node = llist.head
    #create a list from ll
    while node is not none: 
         ll_list.append(node.data)
         node = node.next
    # Start at the head of the ll, figure out the number of rotations 
    for _ in range(0,k): 
        temp_tail = ll_list[-1]
        del ll_list[-1]
        ll_list[0] = temp_tail
   return ll_list 

   """
   Given an array of k singly-linked lists, each of whose values 
   are in sorted order, combine all nodes (do not create new nodes) 
   into one singly-linked list with all values in order.
   """

   def singly_fr_multiple(arr): 
       ll_list = []
       new_ll = LinkedList()

       for item in arr:
           for node in item: 
               ll_list.append(node.data)
        
        ll_list.sort()

        for item in ll_list:
            new_ll.append(item) 
            
        return new_ll
            
           