The Birthday Paradox
06-09-2011    

I read something the other day that piqued my curiosity:

> In a random gathering of 23 people, there is a 50% chance that two people will have the same birthday.

No way! I've been to many gatherings and I don't remember anyone having the same birthday. Then again, I never really checked..

Thus, began my journey to verify this madness. I messed around with permutations and combinations for half an hour, only to leave more confused than when I started. A new approach was needed.

I decided to look at the problem from a different angle. I could calculate (more easily) the probability of no collisions, then subtract that from 1 to get the number of collisions!

Say there are 10 marbles in front of you and each person has to pick a different marble. The first person has 10 marbles to choose from. The second person only has 9 to choose from. So the probability of 2 people choosing different marbles is:

> 10/10 x 9/10 = 0.9 or 90%

The probability of 3 people choosing different marbles, or having no collisions, is:

> 10/10 x 9/10 x 8/10 = 0.72 or 72%

This same logic can be applied to having the same birthday. The probability that two people do not have the same birthday is:

> 365/365 x 364/365 = 0.99726 or 99.73%

Subtract that from 1 and you get the probability that two people have the same birthday:

> 1 - 0.99728 =  0.00273 or 0.27%

To make this exercise simpler, I wrote a quick python script for the calculations:

<div id="code">
<font color="#cd5c5c">from</font>&nbsp;__future__ <font color="#cd5c5c">import</font>&nbsp;division<br>
<font color="#cd5c5c">import</font>&nbsp;sys, math<br>
<br>
<font color="#f0e68c"><b>def</b></font>&nbsp;<font color="#98fb98">CalcProbMatch</font>( n, days ):<br>
&nbsp;&nbsp; prob_no_match = 1<br>
<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>for</b></font>&nbsp;i <font color="#f0e68c"><b>in</b></font>&nbsp;range( n + 1 ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prob_no_match *= (days - i) / days<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prob_match = 1 - prob_no_match<br>
<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>print</b></font>&nbsp;<span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">%02d people - %05.2f percent</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;% ( i, prob_match * 100 )<br>
<br>
<font color="#f0e68c"><b>for</b></font>&nbsp;i <font color="#f0e68c"><b>in</b></font>&nbsp;range( 27 ):<br>
&nbsp;&nbsp; CalcProbMatch( i, 365 )<br>
</div>

The output was surprising:

> 01 people - 00.00 percent<br>
02 people - 00.27 percent<br>
03 people - 00.82 percent<br>
04 people - 01.64 percent<br>
05 people - 02.71 percent<br>
06 people - 04.05 percent<br>
07 people - 05.62 percent<br>
08 people - 07.43 percent<br>
09 people - 09.46 percent<br>
10 people - 11.69 percent<br>
11 people - 14.11 percent<br>
12 people - 16.70 percent<br>
13 people - 19.44 percent<br>
14 people - 22.31 percent<br>
15 people - 25.29 percent<br>
16 people - 28.36 percent<br>
17 people - 31.50 percent<br>
18 people - 34.69 percent<br>
19 people - 37.91 percent<br>
20 people - 41.14 percent<br>
21 people - 44.37 percent<br>
22 people - 47.57 percent<br>
<b>23 people - 50.73 percent <-</b><br>
24 people - 53.83 percent<br>
25 people - 56.87 percent<br>
26 people - 59.82 percent<br>
27 people - 62.69 percent<br>

23 people in a room, 50.73% chance for a same birthday. It's really true.

In hindsight, it's similar to the penny/wheat and chessboard problem in that we don't see how quickly the compounds or "combinations" can grow. When I first saw this problem, I pictured the probability that 23 other people would have the same birthday as me (pretty low actually). What I failed to consider, however, was that the statement also includes comparing other people's birthdays with each other.

Anyways, it was a fun experiment and I learned something new.

Bonus: How many people would have to be in a room to guarantee a same birthday?

> 80 people - 99.99 percent<br>
81 people - 99.99 percent<br>
82 people - 99.99 percent<br>
<b>83 people - 100.00 percent <-</b><br>
84 people - 100.00 percent<br>
