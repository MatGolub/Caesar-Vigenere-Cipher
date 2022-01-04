"""Milestone Lab 2: Vigenère Cipher
Given: A user input of text and a user's key phrase
Return: An encoded message using the Vigenère Cipher. 
*Note: I do have some previous coding experience, so let me know if something is not explained well and I will create additional comments.
References: 
 1) https://www.asciitable.com/ for a reminder on ASCII values
 2) https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-functions/cheatsheet for a reminder on function basics
 3) Canvas videos for instructions on using .isupper() and .islower()
"""

#This is a fully functioning Vigenère Cipher
#This top area contains all of the functions used to run the program
#The main function calls are at the bottom of the program.

#This function takes the required input from the user and transforms it into a form we will use later in the program.
def receive_message():
    plain_text_message = input('Please enter the message that you would like to be encoded. ') #Receive the message to be encoded from the user. It is saved in a variable as a string.
    key = input('Please enter the desired key. This must be a single string of characters with no spaces. ') #Receive the key shift from the user. 
    plain_text_list = list(plain_text_message) #Break the original message up into individual characters, each character is a separate index in the list. 
    key_list = list(key)
    return plain_text_list, key_list #The list of characters from the message and the numerical key shift are the output of this function. Since there are two outputs, they must be assigned variables in this exact order.

#This function shifts the characters of the input message either left or right by the specified key shift.
def execute_shift(char, key): #Takes inputs from encode_message() and receive_message(). The value of the input 'char' is a numerical value from 1 to 26, where the letter 'a' (or 'A') is 1, 'b' (or 'B') is 2, etc...
    encoded_char = char + key #Shifts the numerical value of the character by the specified key shift.
    while encoded_char < 1 or encoded_char > 26: #This checks to make sure the new value is within the range of 1-26. This will run indefinitely until the new encoded character is within 1-26.
        if encoded_char < 1:
            encoded_char = encoded_char + 26 #if it is less than 1, it will add 26 to the new value
        elif encoded_char > 26:
            encoded_char = encoded_char - 26 #if it is over 26, it will subtract 26 from the new value
        else:
            pass
    return encoded_char #returns the shifted numerical value of the character

#This function takes the outputs of receive_message(), and (using the execute_shift() function), encodes the message and outputs a single string of the encoded message
def encode_message(plain_text_list, key_list):
    new_char_list = [] #Empty list, needed later
    i = 0 #Start a counter for the index of the key
    for char in plain_text_list: #loops through the list of unencoded characters
        if char.isupper() and key[i].isupper(): #if the character is upper case, then
            new_char = execute_shift(ord(char)-64, ord(key_list[i])-65) + 64 #Converts the character (or key) to ASCII, then subtracts 64 (or 65) to convert the letter to an interger in the range of 1-26 (or 0-25). These values are submitted to the execute_shift() function.
            new_char_list.append(chr(new_char)) #Take the newly shifted (AKA encoded) character, put it back into the char data type, then append it to the new list of encoded characters.
            i = i+1 #Increment the counter by 1 after the letter in the key is "used"
        elif char.islower() and key[i].islower(): #does the same thing as the if statement, except for lower case characters and keys.
            new_char = execute_shift(ord(char)-96, ord(key_list[i])-97) + 96
            new_char_list.append(chr(new_char))
            i = i+1 #Increment the counter by 1 after the letter in the key is "used"
        elif char.isupper and key[i].islower(): #does the same thing as the if statement, except for upper case characters and lower case keys.
            new_char = execute_shift(ord(char)-64, ord(key_list[i])-97) + 64
            new_char_list.append(chr(new_char))
            i = i+1 #Increment the counter by 1 after the letter in the key is "used"
        elif char.islower() and key[i].isupper(): #does the same thing as the if statement, except for lower case characters and upper case keys.
            new_char = execute_shift(ord(char)-96, ord(key_list[i])-65) + 96
            new_char_list.append(chr(new_char))
            i = i+1 #Increment the counter by 1 after the letter in the key is "used"
        else:
            new_char = char #anything else (like spaces or punctuation marks) are simply skipped and put directly into the encoded characters list.
            new_char_list.append(new_char) #Note how i is not incremented here in the 'else' statement.
        if i == len(key): #This if statement resets the counter i back to zero once it exceeds the length of the key, essentially starting over again to encode additional characters in the message.
            i = 0
    encoded_message = ''.join(new_char_list) #turn the list of encoded characters into a string
    print(encoded_message) #print it out
    return encoded_message #return it for use later


#Main Function Calls
plain_text_list, key = receive_message() #The receive_message() function runs first and assigns the outputs to variables of the same names (for ease of use).
encoded_message = encode_message(plain_text_list, key) #This function runs second and uses the outputs of receive_message() as inputs. The output of this function is the encoded message.