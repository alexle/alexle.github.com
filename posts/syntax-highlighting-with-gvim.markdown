---
title: Add Syntax Highlighting To Your Blog With VIM
date: 03-17-2012
image:
meta: A tutorial on how to add syntax highlighting to your blog using GVIM and teh TOHtml method.
---

One of the challenges [Chisel][1] presents is the lack of syntax highlighting for code snippets. Luckily, this can be solved with -- surprise, surprise -- VIM!


VIM includes a plugin called **TOhtml**. Calling this will convert the current file into HTML, complete with coloring if syntax highlighting is enabled. This works on hightlighted text too. To execute, enter normal mode and type:

`:TOhtml`

The HTML output is created in a split VIM window. Here is a sample python script pasted into this post:

import sys<br>
<br>
if len(sys.argv) != 2:<br>
   hex_num = str('0');<br>
else:<br>
   hex_num = str(sys.argv[1])<br>
<br>
bin_num = bin(int(hex_num, 16))[2:]<br>
<br>
print bin_num<br>
<br>
counter = 0<br>
for i in bin_num[::-1]:<br>
   if i == str(1):<br>
      print "Bit " + str(counter)<br>
<br>
   counter += 1<br>

Here is the same code after ran through TOhtml with syntax highlighting:

<style type="text/css">
pre { font-family: monospace; color: #ffffff; background-color: #333333; }
.Special { color: #ffdead; }
.Identifier { color: #98fb98; }
.Constant { color: #ffa0a0; }
.Type { color: #bdb76b; font-weight: bold; }
.Comment { color: #87ceeb; }
</style>

<font color="#cd5c5c">import</font>&nbsp;sys<br>
<br>
<font color="#f0e68c"><b>if</b></font>&nbsp;<font color="#98fb98">len</font>(sys.argv) !=&nbsp;<font color="#ffa0a0">2</font>:<br>
&nbsp;&nbsp; hex_num =&nbsp;<font color="#98fb98">str</font>(<font color="#ffa0a0">'0'</font>);<br>
<font color="#f0e68c"><b>else</b></font>:<br>
&nbsp;&nbsp; hex_num =&nbsp;<font color="#98fb98">str</font>(sys.argv[<font color="#ffa0a0">1</font>])<br>
<br>
bin_num =&nbsp;<font color="#98fb98">bin</font>(<font color="#98fb98">int</font>(hex_num,&nbsp;<font color="#ffa0a0">16</font>))[<font color="#ffa0a0">2</font>:]<br>
<br>
<font color="#98fb98">print</font>&nbsp;bin_num<br>
<br>
counter =&nbsp;<font color="#ffa0a0">0</font><br>
<font color="#f0e68c"><b>for</b></font>&nbsp;i&nbsp;<font color="#f0e68c"><b>in</b></font>&nbsp;bin_num[::-<font color="#ffa0a0">1</font>]:<br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;i ==&nbsp;<font color="#98fb98">str</font>(<font color="#ffa0a0">1</font>):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#98fb98">print</font>&nbsp;<font color="#ffa0a0">&quot;Bit &quot;</font>&nbsp;+&nbsp;<font color="#98fb98">str</font>(counter)<br>
<br>
&nbsp;&nbsp; counter +=&nbsp;<font color="#ffa0a0">1</font><br>

Note TOhtml creates a HTML file with **all** tags, which may be overkill for sharing code snippets. My usage simply involves copying the meat between the &lt;body&gt; tags and adding the code in my posts.

The HTML may not be optimal, but it works and provides a quick solution to adding colorized code snippets on your blog.

\* Update: Follow the discussion at [Hacker News][2]

[1]: https://github.com/dz/chisel
[2]: http://news.ycombinator.com/item?id=3716465
