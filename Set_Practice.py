#Q1.Write a Python program to declare and initialize a set and perform following operations on them.
s={10,20,30,40}
#To iterate over set elements by using for-each loop.
for a in s:
    print(a,end=" ")

#To add member(s) to a set.
s.add(50)
s.add(60)
print("\nAdded 50 and 60",s)

#To remove item(s) from a given set.

s.remove(50)
s.discard(70)
s.discard(60)
print("removed 50 and 60",s)

#To remove an item from a set if it is present in the set.
s.discard(100)
s.remove(40)
print("Removed 40",s)

#To print length (numbers of elements) in the set.
print("Length of string is:",len(s))

#To find the smallest and largest element from set

for num in s:
    sm=0
    lr=0
    for each in s:
        if num<each:
            sm+=1
            if sm==2:
                small=num
        elif num>each:
            lr+=1
            if lr==2:
                large=num

print("largest",large,"smallest",small)

#To remove all elements from set
s.clear()
print(s)
s={10,20,30}

#To check presence of an element in Set
print("is 10 in set s",(10 in s))

#2Q. Declare and initialize two sets and perform following operations on them.
set1={1,2,3,4,5}
set2={4,5,6,7,8}

#To create set difference.
set3=set1.difference(set2)
print("difference between set1 to set2:",set3)

#To create a symmetric difference.
set3=set1.symmetric_difference(set2)
print("Difference between set1 and set2 is:",set3)

#To print common elements between them
set3=set1.intersection(set2)
print("comman between set1 and set2:",set3)

#To obtain the values which are in set-A but not in set-B
print("values which are in set-A but not in set-B:",set1.difference(set2))

#To check whether they have any common element between them or not
print("Commen elements:",set1.intersection(set2))

#3. Consider following set of Strings and print the String which has largest length among them.
#{“Mahabaleshwar”, “Pune”, “Mumbai”, “Bangalore”, “Chennai”, “Vishakhapatnam”, “Kochi”}

set_city = {"Mahabaleshwar","Pune","Mumbai","Bangalore","Chennai","Vishakhapatnam","Kochi"}
lar="a"
for a in set_city:
    if len(a)>len(lar):
        lar=a

print("longest city name in:",set_city,"is:",lar)

#4.Consider above set of String and prepare a list containing only length of each city names.
#Expected output: [13, 4, 6, 9, 7, 14, 5]

set_city = {"Mahabaleshwar","Pune","Mumbai","Bangalore","Chennai","Vishakhapatnam","Kochi"}

len_city=[]
for a in set_city:
    l=len(a)
   # set_city.remove(a)
    len_city.append(l)

print("Citys",set_city,"length of  each city is",len_city)



#---------------------------------------------------------------------------------------------------------------------------
#Q1Given two Python sets, write a Python program to update the
#first set with items that exist only in the first set and not in the second set. (remove common elements)

set1 = {10, 20, 30, 40}
set2 = {20, 40, 50}

set1-=set2
print("removed commen element in set1:",set1)

#Q2 Write a Python program to remove items 10, 20, 30 from the following set at once.
#Given:
set1 = {10, 20, 30, 40, 50}

set1.remove(10)
set1.remove(20)
set1.remove(30)
print("removed items 10, 20, 30 from set1",set1)

#Q3 Check if two sets have any elements in common. If yes, display the common elements.

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set1&=set2
print("commen element in set1 and set2 is:",set1)

#Q4 Update set1 by adding items from set2, except common items.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1^=set2
print("Updated set1 by adding items from set2, except common items",set1)

#Q5 Remove items from set1 that are not common to both set1 and set2.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1&=set2
print(f"Removeed items from set1 that are not common to both set1 and set2:{set1}")

#Q6 Return a new set of identical items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1&set2
print("Returned a new set of identical items from two sets",set3)

#Q7 Write a Python program to return a new set with unique items from both sets by removing duplicates.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1|set2
print("returned a new set with unique items from both sets by removing duplicates.",set3)

