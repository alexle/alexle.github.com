---
title: Want To Become More Agile? Reduce Your Cycle Time
date: 12-01-2016
---

 continuous delivery is really about one thing: reducing release cycle time. By cycle time, I mean the time involved in having an idea, getting that idea into the hands of our users, and gathering feedback. We should optimize our software development processes for that. Whatever it takes.

Defining cycle time more clearly

Imagine the simplest change to your production system that you can think of. You want it to be so simple that you can ignore the variable cost of development.

Now imagine that change going through all of the normal processes to get it prioritized, scheduled, defined, implemented, tested, verified, documented, and deployed into production—every step that a change to production would normally take. The time that it takes to complete all of those steps, plus the time that the change spends waiting between steps, is your cycle time. This is a great proxy term I use for measuring the time from "idea" to "valuable software in the hands of users."

We had a cycle time of 57 minutes. In 57 minutes we could evaluate any change to our production system and, if all the tests passed, be in a position to release that change into the hands of users.

Now think about the consequences of being able to do that.

If you have a cycle time of 57 minutes, you can't afford the communications overhead of large teams. You need compact, cross-functional, efficient teams.
 
You can't afford the hand-offs that are implicit in siloed teams. If you divide your development effort up into technical specialisms, you will be too slow. You need cross-functional collaborative teams to ensure a continual flow of changes.
 
You can't rely on manual regression testing. You need a great story on automated testing. Human beings are too slow, too inefficient, too error prone, and too expensive.
 
You can't rely on manual configuration and management of your test and production environments. You need to automate the configuration management, automate deployment, and develop a good story on "infrastructure as code."
 
You can't have a cycle time of 57 minutes and have hand-offs between Dev and Ops.
 
You can't have a cycle time of 57 minutes if your business can't maintain a constant smooth flow of ideas.
 
You have to be very good at a lot of aspects of software development to achieve this kind of cycle time.




Minimizing cycle time

Cycle time is a key metric for kanban teams. Cycle time is the amount of time it takes for a unit of work to travel through the team’s workflow–from the moment work starts to the moment it ships. By optimizing cycle time, the team confidently forecast the delivery of future work.

Overlapping skill sets lead to smaller cycle times. When only one person holds a skill set, that person becomes a bottleneck in the workflow. So teams employ basic best practices like code review and mentoring help to spread knowledge. Shared skills mean that team members can take on heterogeneous work, which further optimizes cycle time. It also means that if there is a backup of work, the entire team can swarm on it to get the process flowing smoothly again. For instance, testing isn't only done by QA engineers. Developers pitch in too!


If you can confidently evaluate your changes to the point where you are happy to release changes into production in under an hour, without any further work, you are doing very well!

Making metrics visual

One of kanban's core values is continuous improvement. But how do teams ensure they're continuing to improve? One word: visuals. When the team can see data, it's easier to spot bottlenecks in the process (and remove them!). Two common reports kanban teams use are control charts and cumulative flow diagrams.

A control chart shows the cycle time for each issue as well as a rolling average for the team.w

A cumulative flow diagram shows the number of issues in each state. The team can easily spot blockages by seeing the number of issues increase in any given state. We can see in the chart below the amount of code waiting to be merged (red) significantly increases over time. This creates a bottleneck that denies the customer of features and fixes that have already built, and increases the likelihood of massive integration conflicts when the work does get merged upstream. 


In the example above, the team realizes the backup just before 1 September and quickly swarms to bring the amount of un-merged code back down to an acceptable level. 

Moving toward continuous delivery

We know that continuous integration–the practice of building and validating code incrementally throughout the day–is essential for maintaining quality. Now let's meet CI's older, more sophisticated cousin: continuous delivery (CD). This is the practice of releasing work to customers frequently–even daily or hourly. Kanban and CD beautifully complement each other because both techniques focus on the just-in-time (and one-at-a-time) delivery of value.

The faster a team can deliver innovation to market, the more competitive their product will be in the marketplace. And kanban teams focus on exactly that: optimizing the flow of work out to customers. 


Optimizing for short cycle time drives good behaviors

You don't have to be great at every step in the release cycle before you start seeing the benefits of this mindset. Simply striving to improve your cycle time will help you (and, in some sense, force you) to improve your development process, culture, and technology. It will force you to address impediments and inefficiencies that get in your way. And the best part is that I've never seen this metric encourage bad behaviors.

Many people are nervous that reducing cycle time will reduce quality. In my experience, and in countless experiences I've heard about throughout the industry, I've found that the reverse is true.

