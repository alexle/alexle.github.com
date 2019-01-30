How estimating my tasks have made me a better developer
11-01-2013

Spend some time planning your projects, but not too much. When starting a project, I would first get a general idea of what components will be necessary for the system to work, but wouldn’t spend too much time defining the interfaces between them or breaking each one down into subcomponents before diving into code. Sometimes it may even be more efficient to write some component the “wrong” way the first time and rewrite it if necessary when the other components are more mature. Excessive time spent planning may be wasted anyway since projects rarely go exactly as initially planned. It’s important to recognize how much time spent on details in a plan is “enough” (i.e. when you should stop planning and start coding), which unfortunately seems to be something that only comes with experience.

I see many Developers that are not fund of estimating how long a task will take. “It’s a waste of time”, they say, “I have to do the task anyway, I’d better start right away instead of spending time coming up with an estimate that will most likely be off anyway”. 

Indeed, most of the Developers never do any estimation when they’re working on personal projects. They want to implement something, they do it – and if it takes longer than what they originally thought unconsciously, so be it. Many startups also work that way. It’s common knowledge that estimates are usually off indeed, which led us to call them “guess’timates” to make this fact obvious to everyone.

So why do we estimate? Here are a few reasons.

It helps the Customer
When you’re working on a project with a Customer ordering changes to you or your team, estimation is crucial to the Customer. It’s a key element to set a priority for the coming changes. If a change has a medium value but takes a long time to implement, you might be better off implementing something of a slightly lower value but faster to do. It also helps planning releases ahead. What matters here is not absolute time values but relative estimates between tasks.

It forces you to better understand what you’re going to do
In Agile Development, estimating stories is also a way to discuss them with the whole team to make sure the requirements are clear and nothing got overlooked. If I ask you if you can implement a “Delete post” functionality on your home-made blog, you’ll say “Sure, no problem”. Now if I ask you to break this down in tasks and estimate how long they’re going to take, you have to think it through and questions arise. “Are you allowed to delete any post, or just yours? Is there a confirmation popup? Should it be possible to undo the delete action afterwards?” You need an answer to these questions to give a proper estimate. Here the added value doesn’t come directly from the estimate; it comes from the thinking that’s involved to get the estimate.

However, helping the Customer prioritize the work and helping the team better understand the requirements is just one side of the equation

I believe estimations are crucial to help the Developer improve
And that’s why every Developer should do it, even if there’s no Customer, even if you don’t have deadlines, even if you’re OK discovering the requirements as you go. Because comparing the actual workload against the original estimate is an incredible insight.

If you thought implementing that little change would just take 1h and it actually took 3 (which is really not uncommon), something clearly went wrong. If you don’t play the game of guessing an estimate and then measuring the actual time, you’re not aware of that problem. When you’re done after the 3h you think, “Hey, that wasn’t such an easy change. What the hell, it’s done. What’s next?”

But taking a few minutes to give an estimate, and then comparing it against the actual time it took, will give you an opportunity to debrief what happened. A one-man retrospective, in a way. Why did it take 3h instead of 1?

Maybe you wasted time on your unit tests – now you know you should spend a few hours to clean them up so that they don’t bother you anymore.

Maybe you realized half-way through that your change was unexpectedly impacting other parts of the system – it’s probably a good idea to refactor a few classes to isolate responsibilities.

Or maybe you had to do repetitive tasks over and over – your IDE can surely do that for you, just spend an hour learning how.

Maybe you discovered dependencies with another team – next time you’ll be sure to involve them earlier in the loop.

Or maybe it’s just your tendency to underestimate work, very common among Developers – it’s good to be aware of it, so you can consciously correct it when planning your work.

This estimation game gives you feedback on your solution, on your tools, on your work environment, on your dependencies, and above all on yourself. This is invaluable, and this is what makes us better every day. Without it, we’re doomed to repeat the same mistakes over and over.

So start estimating now! If you don’t do it for a Customer, or for a Project, do it for you!

jibai31.wordpress.com» by Jean-Baptiste Goulain on September 26, 2013
Report a text problem
◆
