import os
import sys
import socket
from termcolor import cprint
 
cprint("any misuse of the THE DEVILS DEMONS is not responsible for these little idiots", "red")
cprint('i do not care what YOU do with this tool but YOU are reposible for YOU so if you wanna continue and sign your life away just say yes\n', "red")
 
agreement = input('Agree to continue: ')
 
if agreement.lower() == "yes":
    pass
elif agreement.lower() == "no":
    cprint("\nExiting script.", "red")
    sys.exit()
else:
    cprint("\nNot an option. Exiting script.", "cyan")
    sys.exit()
 
 
def clearScr():
    os.system('clear')
 
 
 
 
 
clearScr()
 
 
class tools:
    def __init__(self):
        pass
 
    def yourIP(self):
        import socket
        self.hostname = socket.gethostname()    
        self.IPAddr = socket.gethostbyname(self.hostname)
        cprint("\nfind your ip address with ip finder made by http.zygote" , "red")
        cprint("\nYour Computer Name is: " + self.hostname)    
        cprint("Your Computer IP Address is: " + self.IPAddr , "red")
 
    def dox_template(self):
        cprint("welcome to zygotes dox helper here is your doxing template" , "red")
        cprint("made by the one and only instagram @https.zygote" , "red")
        #about
        self.Fullname = input("Enter Full name: ")
        self.Address = input("enter home address: ")
        self.City = input("Enter city: ")
        self.Zipcode = input("Enter zipcode: ")
        self.State = input("Enter State: ")
        self.Country = input("Enter country: ")
        #emails
        self.Email = input("Enter Emails: ")
        #ip info
        self.IP = input("enter ip address: ")
 
        #-----Print -----
        print("about")
        print (self.Fullname + ", " + self.Address + ", " + self.City + ", " + self.Zipcode + ", " + self.State + ", " + ", " + self.Country)
 
        #----- E-Mails -----
        print("emails")
        print(self.Email + " ")
 
        #----- ISP Information -----
        print("ip info")
        print(self.IP + " ")
 
 
    def anon_mailer(self):
        import requests
        def prGreen(skk):
            print("\033[92m {}\033[00m" .format(skk))
        def prRed(skk):
            print("\033[91m {}\033[00m" .format(skk))
        def prYellow(skk):
            print("\033[93m {}\033[00m" .format(skk))
        def prLightPurple(skk):
            print("\033[94m {}\033[00m" .format(skk))
        def prPurple(skk):
            print("\033[95m {}\033[00m" .format(skk))
        def prCyan(skk):
            print("\033[96m {}\033[00m" .format(skk))
        def prLightGray(skk):
            print("\033[97m {}\033[00m" .format(skk))
        def prBlack(skk):
            print("\033[98m {}\033[00m" .format(skk))
 
        prRed("\nAnonymous Email by anonymouse.org")
        prCyan("coded by http.zygote")
        self.to = input('to: ')
        self.subject = input('insert subject: ')
        self.message = input('insert message: ')
 
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        self.sess = requests.Session()
        self.data = {'to': self.to,
                     'subject': self.subject,
                     'text': self.message}
 
        self.headers = {'Host': 'anonymouse.org',
                        'User-Agent': self.user_agent,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Referer': 'http://anonymouse.org/anonemail.html',
                        'Connection': 'close',
                        'Upgrade-Insecure-Requests':'1',
                        'Content-Type':'application/x-www-form-urlencoded'}
 
        self.email_req = self.sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', data=self.data, headers=self.headers)
       
 
 
        if 'The e-mail has been sent' in self.email_req.text:
            prRed("[+] EMAIL HAS BEEN SENT")
            prCyan("[+] this anonymous email will have a 12 hour delay for more privacy")

    def host_to_ip(self):
        self.host = input("ENTER A HOST TO GET IP: ")
        self.ip = socket.gethostbyname(self.host)
        print("   %s has the IP of %s" % (host, ip))
        self.response = input(continuePrompt)
        
tools = tools()
d3m0nPrompt = "d3m0n ~# "
 
 
print('''
     {1}--yourip
     {2}--anon_mailer
     {3}--dox_template
     {4}--host_to_ip
 
     {99}--exit
   ''')
 
choice = input(d3m0nPrompt)
 
if choice == "1":
    tools.yourIP()
elif choice == "2":
    tools.anon_mailer()
elif choice == "3":
    tools.dox_template()
elif choice == "4":
    tools.host_to_ip()
elif choice == "99":
    sys.exit()
