import os
#This line creates a list called ip_list containing three IP addresses. 
# You can modify this list to include the specific IP addresses you want to check.
ip_list = ["8.8.8.8","8.8.4.4","192.168.1.1"]

#This for loop iterates through each IP address in the ip_list.
for ip in ip_list:
    
    #Within the loop, the code uses the os.popen function to execute the Ping command for each IP address. 
    # The f"ping {ip}" constructs the command dynamically, where {ip} is replaced with the current IP address in the iteration. 
    # The .read() method reads the output of the command.
    response = os.popen(f"ping {ip}").read()
    
    #After executing the Ping command, the script checks the response to determine if the ping was successful. 
    # The condition if "Received = 4" in response checks if the string "Received = 4" is present in the output, which typically indicates a successful ping (four packets received). 
    # If the condition is true, it prints a message stating that the IP address is up; otherwise, it prints a message indicating that the IP address is down.
    if "Received = 4" in response:
        print(f"UP {ip} ping successful")
    else:
        print(f"DOWN {ip} ping unsuccessful")