Sending Netflix OAuth Requests With Python
02-24-2013

Oauth is an authentication protocol that allows users to grant a third-party access to their resources - without sharing their password. Kind of similar to creating a temporary key to your car for someone, a key which can have chosen limitations and be disabled at any time. Great for users. Confusing for newbies like me working with it.

That's because each service can have a different method to "hand-shake" between the user and consumer. In a previous [post][1], I shared a [demo][2] that uses the Netflix API. It was my first experience with Oauth and it took me a while to understand all the nuances involved. Here, I'll detail how I sent non-authenticated and authenticated signed requests to Netflix with Python.

<style type="text/css">
pre { font-family: monospace; color: #ffffff; background-color: #333333; }
.Special { color: #ffdead; }
.Constant { color: #ffa0a0; }
.Identifier { color: #98fb98; }
.Comment { color: #87ceeb; }
.Statement { color: #f0e68c; font-weight: bold; }
.PreProc { color: #cd5c5c; }
</style>

###Before You Start###

1. Register your application at [http://developer.netflix.com/apps/register/][4]. A unique consumer key and secret is provided to you afterwards. Keep this for later.
2. Go over the Netflix [Authentication Overview][3]. This contains all the required info to make Netflix API requests. It also has nice information containing common REST API tasks you can send.

###Performing A Non-Authenticated Request###

The "autocomplete catalog" request searches the Netflix catalog for movies and tv shows that partially match the search string. It is a *non-authenticated* request and only requires the consumer key and a percent-encoded search string. The format of the request is as follows:

> http://api-public.netflix.com/catalog/titles/autocomplete?oauth_consumer_key=**CONSUMER_KEY**&term=**SEARCH_STRING**

To fetch the data in Python, the urllib library is used to send the request, created from the base URL and parameters:

<pre>
<span class="PreProc">import</span> urllib
<span class="PreProc">from</span> xml.etree <span class="PreProc">import</span> ElementTree <span class="Statement">as</span> ET

auto_url = <span class="Constant">&quot;<a href="http://api-public.netflix.com/catalog/titles/autocomplete">http://api-public.netflix.com/catalog/titles/autocomplete</a>&quot;</span>

auto_parameters = [
     (<span class="Constant">'term'</span>, search_string),
     (<span class="Constant">'oauth_consumer_key'</span>, CONSUMER_KEY)]

full_auto_url = auto_url + <span class="Constant">'?'</span> + urllib.urlencode(auto_parameters)

<span class="Comment"># Read autocomplete url</span>
auto_data = urllib.urlopen(full_auto_url)
</pre>

Extracting the Netflix data returned can be done by converting the XML response to an Element Object with the ElementTree library. Once in this tree-format, it can be traversed and parsed with the built-in functions:

<pre>
auto_xml = ET.fromstring(auto_data)

<span class="Comment"># Grab all titles from autocomplete search</span>
<span class="Statement">for</span> i <span class="Statement">in</span> auto_xml.findall(<span class="Constant">'.//title'</span>):
     names = i.attrib.get(<span class="Constant">'short'</span>)
</pre>

###Performing An Authenticated Signed Request###

The "catalog titles" search returns detailed information on a film and is an example of an *authenticated signed* request. It involves 4 steps prior to sending the request:

1. Setting the base URL
2. Gathering the parameters
3. Creating the base string
4. Calculating the signature 

Combining these components produces the signed request, which has the format below:

> http://api-public.netflix.com/**PATH**?parameter=**PARM**&oauth_consumer_key=**CONSUMER_KEY**&oauth_nonce=**NONCE**&oauth_signature_method=**HMAC-SHA1**&oauth_timestamp=**TIME_STAMP**&oauth_version=**1.0**&oauth_signature=**SIGNATURE**

While this may look daunting, it's not too bad once broken down. First, decide what Netflix resource you want to access (catalog/people, users/current, etc). In this example, we want more information on a particular title so we use the catalog/titles resource. The base URL thus looks like:

<pre>
TITLE_URL = <span class="Constant">'<a href="http://api-public.netflix.com/catalog/titles">http://api-public.netflix.com/catalog/titles</a>'</span>
</pre>

Second, we gather the required OAuth parameters for the Netflix request. 

+ **parm** - Optional parameter(s) that specify what data is returned. For the catalog titles search, we use the "term" parameter along with the movie/tv's title to gather the film's details.

+ **consumer_key** - Your application's consumer key.

+ **nonce** - Random string of characters to distinguish each request from one another.

+ **oauth_method** - This is always HMAC-SHA1.

+ **time_stamp** - Number of seconds since epoch (Jan 1st, 1970).

+ **oauth_version** - This is 1.0 for now.

Although not required for the base string, we'll later need the parameters to be in alphabetical order, so it's easier to keep them in order from the start. 

<pre>
<span class="PreProc">from</span> hashlib <span class="PreProc">import</span> sha1
<span class="PreProc">import</span> hmac, binascii, urllib, time, string, random

<span class="Statement">def</span> <span class="Identifier">RandomString</span>( size=<span class="Constant">6</span>, chars=string.ascii_uppercase + string.digits ):
   <span class="Statement">return</span> <span class="Constant">''</span>.join( random.choice(chars) <span class="Statement">for</span> x <span class="Statement">in</span> <span class="Identifier">range</span>(size) )


expand_parms = <span class="Constant">'synopsis,cast,formats,@episodes,@seasons'</span>
nonce = RandomString()
time_stamp = time.time()

parameters = [
   (<span class="Constant">'expand'</span>, expand_parms),
   (<span class="Constant">'max_results'</span>, <span class="Constant">'1'</span>),
   (<span class="Constant">'oauth_consumer_key'</span>, CONSUMER_KEY),
   (<span class="Constant">'oauth_nonce'</span>, nonce),
   (<span class="Constant">'oauth_signature_method'</span>, <span class="Constant">'HMAC-SHA1'</span>),
   (<span class="Constant">'oauth_timestamp'</span>, time_stamp),
   (<span class="Constant">'oauth_version'</span>, <span class="Constant">'1.0'</span>),
   (<span class="Constant">'term'</span>, term)]
</pre>

Next, we create the base string by joining the HTTP method (GET/POST), base URL, and parameters (all percent-encoded):

<pre>
<span class="Comment"># Put together base string</span>
param_encode = urllib.urlencode(parameters).replace(<span class="Constant">'+'</span>, <span class="Constant">'%20'</span>)

base_string = <span class="Constant">'GET&amp;'</span> + OAuthEscape( TITLE_URL ) + <span class="Constant">'&amp;'</span> + OAuthEscape(param_encode)
</pre>

The last piece of data to collect is the signature of the base string. This is calculated by passing your consumer **secret** and the base string to the HMAC-SHA1 hashing algorithm. Also, the result of the HMAC function needs to be base64 encoded, turning it from an unreadable binary string into readable characters:

<pre>
<span class="Statement">def</span> <span class="Identifier">OAuthEscape</span>( s ):
   <span class="Statement">return</span> urllib.quote( s, <span class="Constant">''</span> )

<span class="Statement">def</span> <span class="Identifier">GenerateSig</span>( base_string ):
   secret =  NET_SECRET + <span class="Constant">'&amp;'</span>
   hashed = hmac.new(secret, base_string , sha1)

   signed_sig = binascii.b2a_base64(hashed.digest())[:-<span class="Constant">1</span>]

   <span class="Statement">return</span> signed_sig

sign = GenerateSig( base_string )
</pre>

With the base URL, parameters, and signature set up, all that's left is to combine them together and make the request: 

<pre>
parameters.append((<span class="Constant">'oauth_signature'</span>, sign))

full_url = TITLE_URL + <span class="Constant">'?'</span> + urllib.urlencode(parameters)

<span class="Comment"># Read catalog url</span>
title_data = urllib.urlopen(full_url)

xml = ET.fromstring(title_data)
</pre>

This basic tutorial only brushes the surface of what the Netflix API has available. To see the original code, feel free to [fork my Neatflix demo][5] from Github. Try the example above or see if you can gather data from another Netflix resource. The sky is the limit on what cool applications you can conjure up.

[1]: http://alexanderle.com/blog/2012/neatflix-my-netflix-api-demo.html
[2]: http://neatflix.appspot.com/
[3]: http://developer.netflix.com/docs/Security
[4]: http://developer.netflix.com/apps/register/
[5]: https://github.com/alexle/Neatflix
