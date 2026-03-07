# basic program to count the number of alphabetic characters and special characters in a sentence. 
# because  with out using any function we can do this but here we are using the isalpha() and isalnum() method to count the number of alphabetic characters and special characters in a sentence.


# Wap to find out numbers of alphabetic characters in a sentence
sentence = input("Enter a sentence: ")
count = 0
for char in sentence:
    if char.isalpha():
        count += 1  
print("Number of alphabetic characters:", count)


# Wap to find out numbers of special characters in a sentence
sentence = input("Enter a sentence: ")
special_count = 0
for char in sentence:
    if not char.isalnum():
        special_count += 1
print("Number of special characters:", special_count)


#simple methon in python  to find the any case of a string

# use isupper()  to check if a string is in uppercase or not

# isupper case
sen = "Aaryan"
print(sen.isupper())  


# use istitle() to check if a string is in title case or not what is title case?  Title case means the first letter of each word is capitalized and the rest are lowercase. For example, "Hello World" is in title case, while "hello world" and "HELLO WORLD" are not.
#  
# istitle  case
sen = "Aaryan"
print(sen.istitle())  


# use islower() to check if a string is in lowercase or not

# upper  case
sen = "Aaryan"
print(sen.upper()) 



# use lower() to convert a string to lowercase

# lower  case
sen = "Aaryan"
print(sen.lower()) 


'''output:
Enter a sentence: Hello World! 123
Number of alphabetic characters: 10
'''


'''output:
Enter a sentence: Hello World! 123
Number of special characters: 2'''





'''output:
Enter a sentence: Hello World! 123
Number of alphabetic characters: 10
'''


'''output:
False'''


'''output:
AARYAN'''

'''output:
aaryan
'''