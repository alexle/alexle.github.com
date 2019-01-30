---
layout: post
title: "A Russian Gangster Kidnaps You.."
date: 2013-07-26
---

He puts two bullets in consecutive order in an empty six-round revolver, spins it, points it at your head and shoots.

Click. You're still alive.

He then asks you, do you want me to spin it again and fire or pull the trigger again. What option do **YOU** choose?

I came across this question on Business Insider's "[20 Toughest Job Interview Questions][1]" this morning. While either choice is a lose-lose situation, it did give me pause on what my answer would be.

Naturally, it would depend on which option had the greatest chance of survival. Here is my take on the problem:

## "Spin It Again and Fire" ##

The probability of dying is simple to calculate here. There are 6 chambers in the revolver, with 2 chambers containing bullets. Thus, the probability of eating a bullet is 2 (number of given outcomes) divided by 6 (number of total outcomes) or **33%**.

Note that by spinning the chambers again, the previous "survival" shot has no bearing on the next shot. Also, the fact the bullets are in consecutive order does not affect the final odds, since it's just a ratio of expected occurrences to total possible occurrences.

## "Pull The Trigger Again" ##

In this situation, however, the previous shot AND the fact the bullets are in consecutive order do matter in the calculation. Bang! The first shot goes off.

![picture of two bullets in consecutive order in six-round revolver](/assets/two_bullets.jpg)
_Diagram of revolver chamber. The red circles are bullets._

If you are alive at this point, then it means the first shot did NOT contain a bullet and must have come from either locations 1, 2, 3, or 4. So the number of situations you could be in after the first shot is **4**.

Now we calculate the **given outcomes**, or number of ways we could die. Since the revolver moves in a deterministic fashion, death can <u>only</u> occur if the first shot was fired from chamber 4, leading to the second shot being fired from chamber 5 (bullet). If the first shot was fired from either chambers 1, 2, or 3, then the subsequent shot would be blanks from 2, 3, or 4!

To complete the calculation, the probability of dying here is 1 (number of given outcomes) divided by 4 (number of total outcomes) or **25%**.

Therefore, if given a choice, look the gangster in the eye and tell him - "Pull the trigger".

[1]: http://www.businessinsider.com/toughest-job-interview-questions-2013-7
