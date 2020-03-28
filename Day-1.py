>>> print("hello world")
O/P -> hello world
>>> a=5
>>> type(a)
O/P -> <class 'int'>

>>> dir()
O/P -> ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']

>>> import random
['A', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'random']


>>> import pylearn
>>> from pylearn import fun1


>>> fun1()
"""THIS FUNCTION CALL WILL GIVE ERROR AS FUNCTION IS NOT IN THE LOCAL NAMESPACE"""
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    fun1()
NameError: name 'fun1' is not defined


"""CORRECT FUNCTION CALL"""
>>> pylearn.fun1()


>>> import pylearn
hello world

pylearn.fun()
Hello World in funtion



 >>>for i in range(10):
	print(i)

>>> for i in range(5,20,2): [start,stop,step]
	print(i)

for i in range(19,4,-2):
	print(i)

>>>a=[1,2,'sameem',[1,2]]

>>> for element in a:
	print(element)

"""LIST INITIALIZATION"""
>>> lst=[]
>>> lst2=list()
>>> type(lst)
<class 'list'>
>>> type(lst2)
<class 'list'>
>>> a[2]
'sameem'
>>> a[3][1]
2

st="sameem"
>>> for i in st:
	print(i)


 >>>for i in st:
	print(i,end=" ")

>>> while a<31:
	print(a)
	a+=1


>>> def isprime(n):
	f=2
	while f*f <= n:
		if n%f==0:
			return False
		f+=1
	return True

>>> a = input("Enter a number: ")
Enter a number: 58
>>> a = input()
34
>>> a
'34'
>>> isprime(3)
True
>>> for i in range(1,100):
	if isprime(i):
		print(i)

>>> def primes():
	a = int(input("Upto which number: "))
	for i in range(1,a):
		if  isprime(i):
			print(i,end='  ')

"""the input function reads string data by default"""
>>> a=input()
23
>>> type(a)
<class 'str'>
"""We use int() to convert it to integer"""
>>> a= int(input())
34
>>> type(a)
<class 'int'>
