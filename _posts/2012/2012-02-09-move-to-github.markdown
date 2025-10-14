---
layout: post
title: "Why I Moved My Blog To Github Pages"
date: 2012-02-09
tags: programming
---

In an earlier [post][1], I expressed my desire to write more. While Google Blogger was a good platform to start on, I quickly realized how closed and limiting it was.

*  When you use a hosted platform like Wordpress, Blogger, or Tumblr, you don't own the site. The host does. Remember when the blogging site Posterous shut down? Everyone'custom page designs, blog links, and content disappeared.
* There are restrictions on what you can customize and how. Most solutions involve wedging using plug-ins which don't quite fit, or purchasing expensive pre-made themes (which are also inflexible themselves).
* Hosted platforms don't offer methods to back-up your content, nor allow you to switch to a different platform easily.

After some research, I found an interesting alternative for my blog -- static websites. How do these differ from traditional blogging platforms?

Well, static websites serve simple html/css pages **as they are stored** on the webserver's file system. Think of accessing FTP files in the old days. There's no application which generates the site dynamically when requested. There's no complicated back-end server.

Most static sites are created from [static site generators][3]. These are small programs which convert text files into an HTML website. It's generally done through the use of template languages.

As an added bonus, static site generators follow rule #29 of The Pragmatic Programmer, "Write code that writes code" -- How cool is that?  

The advantages of static sites are numerous. Here are the main reasons why server-side content management systems like WordPress, Tumblr, and Blogger didn't work for me:

## 1. Control Of My Content ##

The major advantage of having my website in static HTML files is I **own my content**. The code that generates the site. The templates that shape my HTML/CSS. The folder of plain text files which contain all my blog's content.

This gives me much freedom in creating and hosting my blog. Want to switch ito a different site generator? No problem, the input source to them are plain [Markdown][5] files. Interested in trying a template languages? Easy, just modify the static site generator code. Unhappy with current host? Just upload them final static HTML pages to a different server!

## 2. WYSIWYG Editor Stinks ##

The WYSIWYG, or "what you see is what you get" editor, is the plain text box used in most blogging platforms for inputting text. Some people are ok with using it to edit posts, but the WYSIWYG box is extremely limiting for me.

As a software developer, I live in my VIM text editor. This includes:

+ efficient text movement (VIM)
+ easy text manipulation (dw, yy)
+ syntax highlighting
+ regex search
+ pre-defined macros
+ and much more..

Writing page after page using the WYSIWYG is a pain-staking endeavor.

## 3. Simple, Minimal ##

An appeal of moving to a static site is the simplicity of it. Markdown text file goes in, HTML file comes out. Everything is stripped down to the bare minimum. There's no complicated databases, no hard to navigate GUI's, no extra bells and whistles I won't use.

## 4. Additional Tools ##

Another advantage of having the site reside in my workspace is it allows me to use additional tools to navigate/manipulate my files.

Power search options via the command line can be used, such as *find -iname ./* and *grep -r*. Want to change all instances of "volvo" to "Volvo"? It's a one-line operation in VIM or Bash. Want to rename all your text files? SED and AWK are at your disposal.

## 5. Chance For Redesign (Bottom Up) ##

Let's admit, building things is fun. So when it came to finding a new platform, I jumped at the chance to redesign my blog from scratch and learn some new tools.

I decided on [Github Pages][2] to host my blog. It's a great service which publishes content from a designated Github repository. The perks include:

1. Version control - I'm able to view every change I've committed, roll files back to any version.
2. Redundancy - The source code resides on a central repository, which I can pull to any computer, anywhere. If Github goes down, I still have a copy on my local machine.

Designing the HTML/CSS was a fun experience as well. The layout is much more simple and maintainable now. And I certainly don't miss the "magic" HTML/CSS/plugins added in the site's code from a CMS.

## 6. Simplify Workflow ##

Maintaining static HTML files is not for everyone, but it greatly fits my style as a software developer. I love opening a plain text file and typing away, without any regards to HTML tags, having to be online, or my hands leaving the keyboard.

I'm able to view my site locally as much as needed, similar to working on a "development" branch. When I'm ready to go live, I simply "git push" my changes and the site is updated.

<hr>

In the end, moving to a static site gave me the freedom and control I was looking for in a blogging platform. It has let me concentrate more on my writing, and not on the management of unneeded features.

Also, I've greatly enjoyed starting from a minimal setup and adding in new features as I go, such as my [own RSS feed][7], a local server for development, and just recently, custom syntax highlighting.

If you're curious, I settled on using [Chisel][4], a static site generator which is only **104 lines** of python. Feel free to [fork][6] it on my Github!

[1]: /farewell-blogger.html
[2]: http://pages.github.com/
[3]: http://iwantmyname.com/blog/2011/02/list-static-website-generators.html
[4]: https://github.com/dz/chisel
[5]: http://tedwise.com/markdown/
[6]: https://github.com/alexle/alexle.github.com
[7]: /create-an-rss-feed-from-scratch.html
