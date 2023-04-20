#write a python function that returns the Nth Fibonacci number
def fibonacci_sequence(n):
    if n<=1:
        return n
    else:    
        return (fibonacci_sequence(n-1)+fibonacci_sequence(n-2))


#Write a Python function that takes a list of numbers and 
#returns the sum of all even numbers in the list
def even_numbers(nums):
    addition=0
    for num in nums:
        if num%2 == 0:
            addition+=nums
            return addition

#Write a Python function that takes two strings and 
#returns True if they are an anagram, False otherwise.
def statements(string1,string2):
    string1=string1.lower()
    string2=string2.lower()
    if (len(string1)==len(string2)):
        sorted_string1=sorted(string1)
        sorted_string2=sorted(string2)
        if (sorted_string1==sorted_string2):
            return(True)
        else:(False)    

 #Write a Python function that takes a string and 
 |#returns the reverse of the string.
def words(string):
    return string[::-1]


#Write a Python function that takes a list of strings and 
#returns the longest string in the list.
def longer_name(names):
    return max(names,key=len)


#Write a Python function that takes a list of integers and 
#returns the second largest number in the list.
def second_largest(numbs):
    numbs.sort()
    return numbs[len(numbs)-2]


#Write a Python function that takes a string and 
#returns True if the string is a palindrome, False otherwise.
def palindrome(str):
    if str[0]==str[-1] and str[1]==str[-2]
     return (True)
    else:return(False) 



    

       


        
