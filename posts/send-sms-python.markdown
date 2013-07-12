How To Send A SMS Message With Python (easy way)
05-05-2011

Python is a scripting programming language. It's easy to read, has great libraries, is documented very well, and is extremely versatile and powerful. It's my favorite language to work with and I have yet to come across a problem that it could not solve.

Can it send text messages? You betcha!

You'll be using the SMTP (Simple Mail Transfer Protocol) library. It's the most common protocol for sending mail and its communication is done using TCP.

<div id="code">
<font color="#cd5c5c">import</font>&nbsp;smtplib<br>
</div>

Next, establish a secure session with gmail's outgoing SMTP server using your gmail account. A TLS or SSL connection must be used; the example below uses STARTTLS which is port 587.

<div id="code">
server = smtplib.SMTP( <span style="background-color: #333333"><font color="#ffffff">&quot;</font></span><font color="#ffa0a0">smtp.gmail.com</font><span style="background-color: #333333"><font color="#ffffff">&quot;</font></span>, 587 )<br>
server.starttls()<br>
server.login( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;gmail_address&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;gmail_password&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;)<br>
</div>

Now you're set up to send email. You will send a text message by taking advantage of each mobile carrier's email to SMS gateway!

For example, to send a text message to a t-mobile number, you would use &lt;number&gt;@tmomail.net. To send a text message to an AT&T number, you would use &lt;number&gt;@mms.att.net. Here's a list of other [mail-sms gateways][1].

Once you have your phone destination, all that's left is to add your message and send the mail.

<div id="code">
server.sendmail( <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;from&gt;</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">&lt;number&gt;@tmomail.net</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>, <span style="background-color: #333333"><font color="#ffffff">'</font></span><font color="#ffa0a0">Hello!</font><span style="background-color: #333333"><font color="#ffffff">'</font></span>&nbsp;)<br>
</div>

5 lines of code. Not bad :)

[1]: https://en.wikipedia.org/wiki/List_of_SMS_gateways
