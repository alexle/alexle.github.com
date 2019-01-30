No problem Richard! I'm glad you were able to find the five-line SMS script useful.

I hadn't given much thought before on sending images via SMS, but you have me curious now! I did some experimentation and was able to come up with a solution.

Like you mentioned earlier, it involves MIME. This involves creating a MIME base object, which allows us to attach text and images. The code is below:

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

# Set up MIME base object and attach text
msg = MIMEMultipart()
msg.attach( MIMEText( <text>, 'plain' ) )

fp = open( <image>, 'rb' )

# Set up MIME image object and attach to base object
msg_img = MIMEImage( fp.read( ) )
msg.attach( msg_img )

fp.close( )

server.sendmail( <from>, <destination>, msg.as_string( ) )

I tested the code and was able to receive both SMS text and images (only used small ones). I uploaded my script to https://gist.github.com/alexle/6576366 for reference. Hope it works for you, have fun!
