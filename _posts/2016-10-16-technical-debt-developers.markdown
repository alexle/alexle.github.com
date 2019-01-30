---
layout: post
title: "How Technical Debt Affects Your Developers"
date: 2016-10-16
tags: programming
---

![stack of coins](/assets/coin_stack.jpg)

Everyone knows what debt is. It's something you owe in exchange for acquiring something now. Get a house today and owe the bank a bunch of money for 30 years.

The price for this service is your debt incurs interest - a percentage charged to your debt. The longer you hold it, the more interest you pay.

[Technical Debt][1], a concept invented by Ward Cunningham, is a similar concept in programming. Ship your product now! Gain an advantage in the market today.

All it costs are some corners cut in your software. Or using a quick & dirty design. The caveat is this "debt" has to be paid eventually - and with **interest**.

In other words, use a global variable and save a day's work to make a code release. But left unchecked, it'll add **more effort and complexity** to your future development, since you didn't choose the best design.

## Is Technical Debt Bad Then? ##

Many years ago, I would have answered with an emphatic **yes**. Technical debt is evil! We must purge it all from our codebase. We can't take on ANY new debt.

Nowadays, my views have somewhat changed. Yes, it isn't good to carry technical debt. At the same time, I've learned that businesses aren't successful because they had perfect code.

They were successful because they got a product to market **fast** and **at the right time**. It doesn't matter how beautiful your state machine is or how efficient your algorithms are if your product ships late and no one buys it.

Technical debt can be a powerful tool, if managed correctly. This post explores debt from a different angle - the negative effects it has on developers. Here are 5 side-effects debt has on developers.

## 1. Tough Work Environment ##

Without routine cleanup (i.e. refactoring), software will atrophy. It's just a natural effect when changes are added. Keeping up with this maintenance is hard enough.

However, when shortcuts are constantly taken and proper designs are skipped, the quality of code degrades even quicker. Something that would have been a 2 point story a couple months ago is now an 8 point story.

This leads to schedules slipping and deadlines missed. Which leads to painful discussions and finger-pointing between developers, managers, and the business group. It's not a fun environment to be in when everyone has different views on reality.

## 2. Debt Decreases Productivity ##

Most people despise inefficiencies. Me especially. Our time on this planet is fleeting. Why put up with crap if you [don't have to][2]?

A codebase high in technical debt means that feature delivery slows to a crawl. It's frustrating when a simple task ends up being 10x more difficult than it has to be, due to working around existing hacks and hooks.

The longer debt lives in code, the more expensive it is to make changes or add features. In this context,  the cost is a developer's time.

No one likes to be unproductive day after day. It's defeating and stressful. The worst part is how vicious this cycle is:

* More debt -> Lower productivity
* Lower productivity -> Less features delivered
* Less features delivered -> Fall behind schedule
* Fall behind schedule -> Take on more debt..

## 3. Debt Lowers Morale ##

We've all faced our share of bad code. Usually, it's "this is awful, but I can work around this". But when technical debt is rampant in the code, it can easily become "what the **@#!$** is this mess".

This is demoralizing to developers, who are the ones who have to carry this burden. Instead of approaching projects with excitement, developers can easily become disengaged and unmotivated when buried in constant technical debt.

The relationship among teams can also be affected by technical debt. Resentment and animosity can arise if one group is always stuck with legacy code, while another gets the fresh, blemish-free projects.

## 4. Debt Makes Change Difficult ##

It's clear software has taken on too much debt when developers are afraid or unwilling to make changes. Maybe the code has too many dependencies, lacks documentation, or has inadequate unit-testing.

Everything just becomes *difficult*.

People become hesitant to touch module XYZ, because they know it'll cause a cascade of subsequent changes in other areas of the code. Fixes can even introduce more bugs.

The clincher is when adding new features or upgrading to next-gen hardware become **risky**. This leads to developers touching things as little as possible, saying to themselves that "the next person will make this right". Clearly, this is not a good culture to cultivate.

## 5. Skills Stop Improving ##

Technical debt slows down progress and innovation in your software. This also applies directly to your developers. More time spent on working through debt means less time improving skills or learning new technology.

It's demotivating when your peers are talking about applying new coding languages, design practices, and frameworks to their exciting projects, while you know what waits for you at work tomorrow will be the same problems in a crippling codebase.

This can lead to disgruntled and unhappy developers. Eventually, the ones who want to make improvements, contribute their ideas, and add impactful solutions will leave. And these are the ones the business can least afford to lose.

## Technical Debt Is Not Just About Code ##

Technical debt is a [positive and necessary step][3] in software engineering. You can capture time-bound market opportunities. Meet aggressive deadlines. Quickly gather early feedback from customers.

The key is paying it down periodically.

It's difficult to quantify the cost of technical debt. Especially to the business, who may not see tangible results from resources used. But every successful software company needs to have a strategy on how they prioritize and reconcile their debt.

Many people view technical debt as a business or code problem, without realizing the toll it has on its developers. Mismanaging this leverage not only hampers a company's agility and software quality, but also its employees.

[1]: https://en.wikipedia.org/wiki/Technical_debt
[2]: /dont-put-up-with-crap.html
[3]: http://www.bigeng.io/why-the-way-we-look-at-technical-debt-is-wrong/
