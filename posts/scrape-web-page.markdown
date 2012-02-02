How to scrape a web page with python (Criminal Minds)
09-27-2011    

I've been hooked on the television show Criminal Minds lately. It follows a team of FBI profilers who analyze criminal behavior to catch some twisted bad guys. It's intriguing to me why serial killers do what they do, so the study and breakdown of each criminal's psyche in the show is appealing.

Luckily for me, ION airs 1-4 episodes almost every day. The only problem is I can never remember what time the show is on. As a result, I have to go to the ION website and check what time the episodes are. Every day.

I got tired of this rather quickly and wrote a python script to "scrape" the webpage for show times. Web scraping is a technique to extract information from websites using code. There are many different ways to scrape the web; the method I used is crude but simple:
#!/usr/bin/python

from urllib import urlopen
import re, time

LINK = 'http://www.ionline.tv' # url to scrape
SHOW = 'CRIMINAL MINDS' # show keyword to search on
msg = SHOW
show_index = 0

content = urlopen( LINK ).read()

dates_array = re.findall( 'weekdate">(.*?)<', content )

time = re.findall( 'title">(.*?)<.*?eastern">(.*?)<.*?(/ul|<li)', content )

for date_entry in range( len(dates_array) - 1 ):

  msg += '\n' + dates_array[date_entry] # iterate through dates

  while True:
    if ( time[show_index][0] == SHOW ): # check if show is CM
      msg += '\n' + time[show_index][1]

    show_index += 1

    if ( time[show_index-1][2] == '/ul' ): # marker for end of day
      break

print msg
The procedure involves 3 steps: 
Read in the site's data. This is done with urlopen( LINK ).read().
Parse the data I want (date/time) using regular expressions with re.findall().
Run a loop to check/print matches for my show.
As of 9/27/11, running the script above produces an output of:
CRIMINAL MINDS
September 27
9
10
11
September 28
10
11
September 29
8
9
10
11
September 30
October 1
October 2
October 3
9
10
11
Time and date of every Criminal Mind episode for the next week. Fist pump!

However, there is a downside to the script above (and web scraping in general). If the site redesigns its web page, or changes its data, there's a high probability the script/regex will be affected. For that reason, it is always preferred to use a site's API if available.
