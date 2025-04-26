#Q.1) Write a Python program to create a lambda function that adds 15 
# to a given number passed in as an argument.

add15 =lambda x: x+15
a=add15(100)
print(a)
print(add15(50))

#Q.2) Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples: 
marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

"""def sort_subj():
    list1=[]
    for i in marks:
        list1.append(i[1])
    list1.sort()
    for i in range(0,4):
        if marks[i]==list1[i]"""

#Q.3) Write a Python program to filter a list of integers using Lambda.
#Original list of integers:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Even numbers from the said list:
#[2, 4, 6, 8, 10]
#Odd numbers from the said list:
#[1, 3, 5, 7, 9]

num_lst =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=lambda x: True if x%2==0 else False
odd=lambda x: True if x%2==1 else False
even_list=list(filter(even,num_lst))
odd_list=list(filter(odd,num_lst))
print(even_list)
print(odd_list)

#Q.4) Write a Python program to square and cube every number
# in a given list of integers using Lambda.
#Original list of integers:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Square every number of the said list:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Cube every number of the said list:
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr=lambda x:x**2
cub=lambda x:x**3
print(list(map(sqr,nums)),"\n",list(map(cub,nums)))

#Q.5) Write a Python program to extract year, month, date from given date,
# using Lambda.
#Sample Output:
#2020-01-15
#2020
#1
#15

#day = lambda x : x="\n" if x =="-" else x == x
"""def day(x):
    if x=="-":
        x="\n"
    return x
a="2020-01-15"
st1=list(map(day,list(a)))
st2=str(st1)
print(st2)"""

#Q.6) Write a Python program to create Fibonacci series up to n using Lambda.
#Fibonacci series upto 2:

"""[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]"""


#Q.7) Write a Python program to find the intersection of 
# two given arrays using Lambda.
"""Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
"""
set1=set([1, 2, 3, 5, 7, 8, 9, 10])
set2=set([1, 2, 4, 8, 9])
intr=lambda set1,set2: list(set1&set2)
a=intr(set1,set2)
a.sort()
print(a)

"""
Q.8) Write a Python program to count 
the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]"""
num_lst=[1, 2, 3, 5, 7, 8, 9, 10]
evn=lambda x: True if x%2==0 else False
odd=lambda x: True if x%2==1 else False

odd_co=len(list(filter(odd,num_lst)))
evn_co=len(list(filter(evn,num_lst)))

print(odd_co,evn_co)

"""Q.9) Write a Python program to rearrange positive 
and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]"""

a = [-1, 2, -3, 5, 7, 8, 9, -10]
a.sort
p1=lambda x: x<0
p2=lambda y: y>0
ans1=list(filter(p1,a))
ans1.reverse()
ans2=list(filter(p2,a))
ans2.extend(ans1)
print(ans2)


"""
Q.10) Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
Sample Input: [“ABHAY“, “AMIT“,“MONDAY“,“THURSDAY“,“SAM“,“VISHWAMBHAR“,“JOSHI“,“KULDEEP“]
Sample Output:
MONDAY
THURSDAY
VISHWAMBHAR
KULDEEP
"""
names = ["ABHAY", "AMIT","MONDAY","THURSDAY","SAM","VISHWAMBHAR","JOSHI","KULDEEP"]
lm6=lambda name: len(name)>=6 
ans=list(filter(lm6,names))
print(ans)


"""
Q.11) Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""
eans=lambda x,y: x+y
f=[1, 2, 3]
s=[4, 5, 6]
ans=list(map(eans,f,s))
print(ans)


"""
Q.12) Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen are:
[19, 65, 57, 39, 152, 190]
"""

ls=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
t_or_n= lambda x: x%13==0 or x%19==0
ans=list(filter(t_or_n,ls))
print(ans)


"""
Q.13) Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""
ls = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
pal = list(filter(lambda x: x==x[::-1],ls))
print(pal)