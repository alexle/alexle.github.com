---
layout: post
title: "How To Setup A Simple HTTP Server With Python"
date: 2012-02-09
tags: programming
---

There are times when you need to setup a quick web server to test your web applications. For basic applications which don't require database or server-side language support, Python has a [module][1] to run a mini web server on your system. It takes no time to configure and eats up very little system resources!

## SimpleHTTPServer by command line ##

Open up a terminal and go to the directory you would like to start the web server:

``` python
$ cd /home/somedirectory
```

To start the server, simply type:

``` python
$ python -m SimpleHTTPServer
```

That's it! Now your HTTP server will run in port 8000. You can access it via [localhost:8000](http://localhost:8000/) or [127.0.0.1:8000](http://127.0.0.1:8000/). If the directory has a file named "index.html", it will be served as the initial file. If there is no "index.html", then the files in the directory will be listed. To quit the web server, use CTRL+C.

If you wish to change the port, it can be configured as an additional parameter:

``` python
$ python -m SimpleHTTPServer 8200
```

## SimpleHTTPServer by python script ##

The SimpleHTTPServer can also be started in a script. Here's a snippet of the code I use:

``` python
import sys, SimpleHTTPServer, BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

SimpleHTTPRequestHandler.protocol_version = "HTTP/1.0"

httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)

sa = httpd.socket.getsockname()

print "Serving HTTP on", sa[0], sa[1], "..."

httpd.serve_forever()
```

And there you go. Happy web serving!

[1]: http://docs.python.org/library/simplehttpserver.html
