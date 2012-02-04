"Write a linked list in python.."
04-26-2011

The first time I heard this, my heart stopped for a couple seconds.

I knew the algorithm. I had reviewed and implemented it the night before. I even slept on my notes to harness the power of osmosis. But implementing one in an interview/test is a different experience.

Like many other things in life, it's hard to see what all the fuss was about. Linked lists are easy and I hope the walk-through below helps.

Define a Node class. Every Node has a value and a pointer to the next node. When a node is first created, it's assigned a given value and does not point to any node.</div><div><blockquote>class Node:<br />
&nbsp;&nbsp;def __init__( self, data ):<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.data = data<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.next = None</blockquote>Define a LinkedList class. In this example, LinkedList holds a pointer to the first (head) and last (tail) node in the list. It also contains functions to later add/remove nodes and display the list. A linked list is empty when created; thus there are no "head" or "tail" nodes at this point.<br />
<blockquote>class LinkedList:<br />
&nbsp;&nbsp;def __init__( self ):<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.head = None<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.tail = None<br />
<br />
&nbsp;&nbsp;def AddNode( self, data ):<br />
&nbsp;&nbsp;..<br />
&nbsp;&nbsp;def RemoveNode( self, index ):<br />
&nbsp;&nbsp;..<br />
&nbsp;&nbsp;def PrintList( self ):<br />
&nbsp;&nbsp;..</blockquote>Adding a node to a linked list takes a couple steps.<br />
<ol><li>Create a node.</li>
<li>Set the current last node's 'next' pointer to this node. This keeps the nodes linked.</li>
<li>Set the current tail pointer to the new node. If it's the first node (head = none), also set the head pointer to this node.</li>
</ol><blockquote>def AddNode( self, data ):<br />
&nbsp;&nbsp;new_node = Node( data )<br />
<br />
&nbsp;&nbsp;if self.head == None:<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.head = new_node<br />
<br />
&nbsp;&nbsp;if self.tail != None:<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.tail.next = new_node<br />
<br />
&nbsp;&nbsp;self.tail = new_node</blockquote>To remove a node from the linked list..<br />
<blockquote>def RemoveNode( self, index ):<br />
&nbsp;&nbsp;prev = None<br />
&nbsp;&nbsp;node = self.head<br />
&nbsp;&nbsp;i = 0<br />
<br />
&nbsp;&nbsp;while ( node != None ) and ( i &lt; index ):<br />
&nbsp;&nbsp;&nbsp;&nbsp;prev = node<br />
&nbsp;&nbsp;&nbsp;&nbsp;node = node.next<br />
&nbsp;&nbsp;&nbsp;&nbsp;i += 1<br />
<br />
&nbsp;&nbsp;if prev == None:<br />
&nbsp;&nbsp;&nbsp;&nbsp;self.head = node.next<br />
&nbsp;&nbsp;else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;prev.next = node.next</blockquote>To print the list, start at the head pointer. Traverse the list through each node's "next" pointer until the node is no longer null.<br />
<blockquote>def PrintList( self ):<br />
&nbsp;&nbsp;node = self.head<br />
&nbsp;&nbsp;while node != None:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print node.data<br />
&nbsp;&nbsp;&nbsp;&nbsp;node = node.next</blockquote>Now the program is ready. Create a linked list, add some nodes, and see what the list contains.<br />
<blockquote>List = LinkedList()<br />
List.AddNode(1)<br />
List.AddNode(2)<br />
List.AddNode(3)<br />
List.AddNode(4)<br />
List.PrintList( )</blockquote>Remove the node at index 2 and see what the list looks like now.<br />
<blockquote>List.RemoveNode( 2 )<br />
List.PrintList( )</blockquote>And there you go, a linked list with functions to add, remove, and print the list. The full source code above can also be found on my github <a href="https://github.com/alexle/Linked-List/blob/master/linked.py">here</a>.<br />
<br />
<hr /><br />
Alternatively, you could use python's built-in list library..<br />
<blockquote>List = []<br />
List.append(1)<br />
List.append(2)<br />
List.append(3)<br />
List.append(4)<br />
<br />
for i in List:<br />
&nbsp; &nbsp; &nbsp;print i</blockquote>

Makes this problem pretty trivial huh? Go python!
