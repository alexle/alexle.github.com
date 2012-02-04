How to scrape a web page with python (Criminal Minds)
09-27-2011    

I've been hooked on the television show [Criminal Minds](http://en.wikipedia.org/wiki/Criminal_Minds) lately. It follows a team of FBI profilers who analyze criminal behavior to catch some twisted bad guys. It's intriguing to me why serial killers do what they do, so the study and breakdown of each criminal's psyche in the show is appealing.

Luckily for me, ION airs 1-4 episodes almost every day. The only problem is I can never remember what time the show is on. As a result, I have to go to the [ION website](http://www.iontelevision.com/) and check what time the episodes are. Every day.

I got tired of this rather quickly and wrote a python script to "scrape" the webpage for show times. [Web scraping](http://en.wikipedia.org/wiki/Web_scraping) is a technique to extract information from websites using code. There are many different ways to scrape the web; the method I used is crude but simple:

<blockquote>
#!/usr/bin/python<br />
<br />
from urllib import urlopen<br />
import re, time<br />
<br />
LINK = 'http://www.ionline.tv'  # url to scrape<br />
SHOW = 'CRIMINAL MINDS'         # show keyword to search on<br />
msg = SHOW<br />
show_index = 0<br />
<br />
content = urlopen( LINK ).read()<br />
<br />
dates_array = re.findall( 'weekdate"&gt;(.*?)&lt;', content )<br />
<br />
time = re.findall( 'title"&gt;(.*?)&lt;.*?eastern"&gt;(.*?)&lt;.*?(/ul|&lt;li)', content )<br />
<br />
for date_entry in range( len(dates_array) - 1 ):<br />
<br />
&nbsp;&nbsp;msg += '\n' + dates_array[date_entry]      # iterate through dates<br />
<br />
&nbsp;&nbsp;while True:<br />
&nbsp;&nbsp;&nbsp;&nbsp;if ( time[show_index][0] == SHOW ):     # check if show is CM<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg += '\n' + time[show_index][1]<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;show_index += 1<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;if ( time[show_index-1][2] == '/ul' ):  # marker for end of day<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br />
<br />
print msg
</blockquote>

The procedure involves 3 steps: 

1. Read in the site's data. This is done with <b>urlopen( LINK ).read()</b>.
2. Parse the data I want (date/time) using regular expressions with <b>re.findall()</b>.
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

</blockquote>

Time and date of <b>every</b> Criminal Mind episode for the next week. Fist pump!

However, there is a downside to the script above (and web scraping in general). If the site redesigns its web page, or changes its data, there's a high probability the script/regex will be affected. For that reason, it is always preferred to use a site's API if available.
