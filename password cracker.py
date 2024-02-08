#These lines import the randint function from the random module and the os module. 
# randint will be used to generate random indices for selecting characters from the password list, and os is used to clear the console screen later in the code.
from random import *
import os

#The user is prompted to input a password. This password will be the target for the simulated brute-force attack.
u_pwd = input("Enter a password: ")

#A list named pwd is defined, containing lowercase letters and digits (0-9). 
# This list represents the character set from which the simulated attacker will guess the password.
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
       'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

#A while loop is initiated, which continues until the guessed password (pw) matches the user-input password (u_pwd).
pw = ""
while(pw!=u_pwd):
    
    #Within the loop, the code generates a random guess for each character in the user-input password. 
    # The random guess is selected from the predefined character set (pwd). 
    # The guessed character is then prepended to the current guess (pw), forming a cumulative guess.
    #The print(pw) statement displays the current guess on the console.
    # The os.system("cls") line clears the console screen to simulate the appearance of cracking the password.
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        pw = str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password...Please Wait!")
        os.system("cls")
        
print("Your Password is: ",pw)