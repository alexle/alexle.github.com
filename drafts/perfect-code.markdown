Does code need to be perfect?



In the past months I have asked myself a lot why we always strive to write perfect code. Picking up coding again for an internal project made me realise our team (and probably a large part of the rest of the software development world) spend a lot of time on writing perfectly formatted, ordered, patterned and tested code. But is this really necessary?
As a software development agency we are constantly trying to balance budgets, time and features with our clients. As a result features are changed or may not even get built because it would take too long and become too expensive. On the other hand, engineers have the feeling they need to rush things and can’t achieve the perfection they dream of. I guess this is recognisable for most agencies.

In these cases I think there is a truth in both points of view. The engineers want to write perfect code using the latest techniques, make sure that the code is well documented so they can fully understand how everything works and that it has tests so they can easily update things later. Product owners on the other hand just want things to be done, fast and cheap, so they can ship new features or convince new clients.
How can you make these conflicting views work together?

Ignore the future, code for now
Most product companies go through a few phases. Each of these phases require a different view on what “perfect” means. We could discuss long and hard about which phases exist, but for the sake of this article, I will just make the distinction between proof-of-concept code, MVP code and long-term code. Some examples of each to clarify.
When fleshing out a new idea for a product, it doesn’t make sense to spend any time on writing code that is open for extension, fully tested and conforming to the latest coding standards. The goal is to make a proof of concept, for example by connecting a few APIs or trying out a new interface idea. It is very unlikely anyone will have to dive into this code again when the goal is achieved.
When building a minimal viable product most people overestimate the need for good code. Every startup’s most important thing is to be out there with a nice looking, functional product. How it works under the hood doesn’t really matter. Until your MVP really gets traction you can run on shitty code or even do things manually to prove you have a product/market fit. Only once you nail it and the customers start flowing in, you should start caring about code, but up until then, you’re almost writing one-off code too.

As soon as those hard earned customers start flowing in, you are most likely generating some revenue or have attracted outside money. Now is the right time to start thinking about clean, long-term code. This is the situation our client from the example in the introduction was in. Since your audience is most likely to grow a lot, you need to start considering performance, stability and availability a lot more. Your engineering team is also going to scale up. This will force you to implement coding standards, documentation standards and a bunch of other procedures and practices. You start to need perfect code.
You can see in each of these examples a difference in the goal of the code and a difference in what “perfect” means in those situations.

In reality there is no such thing as the perfect way to do something. It might sounds strange, but programming is not an exact science. There are multiple ways to do things, which might all be valid.

Dealing with non-perfect code
There is however a very big difference between not perfect and bad. Think about the Pareto principle and Sufficient Design.
Every programmer that is forced to work on a project with legacy code, an MVP or even an existing long-term product, will want to rewrite it. It puts them back in control and gives a feeling of security, working on something they understand instead of dealing with what they will most likely consider a big spaghetti with meatballs. Big rewrites from the ground up are however always a bad idea. You will lose a lot of business logic and knowledge while doing so. This is not necessary, things can be left untouched, and considered not perfect, but not bad either, if they match the following criteria (taken from this article):

oes the code do what it is supposed to do?
Is it correct, usable and efficient?
Can it handle errors and bad data without crashing — or at least fail safely?
Is it easy to debug? Is it easy and safe to change?

When starting from scratch, extra care is needed. Of course any new project (or refactor of an existing part of a product) should be written properly: clean and readable code that follows some coding standard. The danger here is premature optimisation. Think about the current goal, not things like caching or overly complex database structures, avoid expensive technology or caring too much about performance. The less complex the code, the easier it is for new developers to get started. This is important in early stage startups, but also when working for clients; someone might need to take over the code one day.

As programmers we should try to be less perfectionistic and keep that goal in mind. Delivering value is more important than the cleanliness of our code. Only when you go for the long-term it makes sense to go for perfection.




Much of our programmer culture is built on the ideal of perfect code: code which not only works, but is also clean and elegant. We take pride in constructing clever solutions to difficult problems. This perfectionism, however, can be detrimental to the success of the team because perfectionism often leads to personal disagreements.


As I’ve matured as a programmer, I’ve found that an effective technique in avoiding team conflict is to stop aiming for perfect code. What follows are some examples of how to apply that concept to your own work.

Don’t get hung up on dogma

The only thing to demand of a codebase is that it works. A simple way to verify that is if it’s fully test-covered and that those tests are passing. Beyond that, every measurement of quality is subjective.

When you read other people’s code, try not to think how you would prefer it to look. Try not to rewrite it in your head. Let it exist just the way it is.
