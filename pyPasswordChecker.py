#List of valid password characters, excludes capitals as later we can accomodate
#for them using the .lower() function
valid_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
 "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Password rule 1 - Must have more than 8 Characters
def pass_rule1(password): #Function takes password as input
    if (len(password) < 8): #if length of password string is less than 8 characters
        print("Password must be more than 8 Characters!")
        return False
        
    return True

#Password rule 2 - Must have only letters and numbers
def pass_rule2(password): #Function takes password as input
    for i in range(0, len(password)): #Loop for each character in password string
        valid_char = False #Reset valid_char to False every iteration

        for x in valid_chars: #Loop for each valid password character

            if (password[i].lower() == x): #If a password string character matches a valid character
                 valid_char = True #Set valid_char to True

        if (valid_char == False): #If valid_char is False, return False
            print("Password may not contain any special characters! Only numbers and letters.")
            return False
    
    return True #If function is here, means the password has only letters and numbers, return True

#Password rule 3 - Must have at least 2 numbers
def pass_rule3(password): #Function takes password as input
    num_count = 0 #variable to store how many numbers in password

    for i in range(0, len(password)): #Loop for each character in password string
        for x in range(9): #Loop 9 times to represent each digit
            if (password[i] == str(x+1)): #If character of password correlates to a number
                num_count += 1 #Add 1 to num_count

    if (num_count < 2): #If num_count is less than 2, return False
        print("You must use at least 2 numbers.")
        return False
        

    return True


print("Enter a string for a password:") #Ask user for password
password = input() #Store password in variable password

#If all password rules are passed
if (pass_rule1(password) == True and pass_rule2(password) == True and pass_rule3(password) == True):
    print("Valid Password") #Print valid password
else:
    print("Invalid Password") #If rules not passed, print invalid password

input("Enter any key to exit")