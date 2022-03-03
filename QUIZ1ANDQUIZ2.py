#Problem 1
print("This is problem one OUTPUT")
# Given the string:
s = 'django'
print("Using indexing to print out the following:\n",s[0],'\n',s[5],'\n',s[1:4],'\n',s[4:6])
#reversing the string
print("Reversing the string BONUS")
print(s[::-1])

#Problem 2
print("\nThis is Problem two OUTPUT")
# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'
print(l)

# Problem 3
print("\nThis is Problem Three OUTPUT")
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

# Problem 4
print("\nThis proble four OUTPUT")
# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
def unique(mylist):
    list_set = set(mylist)
    unique_list = (list(list_set))
    for x in unique_list:
        print (x),
unique(mylist)

# Problem 5
print("\nThis proble five OUTPUT")
# You are given two variables:
age = 4
name = "Sammy"
# Use print formatting to print the following string:
#"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is "+name+"and he " +str(age)+ " is years old")


#### Quiz 1 - Part 2: FUNCTION ######
#Problem 1
# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

print("\nQIUZ 2::::")
def arrayCheck(nums):
  returnvalue = False
  for num in range(len(nums)+2):
    if nums[num:num+3] == [1, 2, 3]:
      returnvalue = True
  return returnvalue

print("First List Checking")
print(arrayCheck(([1, 1, 2, 3, 1])))
print("Second List Checking")
print(arrayCheck(([1, 1, 2, 4, 1])))
print("Third List Checking")
print(arrayCheck([1, 1, 2, 1, 2, 3]))


# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".
#Problem 2
# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

print("\nQUIZ 2:: PROBLEM 2")
def stringBits(str):
    returnvalue2 = ""
    for i in range(len(str)):
        if i % 2 ==0:
            returnvalue2 = returnvalue2 + str[i]
    return  returnvalue2

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
#Problem 3

print("\nQUIZ 2:: PROBLEM 4")
def end_other(a,b):
    a=a.lower()
    b=b.lower()
    return(b.endswith(a)or a.endswith(b))
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

print("\nQUIZ 2:: PROBLEM 3")
def doubleChar(str):
    result=''
    for i in str:
        result+=i
        result+=i
    return result
print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

#Problem 5

print("\nQUIZ 2:: PROBLEM 5")
def no_teen_sum(a,b,c):
    return fix_teem(a) + fix_teem(b) + fix_teem(c)
def fix_teem(n):
        if n>=13 and n<=19:
            if n==15 or n==16:
                return n
            else:
                return 0
        else:
            return n
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

print("\nQUIZ 2:: PROBLEM 6")

def count_evens(nums):
    result=0
    for i in nums:
        if i % 2 == 0:
            result+=1
    return result

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))