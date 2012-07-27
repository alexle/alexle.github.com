Neatflix: A Netflix API Demo
07-27-2012

[Netflix][1] is one of my guilty pleasures in life. *Guilty* because I believe TV is evil and try to limit the amount of time I spend in front of one. Yet, there are good, interesting, and entertaining shows out there which I enjoy watching every now and then and Netflix is an economical way to get some of this content.

A minor issue I have with Netflix, however, is that I never know which titles are available. This is compounded by the fact that I only have the "streaming" plan, which negates all the DVD/Blu-Ray selections. I often find myself wondering if a movie is available on Netflix, and if yes, whether or not it is streamable.

When I discovered that Netflix has an [API][3], I saw an opportunity to hone my skills and learn something new by creating a web app to solve this problem. Hence, [Neatflix][2] was born.

Neatflix is simple to use. Just enter a search phrase and click on any result to display its information. The search will return the top 10 titles matched in the Netflix libary. Say you wanted to find out more information about the movie "Thor". A search of this phrase would return the following:

<a href="/static/neatflix2.png"><img src="/static/neatflix2.png" style="display:block; margin-left:auto; margin-right:auto; border:1px solid #999;" width="560px" /></a>

Clicking any button gives you a collection of important details such as the year the title was made, the length of the movie, the average Netflix rating, its availability on Netflix, a detailed synopsis, and the genre! For example, the first result would display the output below:

<a href="/static/neatflix3.png"><img src="/static/neatflix3.png" style="display:block; margin-left:auto; margin-right:auto; border:1px solid #999;" width="560px" /></a>

That movie looks good! **And** it's available on streaming. I guess I know what I'm doing tonight. Neatflix also shows the number of episodes in a TV series as well. Ever wondered how long Season 1 of "The Walking Dead" is?

<a href="/static/neatflix4.png"><img src="/static/neatflix4.png" style="display:block; margin-left:auto; margin-right:auto; border:1px solid #999;" width="560px" /></a>

Only 6 episodes, pretty short season. I wonder if Game Of Thrones is available to stream..

<a href="/static/neatflix5.png"><img src="/static/neatflix5.png" style="display:block; margin-left:auto; margin-right:auto; border:1px solid #999;" width="560px" /></a>

Dvd and Blu-Ray only. Darn!

Neatflix is only a demo at this stage, but I hope to add more features in the future. It was fun learning about how to make OAuth requests, hide sensitve developer key data, and manage data flow in a web app. I plan to share some of my experiences in a future post.

In the meantime, check out [http://neatflix.appspot.com][2] if you want some quick information on a particular Netflix title. The [source code][4] is also available publicly in my Github. 

[1]: http://www.netflix.com
[2]: http://neatflix.appspot.com
[3]: http://developer.netflix.com/
[4]: https://github.com/alexle/Neatflix
