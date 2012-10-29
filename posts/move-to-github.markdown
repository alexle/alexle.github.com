Why I Moved My Blog To Github Pages
02-29-2012

In an earlier [post][1], I expressed my desire to write more. While Blogger was a good platform to start on, it wasn't conducive to my work flow nor management of the site. I spent more time manipulating html tags and tinkering with the css/design of the page than producing content. Thus, I researched alternatives and settled on using [Chisel][4], a static site generator.

[Static site generators][3] are programs that generates **static** HTML files which can be served through any web server. They use template languages that separate the layout of the website from the content and styles. As an added bonus, SSG's follow rule #29 of The Pragmatic Programmer, "Write code that writes code", which is just plain cool.

Here are some reasons why server-side content management systems like WordPress, Tumblr, or Blogger didn't work for me:

###WYSIWYG Editor Stinks###

The WYSIWYG, or "what you see is what you get" editor, is the plain text box used in most blogging platforms for inputting content. Some people are ok with using it to edit posts, but the WYSIWYG box is extremely limiting and causes much frustration for me. 

For example, Blogger's editor lacks:

+ efficient text movement (VIM/Emacs)
+ easy text manipulation
+ syntax highlighting
+ regex search
+ pre-defined macros
+ and much more..

Another perk of static site generators is that they create HTML content from simple text files. I personally use [MarkDown][5], which is a lightweight markup language that converts easy-to-write plain text to valid HTML. This lets me focus less on editing code tags/structures/syntax and more on writing text.

###Control Of Content###

One advantage of having your website in static HTML files is that your content is separate from the server. This makes it extremely easy to move your website to any host (Amazon S3, Heroku, Github Pages, the server in your home office) - just upload your HTML, re-route the domain name and you're good to go. Virtually all servers are able to serve HTML as well, meaning you rarely have to worry about hosting incompatibilities.

###Chance For Redesign (Bottom Up)###

I like building things, even if it's been done before. So when it came to finding a new platform, I jumped at the chance to redesign my blog from scratch and incorporate some new tools.

I decided on [Github Pages][2] to host my blog. It's a great service that publishes content from a designated Github repository. The perks include:

1. Version control - I'm able to view every change I've committed, roll files back to any version.
2. Redundancy - The source code resides on a central repository, which I can pull to any computer, anywhere. If Github goes down, I still have a copy on my local machine.

Designing the HTML+CSS was a fun experience as well. The layout is much more simple and pleasing to me now.  And I certainly don't miss the "magic" html/css/plugins added in the site's code from a CMS.

###Simplify Workflow###

Maintaining static HTML files is not for everyone, but it greatly fits my style as a software developer. I love opening a plain text file and writing, without any regards to HTML tags, having to be online, or my hands leaving the keyboard. I'm able to view my site locally as much as needed, similar to working on a "development" branch. When I'm ready to go live, I simply "git push" my changes and the site is updated.

In the end, moving to a static site has let me concentrate more on my writing, and not on the styling of my content. There are some disadvantages to static site generators, such as lack of dynamic content (comments/plugins) and RSS feeds. I haven't decided how, or even if, I'll address those yet. For now, my main goal is just to focus on content.

*Feel free to [fork][6] my blog!

[1]: http://alexanderle.com/blog/2012/02/07/farewell-blogger.html
[2]: http://pages.github.com/
[3]: http://iwantmyname.com/blog/2011/02/list-static-website-generators.html
[4]: https://github.com/dz/chisel
[5]: http://tedwise.com/markdown/
[6]: https://github.com/alexle/alexle.github.com
