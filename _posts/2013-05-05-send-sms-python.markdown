---
layout: post
title: "How To Send A SMS Message With Python (easy way)"
date: 2013-05-05
tags: programming
---

[Python][2] is a high-level programming language. It's easy to read, has great libraries, and is well documented. On top of it, it's extremely versatile and powerful. Python is my favorite language to work with and I've yet to come across a problem it could not solve.

Can it send text messages? You betcha! Here are the steps to send one easily:

## 1. Load SMTP Module ##
SMTP (simple mail transfer protocol) is a common protocol for sending e-mail between mail servers. This is what will be used to send the text message. Fortunately, Python includes a nice library of basic SMTP functions in *smtplib*.

``` python
import smtblib
```

## 2. Connect to Gmail SMTP Server ##
Establish a secure session with Gmail's outgoing SMTP server. A connection can be made with either TLS or SSL.

In this example, the STARTTLS connection is used (port 587). The session is complete with the credentials of a valid Gmail account.

``` python
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<gmail_address>', '<gmail_password>' )
```

## 3. Select Phone Destination ##
Now the program is ready to send e-mail. The text message will be sent by taking advantage of each mobile carrier's **e-mail to SMS gateway**.

For example, to send a text message to a T-Mobile number, you would use &lt;number&gt;@tmomail.net. To send a text message to an AT&T number, you would use &lt;number&gt;@mms.att.net. Here is a list of other [mail-sms gateways][1].

## 4. Send The Message ##
Once the phone destination has been selected, all that's left is to add the message and send the mail.

``` python
server.sendmail( '<from>', '<number>@tmomail.net', 'Hello!' )
```

5 lines of code. Not bad!

## Reader Follow-Up (12-17-2016) ##

Here's an email I received email from a reader:

> Hi Alex,

> I was working on a project where I need to use python to send messages to a phone. I read your blog and found that it's extremely simple to do this with the short message gateway.

> However, I've met a problem with this method. Sometimes when I send a message my phone instantly receives it. Other times it will take longer to receive a message. I wonder if there is any way to make this more stable.

Hello reader!

Unfortunately, using e-mail to SMS gateway has some limitations. Here are some that I know of, including the "extended period to receive" issue you mentioned:

1. You have no control over your text format. Each carrier seems to have its own formatting (email address, subject, names, etc..)

2. You have no delivery confirmation.

3. While delivery is mostly consistent, there is increased and varying latency when sending SMS through email gateway. This is because the email hub is responsible for processing ALL email messages for all mobile devices on the network. If the queue is low, the SMS is distributed quickly. If the queue is high, the email/SMS is held for later distribution, thus causing delay in when the message is received.

If you want to send consistent, customized text messages, the best option is to use a third-party service such as Twilio. Hope that answers your question!

[1]: https://en.wikipedia.org/wiki/List_of_SMS_gateways
[2]: http://www.python.org/
