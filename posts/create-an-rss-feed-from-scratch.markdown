Create An RSS Feed From Scratch
04-11-2012

[RSS feeds][1] are a great way to stay updated with the barrage of content on the web. Unfortunately, not all websites have one available - including this one (until now). Here's a quick guide to the basic components of an RSS feed and how to create one from scratch.

<style type="text/css">
pre { font-family: monospace; color: #ffffff; background-color: #333333; }
.Special { color: #ffdead; }
.Identifier { color: #98fb98; }
.Constant { color: #ffa0a0; }
.Type { color: #bdb76b; font-weight: bold; }
.Comment { color: #87ceeb; }
</style>

###XML and RSS Element###

To start, create a text file with an .xml extension. Add the `<xml>` declaration (must be the first line), followed by the `<rss>` tags which will encompass the rest of the RSS content.

<pre>
<span class="Comment">&lt;?</span><span class="Type">xml</span><span class="Type"> </span><span class="Type">version</span>=<span class="Constant">&quot;1.0&quot;</span><span class="Type"> </span><span class="Type">encoding</span>=<span class="Constant">&quot;utf-8&quot;</span><span class="Comment">?&gt;</span>
<span class="Identifier">&lt;</span><span class="Identifier">rss</span><span class="Identifier"> </span><span class="Type">version</span>=<span class="Constant">&quot;2.0&quot;</span><span class="Identifier"> </span><span class="Type">xmlns</span><span class="Comment">:</span><span class="Type">atom</span>=<span class="Constant">&quot;http://www.w3.org/2005/Atom&quot;</span><span class="Identifier">&gt;</span>

<-- channel goes here -->

<span class="Identifier">&lt;/rss&gt;</span>
</pre>

###Channel Element###

The `<channel>` tag describes the charateristics of the RSS feed. There are many different tags that can be added to customize the channel, which are listed in the [RSS specification][2]. The channel has three required elements:

1. `<title>` - title of RSS feed
2. `<description>` - description of RSS feed
2. `<link>` - link to RSS feed

<pre>
<span class="Identifier">&lt;</span><span class="Identifier">channel</span><span class="Identifier">&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">title</span><span class="Identifier">&gt;</span>Alex Le's Blog<span class="Identifier">&lt;/title&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">description</span><span class="Identifier">&gt;</span>Alex Le's Blog<span class="Identifier">&lt;/description&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">link</span><span class="Identifier">&gt;</span>http://www.alexanderle.com<span class="Identifier">&lt;/link&gt;</span>

   <-- items goes here -->

<span class="Identifier">&lt;/channel&gt;</span>
</pre>

###Item Element###

Now comes the real meat. Items are the individual "stories" or posts that are published in the feed. They follow the same basic requirements of the channel (title, description, link). 

<pre>
   <span class="Identifier">&lt;</span><span class="Identifier">item</span><span class="Identifier">&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">title</span><span class="Identifier">&gt;</span>Create An RSS Feed From Scratch<span class="Identifier">&lt;/title&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">link</span><span class="Identifier">&gt;</span>http://alexanderle.com/blog/create-an-rss-feed.html<span class="Identifier">&lt;/link&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">description</span><span class="Identifier">&gt;</span><span class="Identifier">&lt;/description&gt;</span>
   <span class="Identifier">&lt;/item&gt;</span>
</pre>

###End Result and Validation###

Put it all together and it becomes a valid, basic RSS feed. Notice there are a couple additions, such as `<atom:link>`, `<guid>`, and `<pubDate>`. This is to meet the [W3C Feed Validation Service][3] requirements, which all feeds should be run through to validate.

<pre>
<span class="Comment">&lt;?</span><span class="Type">xml</span><span class="Type"> </span><span class="Type">version</span>=<span class="Constant">&quot;1.0&quot;</span><span class="Type"> </span><span class="Type">encoding</span>=<span class="Constant">&quot;utf-8&quot;</span><span class="Comment">?&gt;</span>
<span class="Identifier">&lt;</span><span class="Identifier">rss</span><span class="Identifier"> </span><span class="Type">version</span>=<span class="Constant">&quot;2.0&quot;</span><span class="Identifier"> </span><span class="Type">xmlns</span><span class="Comment">:</span><span class="Type">atom</span>=<span class="Constant">&quot;http://www.w3.org/2005/Atom&quot;</span><span class="Identifier">&gt;</span>
<span class="Identifier">&lt;</span><span class="Identifier">channel</span><span class="Identifier">&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">title</span><span class="Identifier">&gt;</span>Alex Le's Blog<span class="Identifier">&lt;/title&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">description</span><span class="Identifier">&gt;</span>Alex Le's Blog<span class="Identifier">&lt;/description&gt;</span>
   <span class="Identifier">&lt;</span><span class="Identifier">link</span><span class="Identifier">&gt;</span>http://www.alexanderle.com<span class="Identifier">&lt;/link&gt;</span>
   <span class="Identifier">&lt;</span><span class="Special">atom</span><span class="Comment">:</span><span class="Identifier">link</span><span class="Identifier"> </span><span class="Type">href</span>=<span class="Constant">&quot;http://alexanderle.com/feed.xml&quot;</span><span class="Identifier"> </span>
     <span class="Type">rel</span>=<span class="Constant">&quot;self&quot;</span><span class="Identifier"> </span><span class="Type">type</span>=<span class="Constant">&quot;application/rss+xml&quot;</span><span class="Identifier"> /&gt;</span>

   <span class="Identifier">&lt;</span><span class="Identifier">item</span><span class="Identifier">&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">title</span><span class="Identifier">&gt;</span>Create An RSS Feed From Scratch<span class="Identifier">&lt;/title&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">link</span><span class="Identifier">&gt;</span>http://alexanderle.com/blog/create-an-rss-feed.html<span class="Identifier">&lt;/link&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">description</span><span class="Identifier">&gt;</span><span class="Identifier">&lt;/description&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">guid</span><span class="Identifier">&gt;</span>http://alexanderle.com/blog/create-an-rss-feed.html<span class="Identifier">&lt;/guid&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">pubDate</span><span class="Identifier">&gt;</span>Wed, 11 Apr 2012 00:00:00 MST<span class="Identifier">&lt;/pubDate&gt;</span>
     <span class="Identifier">&lt;</span><span class="Identifier">author</span><span class="Identifier">&gt;</span>alex.csm@gmail.com (Alex Le)<span class="Identifier">&lt;/author&gt;</span>
   <span class="Identifier">&lt;/item&gt;</span>
<span class="Identifier">&lt;/channel&gt;</span>
<span class="Identifier">&lt;/rss&gt;</span>
</pre>

###Automation###

While editing xml document is not difficult, it can be cumbersome - especially when dealing with a lot of content. My way around this is leveraging the code that creates my site ([chisel][5]). A [Jinja2][6] template (python template language) is created that generates the "skeleton" of the RSS feed, leaving the specifics as variables:

<pre>
{% for entry in entries %}
<span class="Identifier">&lt;</span>item<span class="Identifier">&gt;</span>
  <span class="Identifier">&lt;</span><span class="Statement">title</span><span class="Identifier">&gt;</span><span class="Title">{{ entry.title }}</span><span class="Identifier">&lt;/</span><span class="Statement">title</span><span class="Identifier">&gt;</span>
  <span class="Identifier">&lt;</span><span class="Statement">link</span><span class="Identifier">&gt;</span>{{ entry.url }}<span class="Identifier">&lt;/</span><span class="Statement">link</span><span class="Identifier">&gt;</span>
  <span class="Identifier">&lt;</span>guid<span class="Identifier">&gt;</span>{{ entry.url }}<span class="Identifier">&lt;/</span>guid<span class="Identifier">&gt;</span>
  <span class="Identifier">&lt;</span>pubDate<span class="Identifier">&gt;</span>{{ entry.rss_date }}<span class="Identifier">&lt;/</span>pubDate<span class="Identifier">&gt;</span>
<span class="Identifier">&lt;/</span>item<span class="Identifier">&gt;</span>
{% endfor %}
</pre>

A simple loop through all the entries fills the variables with their appropriate content, such as entry.post\_title, entry.url, and entry.date.

Hopefully, this introduction to creating RSS feeds was useful. The full RSS xml of this page can be found (and subscribed to) [here][4].

[1]: http://en.wikipedia.org/wiki/RSS
[2]: http://www.rssboard.org/rss-specification
[3]: http://validator.w3.org/feed/
[4]: http://alexanderle.com/feed.xml
[5]: http://alexanderle.com/blog/2012/02/29/move-to-github.html
[6]: http://jinja.pocoo.org/docs/
