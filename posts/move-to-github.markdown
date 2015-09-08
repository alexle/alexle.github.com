Why I Moved My Blog To Github Pages
02-29-2012

In an earlier [post][1], I expressed my desire to write more. While Blogger was a good platform to start on, it wasn't conducive to my work flow nor management of the site. After much research, I settled on using [Chisel][4], a static site generator that is only **104 lines** of python.

[Static site generators][3] are simply programs that process raw content into an HTML website. This is generally done through the use of template languages. As an added bonus, static site generators follow rule #29 of The Pragmatic Programmer, "Write code that writes code" -- How cool is that?

Here are the main reasons why server-side content management systems like WordPress, Tumblr, and Blogger didn't work for me:

###1. Simple, Minimal###

A main appeal of moving to Github Pages is the simplicity of it. Everything is stripped down to the bare minimum. There's no bloat, no databases.

Just simple text files that get converted to static HTML pages. Which in most cases, is fast!

###2. WYSIWYG Editor Stinks###

The WYSIWYG, or "what you see is what you get" editor, is the plain text box used in most blogging platforms for inputting text. Some people are ok with using it to edit posts, but the WYSIWYG box is extremely limiting for me. 

For example, Blogger's editor does not have:

+ efficient text movement (VIM/Emacs)
+ easy text manipulation (dw, yy)
+ syntax highlighting
+ regex search
+ pre-defined macros
+ and much more..

Additionally, the act of writing flows much easier using a markup language, which most static site generators use. [MarkDown][5], for example, can easily be converted into HTML. This lets me focus less on editing code/structures/syntax and more on writing text.

###3. Control Of My Content###

The major advantage of having my website in static HTML files is that I **own my content**. The code that generates the site. The templates that shape my HTML/CSS. The contentof each blog post in raw text.

This gives me the freedom of switching site generators or template languages. Or moving my site to another host (just upload static HTML). Could you migrate a blog from Workdpress over to Tumblr easily?

When Posterous went down, its users lost their settings, page layouts, blog links, and comments. The only data they could salvage were the words in their blog posts, but even that involved a pain-staking migration process.

###4. Additional Tools###

Another advantage of having the site reside in my workspace is it allows me to use additional tools to navigate/manipulate my files.

Power search options via the command line can be used, such as searching my entire blog for any files (*find -iname ./*) or perhaps a specific group of text (*grep -r*). Want to change all instances of "volvo" to "Volvo"? It's a one-line operation.

Having control over your data/files allows you endless levels of editing.

###5. Chance For Redesign (Bottom Up)###

Let's admit, building things is fun. So when it came to finding a new platform, I jumped at the chance to redesign my blog from scratch and learn some new tools.

I decided on [Github Pages][2] to host my blog. It's a great service that publishes content from a designated Github repository. The perks include:

1. Version control - I'm able to view every change I've committed, roll files back to any version.
2. Redundancy - The source code resides on a central repository, which I can pull to any computer, anywhere. If Github goes down, I still have a copy on my local machine.

Designing the HTML+CSS was a fun experience as well. The layout is much more simple and pleasing to me now.  And I certainly don't miss the "magic" HTML/CSS/plugins added in the site's code from a CMS.

###6. Simplify Workflow###

Maintaining static HTML files is not for everyone, but it greatly fits my style as a software developer. I love opening a plain text file and typing away, without any regards to HTML tags, having to be online, or my hands leaving the keyboard.

I'm able to view my site locally as much as needed, similar to working on a "development" branch. When I'm ready to go live, I simply "git push" my changes and the site is updated.

<hr> 

In the end, moving to a static site has let me concentrate more on my writing, and not on the styling of my content. There are some disadvantages to static site generators, such as lack of dynamic content (comments/plugins) and [RSS feeds][7]. I haven't decided how, or even if, I'll address those yet. For now, my main goal is just to focus on content.

*Feel free to [fork][6] my blog!

[1]: blog/2012/02/07/farewell-blogger.html
[2]: http://pages.github.com/
[3]: http://iwantmyname.com/blog/2011/02/list-static-website-generators.html
[4]: https://github.com/dz/chisel
[5]: http://tedwise.com/markdown/
[6]: https://github.com/alexle/alexle.github.com
[7]: blog/2012/create-an-rss-feed-from-scratch.html
