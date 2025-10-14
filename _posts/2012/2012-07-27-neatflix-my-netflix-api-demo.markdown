---
layout: post
title: "Neatflix: A Netflix API Demo"
date: 2012-07-27
tags: programming
---

[Netflix][1] is one of my guilty pleasures in life. *Guilty* because I believe TV is evil and try to limit the amount of time I spend in front of one. Yet, there are good, interesting, and entertaining shows out there which I enjoy watching every now and then and Netflix is an economical way to get some of this content.

A minor issue I have with Netflix, however, is I never know which titles are available. This is compounded by the fact I only have the "streaming" plan, which negates all the DVD/Blu-Ray selections. I often find myself wondering if a movie is available on Netflix, and if so, whether or not it is streamable.

When I discovered Netflix had an [API][3], I saw an opportunity to learn something new by creating a web app to solve this problem. Hence, [Neatflix][2] was born.

Neatflix is simple to use. Just enter a search phrase and click on any result to display its information. The search will return the top 10 titles matched in the Netflix libary. Say you wanted to find out more information about the movie "Thor". A search of this phrase would return the following:

![neatflix home page](/assets/neatflix2.png)

Clicking any button gives you a collection of important details such as the year the title was made, the length of the movie, the average Netflix rating, its availability on Netflix, a detailed synopsis, and the genre! For example, the first result would display the output below:

![neatflix result page](/assets/neatflix3.png)

That movie looks good! **And** it's available on streaming. I guess I know what I'm doing tonight. Neatflix also shows the number of episodes in a TV series as well. Ever wondered how long Season 1 of "The Walking Dead" is?

![neatflix walking dead](/assets/neatflix4.png)

Only 6 episodes, pretty short season. I wonder if Game Of Thrones is available to stream..

![neatflix game of thrones](/assets/neatflix5.png)


Dvd and Blu-Ray only. Darn!

Neatflix is only a demo at this stage, but I hope to add more features in the future. It was fun learning how to make OAuth requests, hide sensitve developer key data, parse xml, and manage data flow in a web app. I plan to share some of my experiences in a future post.

In the meantime, check out [http://neatflix.appspot.com][2] if you want some quick information on a particular Netflix title. The [source code][4] is also available publicly in my Github.

[1]: http://www.netflix.com
[2]: http://neatflix.appspot.com
[3]: http://developer.netflix.com/
[4]: https://github.com/alexle/Neatflix
