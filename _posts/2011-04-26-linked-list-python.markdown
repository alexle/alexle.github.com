---
layout: post
title: "'Write a linked list in python..'"
date: 2011-04-26
---

The first time I heard this, my heart stopped for a couple seconds.

I knew the algorithm. I had reviewed and implemented it the night before. I even slept on my notes to harness the power of osmosis. But implementing one in an interview/test is a different experience.

Like many other things in life, it's hard to see what all the fuss was about. Here is a break down of the algorithm and code:

## 1. Define A Node Class ##

Every Node has a value and a pointer to the next node. When a node is first created, it's assigned a given value and does not point to any other node.

``` python
class Node:
   def __init__( self, data ):
      self.data = data
      self.next = None
```

## 2. Define A LinkedList Class ##

The LinkedList class will hold all our nodes. It's responsible for keeping track (via pointers) of the first (head) and last (tail) node in the list. It also contains functions to add/remove nodes and display the list. A linked list is empty when created; thus there are no "head" or "tail" nodes at this point.

``` python
class LinkedList:
   def __init__( self ):
      self.head = None
      self.tail = None

   def AddNode( self, data ):
   ..
   def RemoveNode( self, index ):
   ..
   def PrintList( self ):
```

## 3. The Add Node Method ##

Adding a node to a linked list takes a couple steps.

1. Create a node. If it is the first node, set the 'head' pointer to it.
2. If a Tail exists, update its 'next' pointer to the new node. This keeps the nodes linked.
3. Assign the new node to be the Tail node.

``` python
def AddNode( self, data ):
   new_node = Node( data )

   if self.head == None:
      self.head = new_node

   if self.tail != None:
      self.tail.next = new_node

   self.tail = new_node
```

## 4. The Remove Node Method ##

To remove a node from the linked list, we must keep track of *two* nodes - the node we're attempting to remove, and the previous node before it. This is to be able to re-stitch the list back together after removing a node.

1. Iterate through the list to find the node to remove.
2. Create pointers to keep track of the previous and current node.
3. Once the node to remove is reached, the previous node 'next' pointer is changed to *skip* the current node and point to the current 'next' instead.
4. If the Head node is removed, update the Head to be the 'next' node.

Note there are two corner cases here. If the list only has one node, then there is no "prev" node. Also, if the first item in the list is being removed, there also wouldn't be a "prev" node.

``` python
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
```

## 5. Printing The Linked List ##

To print the list, start at the head pointer. Traverse the list through each node's "next" pointer, displaying its data member, until the node is no longer null.<br />

``` python
def PrintList( self ):
   node = self.head

   while node != None:
      print node.data
      node = node.next
```

And there you go, a linked list with functions to add, remove, and print the list. The full source code above can also be found on my github <a href="https://github.com/alexle/Linked-List/blob/master/linked.py">here</a>.<br />

---------

Alternatively, you could use python's built-in list library..<br />

``` python
List = []

List.append(1)
List.append(2)
List.append(3)
List.append(4)

for i in List:
   print i
```

Makes this problem pretty trivial huh? Go python!
