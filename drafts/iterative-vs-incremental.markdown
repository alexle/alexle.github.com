Iterative vs. Incremental Development
01-20-2014

’ve found that people often conflate the terms “iterative” and “incremental” when it comes to software and/or product development—they often use “iterative” when they really mean “incremental”. I’ve been guilty of this in the past, but feel like I have a good handle on the differences now.
Iterative
Iterative development involves a cyclical process. While one may still have a general product road map, learning from one iteration informs the next iteration. This learning can come from end-users, testers, or the developers themselves. An iterative process embraces the fact that it is very difficult to know upfront exactly what the final product should look like (no matter how smart or well-informed you might be) and builds in as many learning opportunities as possible.
Incremental
Incremental development involves breaking a large chunk of work into smaller portions. This is typically preferable to a monolithic approach where all development work happens in one huge chunk. Unlike those using an iterative approach, those taking an incremental approach will stick as closely as possible to the original road map. Few, if any, opportunities for feedback exist until the final product launch.
Conclusion
No one uses a purely iterative or incremental process. Those using an incremental process are unlikely to completely ignore any feedback or learning that happens to seep into the process. Those using an iterative process are unlikely to completely let go of their original vision and preconceived notions and rely purely on outside learning.
Both processes have their places. If the problem and solution are well known, then an incremental process can work well. However, many software and product development initiatives are a search for an unknown solution to a known problem. If the solution is unknown, then an iterative process is critical. If both the problem and the solution are unknown, then an iterative process alone isn’t enough—but that’s a topic for another day.


http://itsadeliverything.com/revisiting-the-iterative-incremental-mona-lisa

What is iterative and what is incremental development? Even the experts are confusing themselves when describing it. Perhaps our language is an inadequate reflection of reality.

Jeff Patton thinks software should be built the way an artist works. The artist "iterates" on the whole thing and the potential of the whole picture is visible in every iteration from the initial sketch to the final painting. The complete work comes gradually into focus. Patton calls this "iterative" development.

However, this is exactly what Mills and Brooks call "incremental" development. They advocate growing software like a plant. This is a similar metaphor to the way an artist's sketch "grows."


IterativeDevelopment means:
I write loads of stuff that's a complete mess
I go through it throwing out the irrelevant drivel, expanding on the important bits, and sorting out the structure
I go through it again now I can start to see the shape of it, sorting it some more
I go through it yet again, etc, until it's GoodEnough
IncrementalDevelopment means:
I write part one
I write part two
I write part three, etc, until the book is finished
Now incremental development may work OK for novelists (e.g. Charles Dickens, or J.K. Rowling), but when you try doing it with computer systems you find that in writing part two, you need to revise and rework some of part one (e.g. to allow reuse), and in writing part three you need to reworks parts one and two, etc..., especially if you subscribe to OnceAndOnlyOnce and MercilessRefactoring.
So in practice, at least in XP practice, your development is both incremental and iterative


[1]: http://www.agileproductdesign.com/jeff_patton.html
