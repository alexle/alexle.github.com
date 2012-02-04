How To Send A SMS Message With Python (easy way)
05-05-2011

Python is a scripting programming language. It's easy to read, has great libraries, is documented very well, and is extremely versatile and powerful. It's my favorite language to work with and I have yet to come across a problem that it could not solve.

Can it send text messages? You betcha!

You'll be using the SMTP (Simple Mail Transfer Protocol) library. It's the most common protocol for sending mail and its communication is done using TCP.

> import smtplib

Next, establish a secure session with gmail's outgoing SMTP server using your gmail account. A TLS or SSL connection must be used; the example below uses STARTTLS which is port 587.

> server = smtplib.SMTP( "smtp.gmail.com", 587 )<br>
> server.starttls()<br>
> server.login( '&lt;gmail_address&gt;', '&lt;gmail_password&gt;' )

Now you're set up to send email. You will send a text message by taking advantage of each mobile carrier's email to SMS gateway!

For example, to send a text message to a t-mobile number, you would use &lt;number&gt;@tmomail.net. To send a text message to an AT&T number, you would use &lt;number&gt;@mms.att.net.

Once you have your phone destination, all that's left is to add your message and send the mail.

> server.sendmail( '&lt;from&gt;', '&lt;number&gt;@tmomail.net', '&lt;msg&gt;' )

5 lines of code. Not bad :)

