"""Milestone Lab 2: Caesar Cipher
Given: A user input of text and a key shift value
Return: An encoded message using the Caesar Cipher. Give the option for the user to decode the message as well.
*Note: I do have some previous coding experience, so let me know if something is not explained well and I will create additional comments.
References: 
 1) https://www.asciitable.com/ for a reminder on ASCII values
 2) https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-functions/cheatsheet for a reminder on function basics
 3) Canvas videos for instructions on using .isupper() and .islower()
"""

#This is is the Caeser Cipher
#This top area contains all of the functions used to run the program
#The main function calls are at the bottom of the program.

#This function takes the required input from the user and transforms it into a form we will use later in the program.
def receive_message():
    plain_text_message = input('Please enter the message that you would like to be encoded. ') #Receive the message to be encoded from the user. It is saved in a variable as a string.
    key_shift = int(input('Please enter the desired key shift. This must be an interger. A positive interger will result in a \'right shift\' and a negative interger will result in a \'left shift\'.  ')) #Receive the key shift from the user. It is recast as an int for use later in mathematical operations.
    plain_text_list = list(plain_text_message) #Break the original message up into individual characters, each character is a separate index in the list. 
    return plain_text_list, key_shift #The list of characters from the message and the numerical key shift are the output of this function. Since there are two outputs, they must be assigned variables in this exact order.

#This function shifts the characters of the input message either left or right by the specified key shift.
def execute_shift(char, key_shift): #Takes inputs from encode_message() and receive_message(). The value of the input 'char' is a numerical value from 1 to 26, where the letter 'a' (or 'A') is 1, 'b' (or 'B') is 2, etc...
    encoded_char = char + key_shift #Shifts the numerical value of the character by the specified key shift.
    while encoded_char < 1 or encoded_char > 26: #This checks to make sure the new value is within the range of 1-26. This will run indefinitely until the new encoded character is within 1-26.
        if encoded_char < 1:
            encoded_char = encoded_char + 26 #if it is less than 1, it will add 26 to the new value
        elif encoded_char > 26:
            encoded_char = encoded_char - 26 #if it is over 26, it will subtract 26 from the new value
        else:
            pass
    return encoded_char #returns the shifted numerical value of the character

#This function takes the outputs of receive_message(), and (using the execute_shift() function), encodes the message and outputs a single string of the encoded message
def encode_message(plain_text_list, key_shift):
    new_char_list = [] #Empty list, needed later
    for char in plain_text_list: #loops through the list of unencoded characters
        if char.isupper(): #if the character is upper case, then
            new_char = execute_shift(ord(char)-64,key_shift) + 64 #take the character in ASCII decimal form, subtract 64 from that number to put it in the appropriate range of 1-26, then submit it to execute_shift()
            new_char_list.append(chr(new_char)) #Take the newly shifted (AKA encoded) character, put it back into the char data type, then append it to the new list of encoded characters.
        elif char.islower(): #does the same thing as the if statement, except for lower case characters.
            new_char = execute_shift(ord(char)-96,key_shift) + 96
            new_char_list.append(chr(new_char))
        else:
            new_char = char #anything else (like spaces or punctuation marks) are simply skipped and put directly into the encoded characters list.
            new_char_list.append(new_char) 
    encoded_message = ''.join(new_char_list) #turn the list of encoded characters into a string
    print(encoded_message) #print it out
    return encoded_message #return it for use later

#This function asks the user if they want to decode the message back to its original form or not. If they answer Yes, then the message is decoded and printed to the terminal
def decode_choice():
    while 1: #Starts an infinite loop. The user is forced to stay in this loop until they hit a 'break' statement
        decode_choice = input('Would you like to decode the message? Please type in \'Yes\' or \'No\'. ') #Ask the user if they want to decode
        if decode_choice == 'Yes': #If they say Yes, then:
            encode_message(encoded_message, key_shift*-1) #Run the same encode_message() function, but with the encoded message as the input (as opposed to the output) and the opposite of the key shift value.
            break #Exit infinite loop
        elif decode_choice == 'No': #If they say No, then:
            break #Exit infinite loop
        else: #If the user answers with anything other than exactly Yes or No, they are reminded to answer in that form and then returned to the top of the infinite while loop.
            print('Please enter \'Yes\' or \'No\' only. \n')

#Main Function Calls
plain_text_list, key_shift = receive_message() #The receive_message() function runs first and assigns the outputs to variables of the same names (for ease of use).
encoded_message = encode_message(plain_text_list, key_shift) #This function runs second and uses the outputs of receive_message() as inputs. The output of this function is the encoded message.
decode_choice() #This function runs third and, if the user chooses, they can decode the message. 