---
layout: post
title: "The Birthday Paradox"
date: 2011-06-09
tags: programming
---

I read something the other day that piqued my curiosity:

> In a random gathering of 23 people, there is a 50% chance that two people will have the same birthday.

No way! I've been to many gatherings and I don't remember anyone having the same birthday. Then again, I never really checked..

Thus, began my journey to verify this madness. I messed around with permutations and combinations for half an hour, only to leave more confused than when I started. A new approach was needed.

I decided to look at the problem from a different angle. I could calculate (more easily) the probability of no collisions, then subtract that from 1 to get the number of collisions!

Say there are 10 marbles in front of you and each person has to pick a different marble. The first person has 10 marbles to choose from. The second person only has 9 to choose from. So the probability of 2 people choosing different marbles is:

> 10/10 x 9/10 = 0.9 or 90%

The probability of 3 people choosing different marbles, or having no collisions, is:

> 10/10 x 9/10 x 8/10 = 0.72 or 72%

This same logic can be applied to having the same birthday. The probability that two people do **not** have the same birthday is:

> 365/365 x 364/365 = 0.99726 or 99.73%

Subtract that from 1 and you get the probability that two people **have** the same birthday:

> 1 - 0.99728 =  0.00273 or 0.27%

To make this exercise simpler, I wrote a quick python script for the calculations:

``` python
from __future__ import division
import sys, math

def CalcProbMatch( n, days ):
   prob_no_match = 1

   for i in range( n + 1 ):
      prob_no_match *= (days - i) / days

      prob_match = 1 - prob_no_match

   print '%02d people - %05.2f percent' % ( i, prob_match * 100 )

for i in range( 27 ):
   CalcProbMatch( i, 365 )
```

The output was surprising:

``` python
01 people - 00.00 percent  
02 people - 00.27 percent  
03 people - 00.82 percent  
04 people - 01.64 percent  
05 people - 02.71 percent  
06 people - 04.05 percent  
07 people - 05.62 percent  
08 people - 07.43 percent  
09 people - 09.46 percent  
10 people - 11.69 percent  
11 people - 14.11 percent  
12 people - 16.70 percent  
13 people - 19.44 percent  
14 people - 22.31 percent  
15 people - 25.29 percent  
16 people - 28.36 percent  
17 people - 31.50 percent  
18 people - 34.69 percent  
19 people - 37.91 percent  
20 people - 41.14 percent  
21 people - 44.37 percent  
22 people - 47.57 percent  
23 people - 50.73 percent
24 people - 53.83 percent  
25 people - 56.87 percent    
26 people - 59.82 percent  
27 people - 62.69 percent  
```

**23 people** in a room, **50.73%** chance for a same birthday. It's really true.

In hindsight, it's similar to the penny/wheat and chessboard problem in that we don't see how quickly the compounds or "combinations" can grow.

When I first saw this problem, I pictured the probability that 23 other people would have the same birthday as me (pretty low actually). What I failed to consider, however, was that the statement also includes comparing other people's birthdays with each other.

Anyways, it was a fun experiment and I learned something new.

Bonus: How many people would have to be in a room to *almost*<sub>1</sub> guarantee a same birthday?

> 80 people - 99.99 percent  
81 people - 99.99 percent  
82 people - 99.99 percent  
<b>83 people - 100.00 percent <-</b>  
84 people - 100.00 percent  

1: The precision is beyond the computer's capability at this point so 99.99999.. is rounded to 100. To truly guarantee a same birthday, there must be 366 people (or 367 on a leap year).
