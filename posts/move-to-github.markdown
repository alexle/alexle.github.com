Why I Moved My Blog To Github Pages
02-29-2012

In an earlier [post][1], I expressed my desire to write more. While Blogger was a good platform to start on, it wasn't conducive to my work flow nor management of the site. After much research, I settled on using [Chisel][4], a static site generator that is only **104 lines** of python.

[Static site generators][3] are simply programs that generate an HTML website as an output. They usually use template languages that process content information into flat, HTML pages that can be served through any web server. As an added bonus, static site generators follow rule #29 of The Pragmatic Programmer, "Write code that writes code", which is very cool.

Here are some reasons why server-side content management systems like WordPress, Tumblr, and Blogger didn't work for me:

###WYSIWYG Editor Stinks###

The WYSIWYG, or "what you see is what you get" editor, is the plain text box used in most blogging platforms for inputting content. Some people are ok with using it to edit posts, but the WYSIWYG box is extremely limiting and causes much frustration for me. 

For example, Blogger's editor does not have:

+ efficient text movement (VIM/Emacs)
+ easy text manipulation (dw, yy)
+ syntax highlighting
+ regex search
+ pre-defined macros
+ and much more..

Additionally, the act of writing flows much easier using a markup language, which most static site generators use. These languages convert plain text into HTML, avoiding the constant overhead of mixing HTML tags, text, and formatting. I personally use [MarkDown][5], which is lightweight and commonly available. This lets me focus less on editing code/structures/syntax and more on writing text.

###Control Of Content###

The major advantage of having your website in static HTML files is that you **own your content**. Your content is separate from the server, allowing you to easily move your website to any host (Amazon S3, Heroku, Github Pages, the server in your home office). Just upload your HTML, re-route the domain name and you're good to go. Virtually all servers are able to serve HTML as well, meaning you rarely have to worry about hosting incompatibilities.

When Posterous went down, its users lost their settings, page links, and comments. The only data they could salvage were their blog posts, but even that involved a limited and pain-staking migration process.

As an added bonus, since all the files reside statically in your workspace, you can easily search your entire blog for any files (*find -iname ./*) or specific text (*grep -r*) via the command line.

###Chance For Redesign (Bottom Up)###

I like building things, even if it's been done before. So when it came to finding a new platform, I jumped at the chance to redesign my blog from scratch and incorporate some new tools.

I decided on [Github Pages][2] to host my blog. It's a great service that publishes content from a designated Github repository. The perks include:

1. Version control - I'm able to view every change I've committed, roll files back to any version.
2. Redundancy - The source code resides on a central repository, which I can pull to any computer, anywhere. If Github goes down, I still have a copy on my local machine.

Designing the HTML+CSS was a fun experience as well. The layout is much more simple and pleasing to me now.  And I certainly don't miss the "magic" html/css/plugins added in the site's code from a CMS.

###Simplify Workflow###

Maintaining static HTML files is not for everyone, but it greatly fits my style as a software developer. I love opening a plain text file and typing away, without any regards to HTML tags, having to be online, or my hands leaving the keyboard. I'm able to view my site locally as much as needed, similar to working on a "development" branch. When I'm ready to go live, I simply "git push" my changes and the site is updated.

In the end, moving to a static site has let me concentrate more on my writing, and not on the styling of my content. There are some disadvantages to static site generators, such as lack of dynamic content (comments/plugins) and [RSS feeds][7]. I haven't decided how, or even if, I'll address those yet. For now, my main goal is just to focus on content.

*Feel free to [fork][6] my blog!

[1]: http://alexanderle.com/blog/2012/02/07/farewell-blogger.html
[2]: http://pages.github.com/
[3]: http://iwantmyname.com/blog/2011/02/list-static-website-generators.html
[4]: https://github.com/dz/chisel
[5]: http://tedwise.com/markdown/
[6]: https://github.com/alexle/alexle.github.com
[7]: http://alexanderle.com/blog/2012/create-an-rss-feed-from-scratch.html
