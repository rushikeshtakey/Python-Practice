"""
# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
"""
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
map_result = list(map(lambda x: round(x**2,3),my_floats))
print(map_result)

"""
# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
"""

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filter_result= list(filter(lambda x: len(x)<=7,my_names))
print(filter_result)

"""
# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
"""
from functools import reduce
my_numbers = [4, 6, 9, 23, 5]
reduce_result=reduce(lambda x,y: x*y , my_numbers)
print(reduce_result)

"""
1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
"""
ls = [1,2,3,4,5,6,7,8]
trip = list(map(lambda x: x*3,ls))
print(trip)

"""
2. Write a Python program to add three given lists using Python map and lambda.
"""

ls1=[1,2,3,4]
ls2=[1,2,3,4]
ls3=[1,2,3,4]
addls=list(map(lambda x,y,z: x+y+z,ls1,ls2,ls3))
print(addls)

"""
3. Write a Python program to listify the list of given strings individually using Python map.
"""
ls= ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
listify= list(map(lambda x: list(x),ls))
print(listify)

"""
4. Write a Python program to create a list containing the power of said number in bases raised to the
corresponding number in the index using Python map.
"""

ls=[4,7,3,6]
powe=list(map(lambda x: x**ls.index(x),ls))
print(powe)

"""
5. Write a Python program to square the elements of a list using the map( ) function.
"""
ls=[4,7,3,6]
sqr=list(map(lambda x: x**2,ls))
print(sqr)

"""
6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate
duplicate letters from a given sequence. Use the map( ) function.
"""
mobile = "MotoRola"
sm=set(mobile)
low= list(map(lambda x: x.lower(),sm))
upp= list(map(lambda x: x.upper(),sm))
print(low)
print(upp)

"""
7. Write a Python program to add two given lists and find the difference between them. Use the map( )
function.

"""

ls=[4,6,9,7]
ls1=[2,3,8,5]
ad=list(map(lambda x,y: x+y,ls,ls1))
diff=list(map(lambda x,y: y-x,ls,ls1))
print(ad,diff)

"""
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
"""

ls=[5,4,3,2,1]
tp=(9,8,7,6,5)
ls1=list(map(lambda x: str(x),ls))
ls2=list(map(lambda x: str(x),tp))
ls1.extend(ls2)
print(ls1)

"""
9. Write a Python program to create a new list taking specific elements from a tuple and convert a string
value to an integer.
"""
tp=("56","34","ajay","chetan","pawan","95","4","ravi")
ls = list(filter(lambda x: x.isdigit(),tp))
ls1= list(map(int,ls))
print(ls1)

"""
10. Write a Python program to compute the square of the first 
N Fibonacci numbers, using the map
function and generate a list of the numbers.
"""
t1=0
t2=1
ls=[0,1]
n=1
while(n<=8):
    z= t1+t2
    ls.append(z)
    t1=t2
    t2=z
    n+=1
print(ls)
sqr=list(map(lambda x: x**2,ls))
print(sqr)
