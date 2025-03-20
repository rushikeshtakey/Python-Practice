#Q1  Reverse a given list
aList = [100, 200, 300, 400, 500]

aList.reverse()
print(aList)

"""Exercise 2: Given a Python list, find value 20 in the list, 
and if it is present, replace it with 200. (Only update the first occurrence of a value.)
Given
list1 = [5, 10, 15, 20, 25, 50, 20]"""
list1 = [5, 10, 15, 20, 25, 50, 20]
a=list1.index(20)
list1.remove(20)
list1.insert(a,200)
print(list1)



'''Exercise 3: Concatenate two lists index-wise.
Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:
list3 = ['My', 'name', 'is', 'Kelly']'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
i=0
list3=[]
for a in range(0,4):
    list3.append(list1[i]+list2[i])
    i+=1
print(list3)


'''Exercise 4: Given a Python list of numbers. Turn every item of a list into its square
Given:
aList = [1, 2, 3, 4, 5, 6, 7]
Expected output:
aList = [1, 4, 9, 16, 25, 36, 49]'''

aList = [1, 2, 3, 4, 5, 6, 7]
i=0
while i<7:
    aList[i]=aList[i]**2
    i+=1
print(aList)
    
'''Exercise 5: Concatenate two lists in the following order
Given:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:
list3 = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3=[]
for a in  list1:
    for b in list2:
        list3.append(a+b)
    
print(list3)

"""Exercise 6: Given a two Python list. Iterate both lists simultaneously
 such that list1 should display item in original order and list2 in reverse order.
Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400
20 300
30 200
40 100"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
i=0
for a in list1:
    print(a,list2[i])
    i+=1


"""Exercise 7: Remove empty strings from the list of strings
Given:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:
list1 = ["Mike", "Emma", "Kelly", "Brad"]"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
b=list1.count("")
i=0
while i<b:
    list1.remove("")
    i+=1
print(list1)

"""Exercise 8: Add item 7000 after 6000 in the following Python List
Given:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)


'''Exercise 9: Given a nested list extend it by adding the sub list ["h", "i", "j"] 
in such a way that it will look like the following list
Given List:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

add = ["h", "i", "j"]
list1[2][1][2].extend(add)
print(list1)

"""Exercise 12: Given a Python list, remove all occurrence of 20 from the list.
Given:
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
[5, 15, 25, 50]"""

list1 = [5, 20, 15, 20, 25, 50, 20]

b=list1.count(20)
i=0
while i<b:
    list1.remove(20) 
    i+=1
print(list1)


"""Exercise 13: Write a Python program to count the number of 
strings where the string length is 3 or more and the first and last character
are same from a given list of strings. Go to the editor
Given:
list1 = ['abc', 'xyz', 'aba', '1221', ‘xyyxz’, ‘AA’]
Expected output: 2"""

list1 = ['abc', 'xyz', 'aba', '1221','xyyxz','AA']
count=0
for a in list1:
    if len(a)>=3 and  a[0]==a[-1]:
        count+=1

print(count)              
