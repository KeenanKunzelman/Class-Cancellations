
def DoIHaveClass(teacher):

 
    if teacher in html:
        from twilio.rest import TwilioRestClient
        
        ACCOUNT_SID = "AC3b62660b9e7f012458402a5c8c204f76"
        AUTH_TOKEN = "8059ac4c740fd09e35f7d0475cb8401e"
        
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        
        client.messages.create(
          to="+18454643900", 
          from_="+18457634350", 
          body="You have a cancelled class go to https://www.sunydutchess.edu/classcancellations/ for more information ", )
    else:
        print 'you have class' 
import urllib2

response = urllib2.urlopen('https://www.sunydutchess.edu/classcancellations/')
html= response.read()


CIS212 = "Francis J. Whittle"
CIS213 = "Carson Lee McCullers"
CIS117 = "Stephen Leggett"

DoIHaveClass(CIS117) 
DoIHaveClass(CIS212)
DoIHaveClass(CIS213)


