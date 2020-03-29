Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> import pylearn
hello world
>>> fun()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fun()
NameError: name 'fun' is not defined
>>> pylearn.fun()
Hello World in funtion
>>> from pylearn import fun
>>> from pylearn import *
>>> fun()
Hello World in funtion
>>> a= [1,3,4,6,8]
>>> l2=[1,2,'edwin',[1,2]]
>>> lst=[]
>>> a=list()
>>> type(lst)
<class 'list'>
>>> type(a)
<class 'list'>
>>> a= [1,3,4,6,8]
>>> for i in a:
	print(a)

	
[1, 3, 4, 6, 8]
[1, 3, 4, 6, 8]
[1, 3, 4, 6, 8]
[1, 3, 4, 6, 8]
[1, 3, 4, 6, 8]
>>> for i in a:
	print(1)

	
1
1
1
1
1
>>> for i in a:
	print(i)

	
1
3
4
6
8
>>> for i in range(1,6):
	print(i)

	
1
2
3
4
5
>>> for i in range(1,6):
	print(2*i)

	
2
4
6
8
10
>>> for i in range(1,6):
print(2*i)
SyntaxError: expected an indented block
>>> def isprime(n):
	for i in range(0,n):
		if n%f == 0:
			return False
	return True

>>> isprime(3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    isprime(3)
  File "<pyshell#32>", line 3, in isprime
    if n%f == 0:
NameError: name 'f' is not defined
>>> def isprime(n):
	for i in range(0,n):
		if i%n == 0:
			return False
	return True

>>> isprime(3)
False
>>> def isprime(n):
	for i in range(0,n):
		if i%n == 0:
			return False
	return True

>>> isprime(0)
True
>>> def isprime(n):
	if n <2:
		print("Neither prime nor composite")
		return False
	for i in range(0,n):
		if i%n == 0:
			return False
	return True

>>> isprime(0)
Neither prime nor composite
False
>>> def isprime(n):
	if n <2:
		print("Neither prime nor composite")
		return False
	for i in range(0,n):
		if i%n == 0:
			return 
	return True

>>> isprime(0)
Neither prime nor composite
False
>>> def isprime(n):
	if n <2:
		print("Neither prime nor composite")
		return False
	for i in range(0,n):
		if i%n == 0:
			return

	return True

>>> def isprime(n):
	if n <2:
		print("Neither prime nor composite")
		return 
	for i in range(0,n):
		if i%n == 0:
			return False

	return True

>>> isprime(0)
Neither prime nor composite
>>> a=0
>>> while a<5:
	print(a)
	print("A is smaller than 5")
	a+=1

	
0
A is smaller than 5
1
A is smaller than 5
2
A is smaller than 5
3
A is smaller than 5
4
A is smaller than 5
>>> 
=================================================== RESTART: Shell ==================================================
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import pylearn
hello world
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'pylearn']
>>> input("Enter your name: ")
Enter your name: melvin
'melvin'
>>> a = input("Enter your name: ")
Enter your name: melvin
>>> a
'melvin'
>>> type(a)
<class 'str'>
>>> a = int(input("Enter a number "))
Enter a number 2
>>> type(a)
<class 'int'>
>>> a = input("Enter a number ")
Enter a number 3
>>> type(a)
<class 'str'>
>>> a='edwin'
>>> a=[1,2,3,4]
>>> a[0]
1
>>> a[2]
3
>>> a='edwin'
>>> a[0]
'e'
>>> def isprime(n):
	f=2
	while f<n:
		if n%f == 0:
			return False
		f+=1
	return True

>>> isprime(3)
True
>>> isprime(4)
False
>>> for i in range(1,100):
	if isprime(i):
		print(i,end=', ')

		
1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
>>> for i in range(1,5):
	print(i)

	
1
2
3
4
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> for i in range(10,0,-2):
	print(i)

	
10
8
6
4
2
>>> def isprime(n):
	f=2
	while f<n:
		if n%f == 0:
			return False
		f+=1
	return True

>>> def isprime(n):
	while f<n:
		if n%f == 0:
			return False
		f+=1
	return True

>>> isprime(4)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    isprime(4)
  File "<pyshell#103>", line 2, in isprime
    while f<n:
UnboundLocalError: local variable 'f' referenced before assignment
>>> def isprime(n):
	f=2
	while f<n:
		if n%f == 0:
			return False
		f+=1
	return True

>>> 
>>> for i in range(1,11):
	print(i, end= ' ')

	
