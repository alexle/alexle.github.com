"Write a linked list in python.."
04-26-2011

The first time I heard this, my heart stopped for a couple seconds.

I knew the algorithm. I had reviewed and implemented it the night before. I even slept on my notes to harness the power of osmosis. But implementing one in an interview/test is a different experience.

Like many other things in life, it's hard to see what all the fuss was about. Linked lists are easy and I hope the walk-through below helps.

###1) Define a Node class###

Every Node has a value and a pointer to the next node. When a node is first created, it's assigned a given value and does not point to any node.

<div id="code">
<font color="#f0e68c"><b>class</b></font>&nbsp;<font color="#98fb98">Node</font>:<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">__init__</font>( self, data ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.data = data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.next = None<br>
</div>

###2) Define a LinkedList class###

In this example, LinkedList holds a pointer to the first (head) and last (tail) node in the list. It also contains functions to later add/remove nodes and display the list. A linked list is empty when created; thus there are no "head" or "tail" nodes at this point.

<div id="code">
<font color="#f0e68c"><b>class</b></font>&nbsp;<font color="#98fb98">LinkedList</font>:<br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">__init__</font>( self ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.head =&nbsp;<font color="#98fb98">None</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.tail =&nbsp;<font color="#98fb98">None</font><br>
<br>
&nbsp;&nbsp;def AddNode( self, data ):<br />
&nbsp;&nbsp;..<br />
&nbsp;&nbsp;def RemoveNode( self, index ):<br />
&nbsp;&nbsp;..<br />
&nbsp;&nbsp;def PrintList( self ):<br />
</div>

###3) Create Add and Remove node methods###

Adding a node to a linked list takes a couple steps.

1. Create a node.
2. Set the current last node's 'next' pointer to this node. This keeps the nodes linked.
3. Set the current tail pointer to the new node. If it's the first node (head = none), also set the head pointer to this node.

<div id="code">
&nbsp;&nbsp; <font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">AddNode</font>( self, data ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new_node = Node( data )<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;self.head == None:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.head = new_node<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;self.tail != None:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.tail.next = new_node<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.tail = new_node<br>
</div>

To remove a node from the linked list..<br />

<div id="code">
&nbsp;&nbsp; <font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">RemoveNode</font>( self, index ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prev = None<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node = self.head<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i = 0<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>while</b></font>&nbsp;( node != None ) <font color="#f0e68c"><b>and</b></font>&nbsp;( i &lt; index ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prev = node<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; node = node.next<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;prev == None:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.head = node.next<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>else</b></font>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prev.next = node.next<br>
</div>

###4) Printing the Linked List###

To print the list, start at the head pointer. Traverse the list through each node's "next" pointer until the node is no longer null.<br />

<div id="code">
&nbsp;&nbsp; <font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">PrintList</font>( self ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node = self.head<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>while</b></font>&nbsp;node != None:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color="#f0e68c"><b>print</b></font>&nbsp;node.data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; node = node.next<br>
</div>

And there you go, a linked list with functions to add, remove, and print the list. The full source code above can also be found on my github <a href="https://github.com/alexle/Linked-List/blob/master/linked.py">here</a>.<br />

---------

Alternatively, you could use python's built-in list library..<br />

<div id="code">
List = []<br>
<br>
List.append(1)<br>
List.append(2)<br>
List.append(3)<br>
List.append(4)<br>
<br>
<font color="#f0e68c"><b>for</b></font>&nbsp;i <font color="#f0e68c"><b>in</b></font>&nbsp;List:<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>print</b></font>&nbsp;i<br>
</div>

Makes this problem pretty trivial huh? Go python!