What happens is that by reducing cycle time you reduce batch-size. By reducing batch-size, you reduce the risk of each change (ever heard of colleagues warning against "big bang" releases?). Each change becomes simpler and lower-risk. 66% of organizations that claim to practice continuous delivery say that quality goes up, not down (according to the 2015 CA Technologies DevOps Survey). Personally, I'm not sure what the other 34% are doing wrong ;-)

Smaller releases are low-risk and lessen the cognitive load

If you have a short cycle time, you can, and will, release changes in small batches. Think about each change. Each change will be small, simple, and easy to understand.

If you release only once every few months, then you will be storing up lots of changes. If you imagine that each change has a small amount of risk associated with it, then the total risk for any release is going to be the sum of all of those risks.

Except it's worse than that. In addition, there is going to be a compounding effect. What if my change interacts with your change? There is an additional risk associated with the interaction between changes. These risks will grow exponentially as more changes are combined. The more changes that are released together, the higher the risk that two or more changes will interact in unexpected ways.

So the total risk is going to be something like the sum of all the risks associated with each change plus the risk that two or more changes will interact badly. If you release one change at a time, though, as I've previously suggested, you eliminate this secondary compounding of risk.

How to reduce cycle time: My experience in a complex software system

A few years ago, I worked with a team building some complex software in C++. This development team was very good. They had adopted an automated testing approach some years before. They were well ahead of industry norms, because they operated a process based on nightly builds.

Each night their automated systems would build and run their automated tests to evaluate their software. The build and tests took about nine hours to complete. Each morning the team would look at the results and there would be a significant number of test failures. I spoke to one of the developers who had been working this way for the previous three years. He told me that during those three years of doing nightly builds, there had been only four occasions when all of the tests had passed.

To get some work past this common blocker, they decided to release the individual modules that passed all of their tests. This was a reasonable strategy as long as none of the components interacted with any other. Mostly they didn't, but the few components that did interact caused numerous problems because the various combinations of modules that happened to get released interacted in unpredictable ways. Most of the issues arose from incompatibilities with old components.

I argued that cycle time was important, a driver for good behavior and outcomes. We worked hard on the build. We invested a lot of time, money, and effort on experimenting with different approaches. Features we added to the process included:

Parallelized builds
Improved incrementalism
Better servers
Tests triaged into groups
Builds divided into a deployment pipeline
A 12-minute commit stage (running the vast majority of the tests) to replace the 9-hour nightly build 
A slower (one-hour) acceptance test stage
The "acceptance test" designation was fairly arbitrary in this case. If a test was too slow, we moved it to the "acceptance test stage."

The results were quite dramatic. In the first two-week period following the introduction of this new build, we saw three builds in which all of the tests passed—compared to four in the previous three years. In the next two-week period, there were multiple successful builds every day (all tests passing).

Instead of cherry-picking modules with passing tests, we could now release all of the software together, or not at all. Each morning we could simply deploy the newest release candidate that had passed all the tests. We could have more confidence that these components would work together, and we could begin improving our test scenarios that crossed the boundaries between components.

Reducing cycle time to improve everything

Reducing cycle time drives good behaviors. It encourages us to establish concrete, efficient feedback loops that allow us to learn and adapt. The team in my war story above was not different before or after the change in process. The change in approach and the focus on cycle time gave them insight into what was going wrong and an opportunity to quickly and efficiently experiment with solutions to any problems that arose.

Cycle time drives us in the direction of lower-risk release strategies. It will move your team in the direction of higher-quality development practices. I encourage you to optimize your development process to reduce cycle time. If you do, I believe that you will see it improve almost everything that you do.




Small batch size is really important for fast feedback cycles and reducing release risk

The smaller the release, the fewer the dependencies. The fewer the dependencies, the fewer things there are to go wrong. If you want to reduce the risk of a release, reduce the size, don’t double-down on control processes that actually increase release size by creating a process so onerous that people will do anything to avoid it, like releasing less frequently. Smaller releases makes coordination easier. They make user adoption easier because there are fewer changes or new features to learn. Smaller more targeted releases make it easier to evaluate their impact because their are fewer things to measure. This makes feedback faster, which reduces waste and helps teams to better scope future releases. Smaller, more frequent releases are good.

They are good, but only if a team is continuous building and testing their software. They are good only if release processes are simple, streamlined, and predictable. They are good only if applications are loosely coupled and don’t create a cascading series of problems when something fails.



