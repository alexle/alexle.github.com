"Write a linked list in python.."
04-26-2011

The first time I heard this, my heart stopped for a couple seconds.

I knew the algorithm. I had reviewed and implemented it the night before. I even slept on my notes to harness the power of osmosis. But implementing one in an interview/test is a different experience.

Like many other things in life, it's hard to see what all the fuss was about. Linked lists are easy and I hope the walk-through below helps.

Define a Node class. Every Node has a value and a pointer to the next node. When a node is first created, it's assigned a given value and does not point to any node.
class Node:
  def __init__( self, data ):
    self.data = data
    self.next = None
Define a LinkedList class. In this example, LinkedList holds a pointer to the first (head) and last (tail) node in the list. It also contains functions to later add/remove nodes and display the list. A linked list is empty when created; thus there are no "head" or "tail" nodes at this point.
class LinkedList:
  def __init__( self ):
    self.head = None
    self.tail = None

  def AddNode( self, data ):
  ..
  def RemoveNode( self, index ):
  ..
  def PrintList( self ):
  ..
Adding a node to a linked list takes a couple steps.
Create a node.
Set the current last node's 'next' pointer to this node. This keeps the nodes linked.
Set the current tail pointer to the new node. If it's the first node (head = none), also set the head pointer to this node.
def AddNode( self, data ):
  new_node = Node( data )

  if self.head == None:
    self.head = new_node

  if self.tail != None:
    self.tail.next = new_node

  self.tail = new_node
To remove a node from the linked list..
def RemoveNode( self, index ):
  prev = None
  node = self.head
  i = 0

  while ( node != None ) and ( i < index ):
    prev = node
    node = node.next
    i += 1

  if prev == None:
    self.head = node.next
  else:
    prev.next = node.next
To print the list, start at the head pointer. Traverse the list through each node's "next" pointer until the node is no longer null.
def PrintList( self ):
  node = self.head
  while node != None:
    print node.data
    node = node.next
Now the program is ready. Create a linked list, add some nodes, and see what the list contains.
List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(4)
List.PrintList( )
Remove the node at index 2 and see what the list looks like now.
List.RemoveNode( 2 )
List.PrintList( )
And there you go, a linked list with functions to add, remove, and print the list. The full source code above can also be found on my github here.


Alternatively, you could use python's built-in list library..
List = []
List.append(1)
List.append(2)
List.append(3)
List.append(4)

for i in List:
     print i

Makes this problem pretty trivial huh? Go python!
