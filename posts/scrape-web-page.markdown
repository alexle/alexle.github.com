How to scrape a web page with python (Criminal Minds)
09-27-2011    

I've been hooked on the television show [Criminal Minds][1] lately. It follows a team of FBI profilers who analyze criminal behavior to catch some twisted bad guys. It's intriguing to me why serial killers do what they do, so the study and breakdown of each criminal's psyche in the show is appealing.

Luckily for me, ION airs 1-4 episodes almost every day. The only problem is I can never remember what time the show is on. As a result, I have to go to the [ION website][2] and check what time the episodes are. Every day.

I got tired of this rather quickly and wrote a python script to "scrape" the webpage for show times. [Web scraping][3] is a technique to extract information from websites using code. There are many different ways to scrape the web; the method I used is crude but simple:

<div id="code">
<font color="#87ceeb">#!/usr/bin/python</font><br>
<br>
<font color="#cd5c5c">from</font>&nbsp;urllib <font color="#cd5c5c">import</font>&nbsp;urlopen<br>
<font color="#cd5c5c">import</font>&nbsp;re, time<br>
<br>
LINK = <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0"><a href="http://www.ionline.tv">http://www.ionline.tv</a></font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;&nbsp;<font color="#87ceeb"># url to scrape</font><br>
SHOW = <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">CRIMINAL MINDS</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color="#87ceeb"># show keyword to search on</font><br>
msg = SHOW<br>
show_index = 0<br>
<br>
content = urlopen( LINK ).read()<br>
<br>
dates_array = re.findall( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">weekdate&quot;&gt;(.*?)&lt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, content )<br>
<br>
time = re.findall( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">title&quot;&gt;(.*?)&lt;.*?eastern&quot;&gt;(.*?)&lt;.*?(/ul|&lt;li)</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, content )<br>
<br>
<font color="#f0e68c"><b>print</b></font>&nbsp;time<br>
<font color="#f0e68c"><b>for</b></font>&nbsp;date_entry <font color="#f0e68c"><b>in</b></font>&nbsp;range( len(dates_array) - 1 ):<br>
<br>
&nbsp;&nbsp; msg += <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffdead">\n</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;+ dates_array[date_entry]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#87ceeb"># iterate through dates</font><br>
<br>
&nbsp;&nbsp; <font color="#f0e68c"><b>while</b></font>&nbsp;True:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;( time[show_index][0] == SHOW ):&nbsp;&nbsp;&nbsp;&nbsp; <font color="#87ceeb"># check if show is CM</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; msg += <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffdead">\n</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;+ time[show_index][1]<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show_index += 1<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;( time[show_index-1][2] == <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">/ul</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;):&nbsp;&nbsp;<font color="#87ceeb"># marker for end of day</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <font color="#f0e68c"><b>break</b></font><br>
<br>
<font color="#f0e68c"><b>print</b></font>&nbsp;msg<br>
</div>

The procedure involves 3 steps: 

1. Read in the site's data. This is done with **urlopen( LINK ).read()**.
2. Parse the data I want (date/time) using regular expressions with **re.findall()**.
3. Run a loop to check/print matches for my show.

As of 9/27/11, running the script above produces an output of:

<blockquote>
CRIMINAL MINDS<br />
September 27<br />
9<br />
10<br />
11<br />
September 28<br />
10<br />
11<br />
September 29<br />
8<br />
9<br />
10<br />
11<br />
September 30<br />
October 1<br />
October 2<br />
October 3<br />
9<br />
10<br />
11
</blockquote>

Time and date of **every** Criminal Mind episode for the next week. Fist pump!

However, there is a downside to the script above (and web scraping in general). If the site redesigns its web page, or changes its data, there's a high probability the script/regex will be affected. For that reason, it is always preferred to use a site's API if available.

[1]: http://en.wikipedia.org/wiki/Criminal_Minds
[2]: http://www.iontelevision.com/
[3]: http://en.wikipedia.org/wiki/Web_scraping