To correct the problem, Microsoft universally adopted something called a "zero defects methodology". Many of the programmers in the company giggled, since it sounded like management thought they could reduce the bug count by executive fiat. Actually, "zero defects" meant that at any given time, the highest priority is to eliminate bugs before writing any new code. Here's why.

In general, the longer you wait before fixing a bug, the costlier (in time and money) it is to fix.

For example, when you make a typo or syntax error that the compiler catches, fixing it is basically trivial.

When you have a bug in your code that you see the first time you try to run it, you will be able to fix it in no time at all, because all the code is still fresh in your mind.

If you find a bug in some code that you wrote a few days ago, it will take you a while to hunt it down, but when you reread the code you wrote, you'll remember everything and you'll be able to fix the bug in a reasonable amount of time.

But if you find a bug in code that you wrote a few months ago, you'll probably have forgotten a lot of things about that code, and it's much harder to fix. By that time you may be fixing somebody else's code, and they may be in Aruba on vacation, in which case, fixing the bug is like science: you have to be slow, methodical, and meticulous, and you can't be sure how long it will take to discover the cure.

And if you find a bug in code that has already shipped, you're going to incur incredible expense getting it fixed.

That's one reason to fix bugs right away: because it takes less time. 


There's another reason, which relates to the fact that it's easier to predict how long it will take to write new code than to fix an existing bug. For example, if I asked you to predict how long it would take to write the code to sort a list, you could give me a pretty good estimate. But if I asked you how to predict how long it would take to fix that bug where your code doesn't work if Internet Explorer 5.5 is installed, you can't even guess, because you don't know (by definition) what's causing the bug. It could take 3 days to track it down, or it could take 2 minutes.

What this means is that if you have a schedule with a lot of bugs remaining to be fixed, the schedule is unreliable. But if you've fixed all the known bugs, and all that's left is new code, then your schedule will be stunningly more accurate.

Another great thing about keeping the bug count at zero is that you can respond much faster to competition. Some programmers think of this as keeping the product ready to ship at all times. Then if your competitor introduces a killer new feature that is stealing your customers, you can implement just that feature and ship on the spot, without having to fix a large number of accumulated bugs.


 My answer is that when you’re starting out you should begin with one-week sprints, after which you might want to experiment with two weeks. The most common response I hear to that suggestion is that one-week sprints are simply impossible in that particular team/language/problem domain/whatever.

One-week sprints aren’t impossible, but they may be challenging, and that’s part of the point. Long sprints are too easy to treat as mini-waterfalls, and for many teams that means that the sprint is pretty much like their previous process — big pieces of work that flow through analysis, design, implementation, testing and delivery. Nothing much changes from whatever process they used before. 
You can’t get away with that in a one-week sprint, at least not if you want to be able to even pretend that you’ve delivered some increment of working software. A one-week sprint forces radical changes to your process; they may not be easy changes, but they will be rewarding.

You actively need to break your stories into smaller pieces. You’ll probably need to better understand what the larger story is trying to achieve, learn more about the problem domain, and also be creative in the way you split it up. You may discover that some of the small pieces aren’t really that valuable and can be done much later, or possibly not at all.

You usually don’t have time for handovers because they’re time-consuming and they make scheduling and coordination too hard. You’ll find you benefit more from generalists, or from specialists working in tandem (pairing).

If you have separate testing environments, you won’t be able to tolerate time-consuming release processes.

You probably won’t have time for a separate user acceptance phase — you’ll need to involve the user more incrementally so that user acceptance is a formality.

When I’ve helped teams transition to agile in the past, I’ve started them with one-week sprints and told them to expect the first few to fail, in the sense that we won’t deliver anything. What we will do is quickly identify areas of the process that need improvement and act on them. By the end of the third sprint (the equivalent of one three-week sprint) we will have made a number of process changes, and we’ll probably have delivered something as well.

Even if we just stick to the “normal” Scrum ceremonies, we’ll have had three retrospectives in three weeks (we may have had more). We’ll also have had three planning meetings and three showcases (and of course fifteen daily scrums).


There are three primary ways to fix Failures of Strategy.

Launch it quickly.
Do it cheaply.
Revise it rapidly.
Launch it quickly. Some ideas work much better than others, but nobody really knows which ideas work until you try them. Nobody knows ahead of time — not venture capitalists, not the intelligent folks at Amazon, not your friends or family members. All of the planning and research and design is just pretext. I love Paul Graham's take on this: "You haven't really started working on [your idea] till you've launched."

Because of this, it is critical to launch strategies quickly. The faster you test a strategy in the real world, the faster you get feedback on whether or not it works. 





