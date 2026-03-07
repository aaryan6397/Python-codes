# Q6: Check if two strings are anagrams of each other
# Input: "listen", "silent"
# Output: True (they are anagrams)



# Define the two strings
str1 = "listen"
str2 = "silent"

# Convert both strings to lowercase and sort the characters
sorted_str1 = sorted(str1.lower())
sorted_str2 = sorted(str2.lower())

if sorted_str1 == sorted_str2:
    print(f'"{str1}" and "{str2}" are Anagrams')
else:
    print(f'"{str1}" and "{str2}" are NOT Anagrams')

# Another test
str3 = "hello"
str4 = "world"
if sorted(str3.lower()) == sorted(str4.lower()):
    
    print(f'"{str3}" and "{str4}" are Anagrams')

else:
    
    print(f'"{str3}" and "{str4}" are NOT Anagrams')

# Output:
# "listen" and "silent" are Anagrams
# "hello" and "world" are NOT Anagrams