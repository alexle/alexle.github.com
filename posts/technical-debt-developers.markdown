---
title: How Technical Debt Affects Your Developers
date: 10-16-2016
image: /static/coin-stack.jpg
meta: Technical debt is a necessary step in software engineering. However, it can take its toll on your developer's productivity, morale, and skills.
---

<p>
<img class="pure-img center" src="/static/coin-stack.jpg" alt="stack of coins" />
</p>

Everyone knows what debt is. It's something you owe in exchange for acquiring something now. Get a house today and owe the bank a bunch of money for 30 years.

The price for this service is your debt incurs "interest" - a percentage charged to your debt. The longer you hold this debt, the larger the interest payments grow.

[Technical Debt][1], a concept invented by Ward Cunningham, is a similar concept in programming. Get your product to market faster, ship your software today, in return for cutting corners or using a quick & dirty design. This "debt" is cost that has to be paid eventually, and with **interest**.

For example, a global variable is used to save a day's work in order to make a code release deadline. But it'll cost more than a day's work to fix it later. The longer debt stays in your code, the more expensive it'll be make changes.

##Is Technical Debt Bad Then?##

9 years ago, I would have answered with an emphatic **yes**. Technical debt is evil! We need to purge all of it from our codebase and we can't take on ANY new debt.

Nowadays, my views have somewhat changed. Yes, it isn't good to carry technical debt. At the same time, I've learned that businesses aren't successful because they had perfect code.

They were successful because they got a product to market **fast** and **at the right time**. It doesn't matter how beautiful your state machine is or how efficient your algorithms are if your product ships late and no one buys it.

There are many arguments for and against technical debt. This post explores a different angle on the topic - the negative effects it has on developers. Yes, we have feelings too!

##Tough Work Environment##

I'm a firm believer that without routine cleanup (i.e. refactoring), software will atrophy. It's just a natural effect when changes are added. Keeping up with this maintenance is hard enough.

However, when shortcuts are constantly taken and proper designs are skipped, the quality of code degrades even faster. Something that would have been a 2 point story a couple months ago is now an 8 point story.

This leads to schedules slipping and deadlines missed. Which leads to painful discussions and finger-pointing between developers, managers, and the business group. It's not a fun environment to be in when everyone has different views on reality.

##Decreases Productivity##

Most people I know despise inefficiencies. Me especially. Our time on this planet is fleeting, why put up with crap if you [don't have to][2]?

A codebase high in technical debt means that feature delivery slows to a **crawl**. It's frustrating when a simple task ends up being 10x more difficult than it has to be, due to working around existing hacks and hooks.

No one likes to be unproductive day after day. It's defeating and stressful. The worst part is how vicious this cycle is:

* More debt -> Lower productivity
* Lower productivity -> Less features delivered
* Less features delivered -> Fall behind schedule
* Fall behind schedule -> Take on more debt..

##Lowers Morale##

We've all faced our share of bad code. Usually, it's "this is awful, but I can work around this". But when technical debt is rampant in the code, it can easily become "what the **@#!$** is this mess".

This is demoralizing to developers, who are usually the ones who have to carry this extra burden. It's like being asked to run a race, but your lane is filled with sand. Then you have to explain afterwards why you weren't able to run as fast as before.

The relationship among teams can also be affected by technical debt. Resentment and animosity can arise if one group is always stuck with legacy code, while another gets the fresh, blemish-free projects.

##Making Changes Become Difficult##

From my experience, it's clear software has taken on too much debt when developers are afraid or unwilling to make changes. Everything becomes *difficult*, because the code has too many dependencies, lacks documentation, or is missing adequate unit-testing. All because of technical debt.

No one wants to touch XYZ module, because they know it'll cause a cascade of subsequent changes in other areas of the code. Every fix introduces more bugs. Faced with deadlines, developers may even resort to the "check-in code, throw it over the wall, and hope nothing breaks" approach.

What's worse is when adding new features or upgrading to next-gen hardware becomes *risky*. This leads to developers touching things as little as possible, saying to themselves that "the next person will make this right". Clearly, this is not a good culture to cultivate.

##Skills Stop Improving##

Technical debt slows down progress and innovation in your software. This also applies directly to your developers. More time spent on working through debt means less time improving skills or learning new practices.

It's demotivating when your peers are talking about applying new coding languages, design practices, and frameworks to their exciting projects, while you know what waits for you at work tomorrow will be the same problems in a crippling codebase.

This can lead to disgruntled and unhappy developers. Eventually, the ones who want to make improvements, contribute their ideas, and add impactful solutions will leave. And these are the ones the business can least afford to lose.

##Technical Debt Is Not Just About Code##

Technical debt is a [positive and necessary step][3] in software engineering. You can capture time-bound market opportunities, meet aggressive deadlines, or quickly gather early feedback from customers. The key is paying it down periodically.

It's difficult to quantify the cost of technical debt. Especially to the business, who may not see tangible results from resources used. But every successful software company needs to have a strategy on how they prioritize and reconcile their debt.

Many people view technical debt as a business or code problem, without realizing the toll it has on its developers. Mismanaging this leverage is not only costly to a company's agility and software quality, but also to its employees.

[1]: https://en.wikipedia.org/wiki/Technical_debt
[2]: /blog/dont-put-up-with-crap.html
[3]: http://www.bigeng.io/why-the-way-we-look-at-technical-debt-is-wrong/
