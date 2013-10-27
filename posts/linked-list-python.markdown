"Write a linked list in python.."
04-26-2011

The first time I heard this, my heart stopped for a couple seconds.

I knew the algorithm. I had reviewed and implemented it the night before. I even slept on my notes to harness the power of osmosis. But implementing one in an interview/test is a different experience.

Like many other things in life, it's hard to see what all the fuss was about. Here is a break down of the algorithm and code:

###1. Define A Node Class###

Every Node has a value and a pointer to the next node. When a node is first created, it's assigned a given value and does not point to any other node.

<div id="code">
<font color="#f0e68c"><b>class</b></font>&nbsp;<font color="#98fb98">Node</font>:<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">__init__</font>( self, data ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.data = data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.next = None<br>
</div>

###2. Define A LinkedList Class###

The LinkedList class will hold all our nodes. It's responsible for keeping track (via pointers) of the first (head) and last (tail) node in the list. It also contains functions to add/remove nodes and display the list. A linked list is empty when created; thus there are no "head" or "tail" nodes at this point.

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

###3. The Add Node Method###

Adding a node to a linked list takes a couple steps.

1. Create a node. If it is the first node, set the 'head' pointer to it.
2. If a Tail exists, update its 'next' pointer to the new node. This keeps the nodes linked.
3. Assign the new node to be the Tail node.

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

###4. The Remove Node Method###

To remove a node from the linked list, we must keep track of *two* nodes - the node we're attempting to remove, and the previous node before it. This is to be able to re-stitch the list back together after removing a node.

1. Iterate through the list to find the node to remove.
2. Create pointers to keep track of the previous and current node.
3. Once the node to remove is reached, the previous node 'next' pointer is changed to *skip* the current node and point to the current 'next' instead.
4. If the Head node is removed, update the Head to be the 'next' node.

Note that there are two corner cases here. If the list only has one node, then there is no "prev" node. Also, if the first item in the list is being removed, there also wouldn't be a "prev" node.

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

###5. Printing The Linked List###

To print the list, start at the head pointer. Traverse the list through each node's "next" pointer, displaying its data member, until the node is no longer null.<br />

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
