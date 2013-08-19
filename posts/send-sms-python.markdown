How To Send A SMS Message With Python (easy way)
05-05-2011

[Python][2] is a high-level programming language. It's easy to read, has great libraries, and is well documented. On top of that, it's extremely versatile and powerful. Python is my favorite language to work with and I've yet to come across a problem that it could not solve.

Can it send text messages? You betcha! Here are the steps to send one easily:

###Load SMTP Module###
SMTP (simple mail transfer protocol) is the most common protocol for sending e-mail between mail servers. This protocol will be used to send the text message. Fortunately, Python includes a nice library of its basic functions in *smtplib*.

<div id="code">
<font color="#cd5c5c">import</font>&nbsp;smtplib<br>
</div>

###Connect to Gmail SMTP Server###
Next, a secure session with Gmail's outgoing SMTP server needs to be established. A connection can be made with either TLS or SSL. In this example, the STARTTLS connection is used (port 587). The session is complete with the credentials of a valid Gmail account.

<div id="code">
server = smtplib.SMTP( <span style="background-color: #333333"><font color="#ffffff">&quot;</font></span><font color="#ffa0a0">smtp.gmail.com</font><span style="background-color: #333333"><font color="#ffffff">&quot;</font></span>, 587 )<br>
server.starttls()<br>
server.login( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;gmail_address&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;gmail_password&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;)<br>
</div>

###Select Phone Destination###
Now the program is ready to send e-mail. The text message will be sent by taking advantage of each mobile carrier's e-mail to SMS gateway.

For example, to send a text message to a T-Mobile number, you would use &lt;number&gt;@tmomail.net. To send a text message to an AT&T number, you would use &lt;number&gt;@mms.att.net. Here is a list of other [mail-sms gateways][1].

###Send The Message###
Once the phone destination has been identified, all that's left is to add the message and send the mail.

<div id="code">
server.sendmail( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;from&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;number&gt;@tmomail.net</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">Hello!</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;)<br>
</div>

5 lines of code. Not bad :)

[1]: https://en.wikipedia.org/wiki/List_of_SMS_gateways
[2]: http://www.python.org/