1 2 3 4 5 6 7 8 9 10 
>>> a=list()
>>> print(a)
[]
>>> a=[]
>>> print(a)
[]
>>> a = [1,2,3,4]
>>> a=list(1,2)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a=list(1,2)
TypeError: list expected at most 1 argument, got 2
>>> a=list('edwin')
>>> a
['e', 'd', 'w', 'i', 'n']
>>> a.append(1)
>>> a
['e', 'd', 'w', 'i', 'n', 1]
>>> 
=================================================== RESTART: Shell ==================================================
>>> a=[]
>>> a= int(input("how
	     
SyntaxError: EOL while scanning string literal
>>> 
>>> def inputlist():
	a=[]
	n = int(input("How many elements to input?: "))
	for i in range(n):
		e=input("Enter element: ")
		a.append(e)
	return a

>>> inputlist()
How many elements to input?: 4
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
['1', '2', '3', '4']
>>> a=[]
>>> a[3]=1
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a[3]=1
IndexError: list assignment index out of range
>>> a[0]=1
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a[0]=1
IndexError: list assignment index out of range
>>> a = [1,2,3,4]
>>> a[0] = 6
>>> a
[6, 2, 3, 4]
>>> a = [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a[0] = 6
>>> a
[6, 2, 3, 4]
>>> a=list('edwin')
>>> a
['e', 'd', 'w', 'i', 'n']
>>> a = [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a=[1,2,3,'sameem',[1,2]]
>>> a[4]
[1, 2]
>>> a[4][0]
1
>>> a[4][1]
2
>>> help(a)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> a=[1,1,1,2,3,4]
>>> a.count(1)
3
>>> a.append('melvin')
>>> a
[1, 1, 1, 2, 3, 4, 'melvin']
>>> a.clear()
>>> a
[]
>>> a.extend('ababab')
>>> a
['a', 'b', 'a', 'b', 'a', 'b']
>>> a.pop()
'b'
>>> a.pop(0)
'a'
>>> a
['b', 'a', 'b', 'a']
>>> a.insert(1,3)
>>> a
['b', 3, 'a', 'b', 'a']
>>> a.in('a')
SyntaxError: invalid syntax
>>> a.index('a')
2
>>> a.remove('b')
>>> a
[3, 'a', 'b', 'a']
>>> a.remove('b')
>>> a
[3, 'a', 'a']
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a=['a','b','c','d',e]
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a=['a','b','c','d',e]
NameError: name 'e' is not defined
>>> a=['a','b','c','d']
>>> a.sort()
>>> a
['a', 'b', 'c', 'd']
>>> a= list('zebra')
>>> a
['z', 'e', 'b', 'r', 'a']
>>> a.sort()
>>> a
['a', 'b', 'e', 'r', 'z']
>>> a
['a', 'b', 'e', 'r', 'z']
>>> a= list('zebra')
>>> A=sorted(a)
>>> a
['z', 'e', 'b', 'r', 'a']
>>> A
['a', 'b', 'e', 'r', 'z']
>>> a.reverse ()
>>> a
['a', 'r', 'b', 'e', 'z']
>>> A=a.reverse()
>>> A
>>> a
['z', 'e', 'b', 'r', 'a']
>>> a.reverse()
>>> a
['a', 'r', 'b', 'e', 'z']
>>> a
['a', 'r', 'b', 'e', 'z']
>>> a.pop()
'z'
>>> a
['a', 'r', 'b', 'e']
>>> A=a.pop()
>>> a
['a', 'r', 'b']
>>> A
'e'
>>> type(A)
<class 'str'>
>>> type(a)
<class 'list'>
>>> a=[1,2,3,4,5]
>>> len(a)
5
>>> a='sameem'
>>> len(a)
6
>>> def binarysearch(List,Key):
	l=0
	u=len(List)-1

	while u>=l:
		mid=(l+u)//2
		if List[mid] == Key:
			return mid
		elif List[mid]>Key:
			u=mid-1
		else:
			l=mid+1
	return "Not Found!!"

>>> l=[1,2,45,46,57,68,80]
>>> binarysearch (l,68)
5
>>> binarysearch (l,99)
'Not Found!!'
>>> def binarysearch(List,Key):
	l=0
	u=len(List)-1
	cmp=0

	while u>=l:
		mid=(l+u)//2
		if List[mid] == Key:
			cmp+=1
			return mid
		elif List[mid]>Key:
			cmp+=1
			u=mid-1
		else:
			l=mid+1
	return "Not Found!!"

>>> def binarysearch(List,Key):
	l=0
	u=len(List)-1
	cmp=0

	while u>=l:
		mid=(l+u)//2
		if List[mid] == Key:
			cmp+=1
			return mid, cmp
		elif List[mid]>Key:
			cmp+=1
			u=mid-1
		else:
			l=mid+1
	return "Not Found!!", cmp

>>> binarysearch (l,68)
(5, 1)
>>> a='123'
>>> type(a)
<class 'str'>
>>> print('"')
"
>>> a= 'mel
SyntaxError: EOL while scanning string literal
>>> print("'")
'
>>> a= 'mel
SyntaxError: EOL while scanning string literal
>>> a= "mel
SyntaxError: EOL while scanning string literal
>>> st = ''' this
is a
multiline
string'''
>>> st
' this\nis a\nmultiline\nstring'
>>> print(st)
 this
is a
multiline
string
>>> st = """this
is a
multiline
string"""
>>> st
'this\nis a\nmultiline\nstring'
>>> print(st)
this
is a
multiline
string
>>> st='sameem'
>>> st[0]
's'
>>> st[0]='m'
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    st[0]='m'
TypeError: 'str' object does not support item assignment
>>> st='melvin'
>>> st
'melvin'
>>> st[:3]
'mel'
>>> st[:3:2]
'ml'
>>> st = 'this is a string'
>>> st[:6]
'this i'
>>> st[:6:2]
'ti '
>>> st[:7:2]
'ti s'
>>> a=list('melvin')
>>> a
['m', 'e', 'l', 'v', 'i', 'n']
>>> '  '.join(a)
'm  e  l  v  i  n'
>>> a= 'this is a string'
>>> a.split('s')
['thi', ' i', ' a ', 'tring']
>>> a.split(' ')
['this', 'is', 'a', 'string']
>>> ' '.join(a)
't h i s   i s   a   s t r i n g'
>>> ''.join(a)
'this is a string'
>>> S= ''.join(a)
>>> S
'this is a string'
>>> import string
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> v='aeiou'
>>> v='aeiou'
>>> 'l' in v
False
>>> a= 'm'
>>> m in string.ascii_letters
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    m in string.ascii_letters
NameError: name 'm' is not defined
>>> a in string.ascii_letters
True
>>> a =[1,2,3]
>>> 1 in a
True
>>> for ein string:
	
SyntaxError: invalid syntax
>>> for e in string:
	if e in string.ascii_letters :
		l+=1
	elif e in string.digits:
		d+=1

		
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    for e in string:
TypeError: 'module' object is not iterable

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 