---
layout: post
title: "Sending Netflix OAuth Requests With Python"
date: 2013-02-24
tags: programming
---

Oauth is an authentication protocol which allows users to grant a third-party access to their resources - without sharing their password. Kind of similar to creating a temporary key to your car for someone, a key which can have chosen limitations and be disabled at any time. Great for users. Confusing for newbies like me working with it.

That's because each service can have a different method to "hand-shake" between the user and consumer. In a previous [post][1], I shared a [demo][2] which uses the Netflix API. It was my first experience with Oauth and it took me a while to understand all the nuances involved. Here, I'll detail how I sent non-authenticated and authenticated signed requests to Netflix with Python.

##Before You Start##

1. Register your application at [http://developer.netflix.com/apps/register/][4]. A unique consumer key and secret is provided to you afterwards. Keep this for later.
2. Go over the Netflix [Authentication Overview][3]. This contains all the required info to make Netflix API requests. It also has nice information containing common REST API tasks you can send.

##Performing A Non-Authenticated Request##

The "autocomplete catalog" request searches the Netflix catalog for movies and tv shows which partially match the search string. It's a *non-authenticated* request and only requires the consumer key and a percent-encoded search string. The format of the request is as follows:

<pre><code class=language-html>http://api-public.netflix.com/catalog/titles/autocomplete?oauth_consumer_key=CONSUMER_KEY&term=SEARCH_STRING
</code></pre>

To fetch the data in Python, the urllib library is used to send the request, created from the base URL and parameters:

<pre><code class=language-python>import urllib
from xml.etree import ElementTree as ET

auto_url = "http://api-public.netflix.com/catalog/titles/autocomplete"

auto_parameters = [
     ('term', search_string),
     ('oauth_consumer_key', CONSUMER_KEY)]

full_auto_url = auto_url + '?' + urllib.urlencode(auto_parameters)

# Read autocomplete url
auto_data = urllib.urlopen(full_auto_url)
</code></pre>

Extracting the Netflix data returned can be done by converting the XML response to an Element Object with the ElementTree library. Once in this tree-format, it can be traversed and parsed with the built-in functions:

<pre><code class=language-python>auto_xml = ET.fromstring(auto_data)

# Grab all titles from autocomplete search
for i in auto_xml.findall('.//title'):
     names = i.attrib.get('short')
</code></pre>

##Performing An Authenticated Signed Request##

The "catalog titles" search returns detailed information on a film and is an example of an *authenticated signed* request. It involves 4 steps prior to sending the request:

1. Setting the base URL
2. Gathering the parameters
3. Creating the base string
4. Calculating the signature

Combining these components produces the signed request, which has the format below:

<pre><code class=language-html>http://api-public.netflix.com/PATH?parameter=PARM&oauth_consumer_key=CONSUMER_KEY&oauth_nonce=NONCE&oauth_signature_method=HMAC-SHA1&oauth_timestamp=TIME_STAMP&oauth_version=1.0&oauth_signature=SIGNATURE
</code></pre>

While this may look daunting, it's not too bad once broken down. First, decide what Netflix resource you want to access (catalog/people, users/current, etc). In this example, we want more information on a particular title so we use the catalog/titles resource. The base URL thus looks like:

<pre><code class=language-html>TITLE_URL = 'http://api-public.netflix.com/catalog/titles'
</code></pre>

Second, we gather the required OAuth parameters for the Netflix request.

+ **parm** - Optional parameter(s) which specify what data is returned. For the catalog titles search, we use the "term" parameter along with the movie/tv's title to gather the film's details.

+ **consumer_key** - Your application's consumer key.

+ **nonce** - Random string of characters to distinguish each request from one another.

+ **oauth_method** - This is always HMAC-SHA1.

+ **time_stamp** - Number of seconds since epoch (Jan 1st, 1970).

+ **oauth_version** - This is 1.0 for now.

Although not required for the base string, we'll later need the parameters to be in alphabetical order, so it's easier to keep them in order from the start.

<pre><code class=language-python>from hashlib import sha1
import hmac, binascii, urllib, time, string, random

def RandomString( size=6, chars=string.ascii_uppercase + string.digits ):
   return ''.join( random.choice(chars) for x in range(size) )

expand_parms = 'synopsis,cast,formats,@episodes,@seasons'
nonce = RandomString()
time_stamp = time.time()

parameters = [
   ('expand', expand_parms),
   ('max_results', '1'),
   ('oauth_consumer_key', CONSUMER_KEY),
   ('oauth_nonce', nonce),
   ('oauth_signature_method', 'HMAC-SHA1'),
   ('oauth_timestamp', time_stamp),
   ('oauth_version', '1.0'),
   ('term', term)]
</code></pre>

Next, we create the base string by joining the HTTP method (GET/POST), base URL, and parameters (all percent-encoded):

<pre><code class=language-python># Put together base string
param_encode = urllib.urlencode(parameters).replace('+', '%20')

base_string = 'GET&' + OAuthEscape( TITLE_URL ) + '&' + OAuthEscape(param_encode)
</code></pre>

The last piece of data to collect is the signature of the base string. This is calculated by passing your consumer **secret** and the base string to the HMAC-SHA1 hashing algorithm. Also, the result of the HMAC function needs to be base64 encoded, turning it from an unreadable binary string into readable characters:

<pre><code class=language-python>def OAuthEscape( s ):
   return urllib.quote( s, '' )

def GenerateSig( base_string ):
   secret =  NET_SECRET + '&'
   hashed = hmac.new(secret, base_string , sha1)

signed_sig = binascii.b2a_base64(hashed.digest())[:-1]

return signed_sig

sign = GenerateSig( base_string )
</code></pre>

With the base URL, parameters, and signature set up, all that's left is to combine them together and make the request:

<pre><code class=language-python>parameters.append(('oauth_signature', sign))

full_url = TITLE_URL + '?' + urllib.urlencode(parameters)

# Read catalog url
title_data = urllib.urlopen(full_url)

xml = ET.fromstring(title_data)
</code></pre>

This basic tutorial only brushes the surface of what the Netflix API has available. To see the original code, feel free to [fork my Neatflix demo][5] from Github. Try the example above or see if you can gather data from another Netflix resource. The sky is the limit on what cool applications you can conjure up.

[1]: /blog/2012/neatflix-my-netflix-api-demo.html
[2]: http://neatflix.appspot.com/
[3]: http://developer.netflix.com/docs/Security
[4]: http://developer.netflix.com/apps/register/
[5]: https://github.com/alexle/Neatflix
