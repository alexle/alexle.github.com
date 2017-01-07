---
title: Create An RSS Feed From Scratch
date: 04-11-2012
image:
meta: A tutorial on how to create and RSS Feed from scratch. Create your own rss.xml file.
code: True
---

[RSS feeds][1] are a great way to stay updated with the barrage of content on the web. Unfortunately, not all websites have one available - including this one (until now). Here's a quick guide to the basic components of an RSS feed and how to create one from scratch.


##XML and RSS Element##

To start, create a text file with an .xml extension. Add the `<xml>` declaration (must be the first line), followed by the `<rss>` tags which will encompass the rest of the RSS content.

<pre><code class=language-xml>&lt;?xml version="1.0" encoding="utf-8"?>
&lt;rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">

<-- channel goes here -->

&lt;/rss>
</code></pre>

##Channel Element##

The `<channel>` tag describes the characteristics of the RSS feed. There are many different tags can be added to customize the channel, which are listed in the [RSS specification][2]. The channel has three required elements:

1. `<title>` - title of RSS feed
2. `<description>` - description of RSS feed
2. `<link>` - link to RSS feed

<pre><code class=language-xml>&lt;channel>
   &lt;title>Alex Le's Blog&lt;/title>
   &lt;description>Alex Le's Blog&lt;/description>
   &lt;link>http://www.alexanderle.com&lt;/link>

   <-- items goes here -->

&lt;/channel>
</code></pre>

##Item Element##

Now comes the real meat. Items are the individual "stories" or posts which are published in the feed. All elements of the Item element are optional, as long as at least one title or description is present.

<pre><code class=language-xml>&lt;item>
   &lt;title>Create An RSS Feed From Scratch&lt;/title>
   &lt;link>http://alexanderle.com/blog/create-an-rss-feed.html&lt;/link>
&lt;/item>
</code></pre>

##End Result and Validation##

Put it all together and it becomes a valid, basic RSS feed. Notice there are a couple additions, such as `<atom:link>`, `<guid>`, and `<pubDate>`. This is to meet the [W3C Feed Validation Service][3] requirements, which all feeds should be run through to validate.

<pre><code class=language-xml>&lt;?xml version="1.0" encoding="utf-8"?>
&lt;rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
&lt;channel>
   &lt;title>Alex Le's Blog&lt;/title>
   &lt;description>Alex Le's Blog&lt;/description>
   &lt;link>http://www.alexanderle.com&lt;/link>
   &lt;atom:link href="http://alexanderle.com/feed.xml"
     rel="self" type="application/rss+xml" />

   &lt;item>
     &lt;title>Create An RSS Feed From Scratch&lt;/title>
     &lt;link>http://alexanderle.com/blog/create-an-rss-feed.html&lt;/link>
     &lt;guid>http://alexanderle.com/blog/create-an-rss-feed.html&lt;/guid>
     &lt;pubDate>Wed, 11 Apr 2012 00:00:00 MST&lt;/pubDate>
   &lt;/item>
&lt;/channel>
&lt;/rss>
</code></pre>

##Automation##

While editing xml document is not difficult, it can be cumbersome - especially when dealing with a lot of content. My way around this is leveraging the code which build my static site ([chisel][5]). I create a [Jinja2][6] template (python template language) that generates the "skeleton" of the RSS feed, leaving the specifics as variables:

<pre><code class=language-html>{% for entry in entries %}
&lt;item>
   &lt;title>{{ entry.title }}&lt;/title>
   &lt;link>{{ entry.url }}&lt;/link>
   &lt;guid>{{ entry.url }}&lt;/guid>
   &lt;pubDate>{{ entry.rss_date }}&lt;/pubDate>
&lt;/item>
{% endfor %}
</code></pre>

A simple loop through all the entries fills the variables with their appropriate content, such as entry.post\_title, entry.url, and entry.date.

Hopefully, this introduction to creating RSS feeds was useful. The full RSS xml of this page can be found (and subscribed to) [here][4].

[1]: http://en.wikipedia.org/wiki/RSS
[2]: http://www.rssboard.org/rss-specification
[3]: http://validator.w3.org/feed/
[4]: /feed.xml
[5]: /blog/2012/02/29/move-to-github.html
[6]: http://jinja.pocoo.org/docs/
