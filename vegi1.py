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
# statement = input("Enter a string statement: ")
statement = "satya sai sai"
# Findout total number of characters present in the statement.
total_characters = len(statement)
print("Total number of characters:", total_characters)

# Findout toal number of duplicate Characters in the statement
char_count = dict()
for char in statement:
    char_count[char] =statement.count(char)

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
reversed_characters = statement[::-1]
print("Reversed characters:", reversed_characters)

# Reverse the words present in the statement.
reversed_words = " ".join(word[::-1] for word in words)
print("Reversed words:", reversed_words)

# Form a new statement from the reversed words.
new_statement = reversed_words
print("New statement from reversed words:", new_statement)

# Remove the duplicate characters from the latest statement.

result = ""

for char in new_statement:
    if char not in result:
        result += char

print("Statement with duplicate characters removed:", result)


# removed_duplicates = statement.split()
# unique_words = list(set(words))
#
# final_string = " ".join(unique_words)
# print("String with duplicate words removed:", final_string)