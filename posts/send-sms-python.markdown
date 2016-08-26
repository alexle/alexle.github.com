---
title: How To Send A SMS Message With Python (easy way)
date: 05-05-2011
image:
meta: how to send sms message with python smtp module gmail smtp server gateway tmobile at&t verizon sendmail
---

[Python][2] is a high-level programming language. It's easy to read, has great libraries, and is well documented. On top of it, it's extremely versatile and powerful. Python is my favorite language to work with and I've yet to come across a problem it could not solve.

Can it send text messages? You betcha! Here are the steps to send one easily:

##Load SMTP Module##
SMTP (simple mail transfer protocol) is the most common protocol for sending e-mail between mail servers. This protocol will be used to send the text message. Fortunately, Python includes a nice library of its basic functions in *smtplib*.

<pre><code class=language-python>import smtplib
</code></pre>

##Connect to Gmail SMTP Server##
Next, a secure session with Gmail's outgoing SMTP server needs to be established. A connection can be made with either TLS or SSL. In this example, the STARTTLS connection is used (port 587). The session is complete with the credentials of a valid Gmail account.

<pre><code class=language-python>server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<gmail_address>', '<gmail_password>' )
</code></pre>

##Select Phone Destination##
Now the program is ready to send e-mail. The text message will be sent by taking advantage of each mobile carrier's e-mail to SMS gateway.

For example, to send a text message to a T-Mobile number, you would use &lt;number&gt;@tmomail.net. To send a text message to an AT&T number, you would use &lt;number&gt;@mms.att.net. Here is a list of other [mail-sms gateways][1].

##Send The Message##
Once the phone destination has been identified, all that's left is to add the message and send the mail.

<pre><code class=language-python>server.sendmail( '<from>', '<number>@tmomail.net', 'Hello!' )
</code></pre>

5 lines of code. Not bad :)

[1]: https://en.wikipedia.org/wiki/List_of_SMS_gateways
[2]: http://www.python.org/
