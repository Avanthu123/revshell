#This line imports the os module,which provides a way to interact with the operating system,allowing you to execute commands.
import os

#Ask the hostname to user
hostname = input("Enter the hostname: ")

#This line constructs a Ping command using the os.system function.
# It pings the specified hostname once (-c 1 option) and captures the response code. 
# The os.system function returns the exit code of the executed command. 
# In the context of the Ping command, a response code of 0 typically indicates a successful ping (the host is reachable), while a non-zero code indicates an unsuccessful ping (the host is not reachable).
response = os.system("ping -c 1 "+ hostname)

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname,'is down!')