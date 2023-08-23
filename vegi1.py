# Write a Python program for the following requirements.
# Read a String statement from the command line
# Findout total number of characters present in the statement.
# Findout toal number of duplicate Characters in the statement
# Findout total number of words present in the statement
# Findout toal number of duplicate wordsin the statement
# Reverse the characters present in the statement.
# Reverse the words present in the statement.
# Form a new statement from the reversed words.
# Remove the duplicate characters from the latest statement.
# Print final latest String statement.

# Read a String statement from the command line

try:
    statement = input("Enter a string statement: ")

    # Findout total number of characters present in the statement.
    total_characters = len(statement)
    print("Total number of characters:", total_characters)

    # Findout toal number of duplicate Characters in the statement
    char_count = dict()
    for char in statement:
        char_count[char] = statement.count(char)

    total_duplicate_characters = sum(count for count in char_count.values() if count > 1)
    print("Total number of duplicate characters:", total_duplicate_characters)

    # Findout total number of words present in the statement
    words = statement.split()
    total_words = len(words)
    print("Total number of words:", total_words)

    # Findout toal number of duplicate words in the statement
    word_count = {}
    for word in words:
        word_count[word] = words.count(word)

    duplicate_words = sum(count for count in word_count.values() if count > 1)
    print("Total number of duplicate words:", duplicate_words)

    # Reverse the characters present in the statement
    reversed_characters = ""
    for char in statement:
        reversed_characters = char + reversed_characters
    print("Reversed characters:", reversed_characters)

    # Reverse the words present in the statement.

    reversed_words = ""
    word = ""
    for char in statement:
        if char != " ":
            word = char + word
        else:
            reversed_words = word + " " + reversed_words
            word = ""
    reversed_words = word + " " + reversed_words
    print("Reversed words:", reversed_words.strip())

    # Form a new statement from the reversed words.
    new_statement = reversed_words
    print("New statement from reversed words:", new_statement)

    # Remove the duplicate characters from the latest statement.
    result = ""
    for char in new_statement:
        if char not in result:
            result += char

    print("Statement with duplicate characters removed:", result)
    print("The final string statement is :",result)

except Exception as e:
    print("An error occurred:", e)
#



##  2nd     TASK        #####
"""Write a Python program to validate the entered email address if the email is valid then write into a file. Continue this operation until uses says No/exit. 
If user says Yes continue Validating emails and writing into file
If user says No then display all the email IDs from the file.
Note: Regex should be for validation"""



# ===============================================
import re

email_list = []
while True:

    user_input = input("Do you want to enter an email address? (Yes/No) :").lower()
    if user_input == 'no':
        fr=open("email_txt.txt","r")
        print(fr.read())

    elif user_input == 'yes':
        email = input("Enter the email address :").lower()
        pattern = r"^[A-Za-z0-9]+(|.)(|\d+|\w+)(|\w+)\@[a-z]+\.(in|com)"
        out = re.search(pattern,email)
        if out:
            fw = open(r"email_txt.txt","a")
            fw.write(out.group()+"\n")
            fw.close()
            fr=open(r"email_txt.txt", "r")
            print(fr.read())
# ===================================================================================

# ==============  3rd task        ==============

import re
from ping3 import ping

user_input = input("Do you want to enter an ip address? (Yes/No) :").lower()

if user_input == 'no':
    file_read = open("ip_address.txt", "r")
    print(file_read.read())

if user_input == 'yes':
    # it should be contain four octes
    input_ip_address = input("Enter the ip address, each octet should be within 0-255 :")
    # input_ip_address = "1.1.1.1"
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ip_address = re.match(pattern, input_ip_address)


    if ip_address:
        octets = input_ip_address.split(".")
        ip = [i for i in octets if int(i) <= 255]
        if len(ip) == 4:
            valid_ip = ip_address.group()
            response_time = ping(valid_ip)

            with open("ip_address.txt", "a") as fw:
                if response_time is not None:
                    fw.write(f"validate_ip: {valid_ip} (Response time: {response_time} ms)\n")
                else:
                    fw.write(f"invalidate_ip: {valid_ip} (Unreachable)\n")
    else:
        with open("ip_address.txt", "a") as fw:
            fw.write(f"invalid_ip_format: {input_ip_address}\n")






