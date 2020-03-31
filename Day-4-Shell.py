Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ls=[1,2,3]
>>> st='leo'
>>> tup=(1,2,3)
>>> a={'me':'melvin','s':'sameem','le':'leo'}
>>> type(a)
<class 'dict'>
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0]
KeyError: 0
>>> a['me']
'melvin'
>>> a={1:1,2:2,3:3}
>>> a[1]
1
>>> a={1:'melvin',2:2,3:[1,23]}
>>> a[1]
'melvin'
>>> a[2]
2
>>> a[3]
[1, 23]
>>> a[3][0]
1
>>> a[1]='sameem'
>>> a
{1: 'sameem', 2: 2, 3: [1, 23]}
>>> a.keys()
dict_keys([1, 2, 3])
>>> a.values()
dict_values(['sameem', 2, [1, 23]])
>>> a.items()
dict_items([(1, 'sameem'), (2, 2), (3, [1, 23])])
>>> a=dict([(1,'melvin'),(2,'sameem')])
>>> a
{1: 'melvin', 2: 'sameem'}
>>> for i in a:
	print(a[i])

	
melvin
sameem
>>> for i in a: #traversing a dictionary
	print(a[i])

	
melvin
sameem
>>> for i in a: #traversing a dictionary
	print(i,a[i])

	
1 melvin
2 sameem
>>> a=dict([('mel','melvin'),('sam','sameem')])
>>> 
>>> for i in a: #traversing a dictionary
	print(i,a[i])

	
mel melvin
sam sameem
>>> a
{'mel': 'melvin', 'sam': 'sameem'}
>>> a['ed']='edwin'
>>> a
{'mel': 'melvin', 'sam': 'sameem', 'ed': 'edwin'}
>>> d1={1:"me",2:'sa',3:'ed'}
>>> d2={2:'we',4:'er',5:'kl'}
>>> d1.update (d2)
>>> d1
{1: 'me', 2: 'we', 3: 'ed', 4: 'er', 5: 'kl'}
>>> d1.pop ()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d1.pop ()
TypeError: pop expected at least 1 argument, got 0
>>> d1.pop (0)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d1.pop (0)
KeyError: 0
>>> del d1[2]
>>> d1
{1: 'me', 3: 'ed', 4: 'er', 5: 'kl'}
>>> d1.has_key(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d1.has_key(1)
AttributeError: 'dict' object has no attribute 'has_key'
>>> def contact():
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	k=input("Enter name to return phone number: ")
	return directory[k]

>>> contact()
Number of elements: 4
Enter name: melvn
enter Number: 123
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    contact()
  File "<pyshell#51>", line 5, in contact
    directory[n]=input("enter Number: ")
NameError: name 'directory' is not defined
>>> def contact():
	directory={}
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	k=input("Enter name to return phone number: ")
	return directory[k]

>>> contact()
Number of elements: 2
Enter name: melvin
enter Number: 234
Enter name: sameem
enter Number: 123
Enter name to return phone number: sameem
'123'
>>> def contact():
	directory={}
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	while True:
		k=input("1. Get phone number:\n2.exit: ")
		if k == 1:
			key=input("Enter name:")
			return directory[key]
		elif k==2:
			break
		else:
			print("Invalid Choice!!")

			
>>> contact()
Number of elements: 4
Enter name: q
enter Number: 13
Enter name: w
enter Number: 23
Enter name: rf
enter Number: 4
Enter name: ss
enter Number: 55
1. Get phone number:
2.exit: 1
Invalid Choice!!
1. Get phone number:
2.exit: 
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    contact()
  File "<pyshell#61>", line 8, in contact
    k=input("1. Get phone number:\n2.exit: ")
KeyboardInterrupt
>>> def contact():
	directory={}
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	while True:
		k=input("1. Get phone number:\n2.exit: ")
		if k == '1':
			key=input("Enter name:")
			return directory[key]
		elif k=='2':
			break
		else:
			print("Invalid Choice!!")

			
>>> contact()
Number of elements: 4
Enter name: qw
enter Number: 12
Enter name: qe
enter Number: 23
Enter name: as
enter Number: 3
Enter name: asx
enter Number: 23
1. Get phone number:
2.exit: 1
Enter name:qw
'12'
>>> def contact():
	directory={}
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	while True:
		k=input("1. Get phone number:\n2.exit: ")
		if k == '1':
			key=input("Enter name:")
			print directory[key]
		elif k=='2':
			break
		else:
			print("Invalid Choice!!")
			
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(directory[key])?
>>> 
>>> def contact():
	directory={}
	a=int(input("Number of elements: "))
	for i in range(a):
		n=input("Enter name: ")
		directory[n]=input("enter Number: ")
	while True:
		k=input("1. Get phone number:\n2.exit: ")
		if k == '1':
			key=input("Enter name:")
			print (directory[key])
		elif k=='2':
			break
		else:
			print("Invalid Choice!!")

			
>>> 
>>> contact()
Number of elements: 3
Enter name: qw
enter Number: 23
Enter name: er
enter Number: 45
Enter name: ty
enter Number: 67
1. Get phone number:
2.exit: 1
Enter name:qw
23
1. Get phone number:
2.exit: 4
Invalid Choice!!
1. Get phone number:
2.exit: 2
>>> a=(1,)
>>> a
(1,)
>>> a[0]
1
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a[1]
IndexError: tuple index out of range
>>> a[0]='mel'
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a[0]='mel'
TypeError: 'tuple' object does not support item assignment
>>> a=,
SyntaxError: invalid syntax
>>> a=10,
>>> a
(10,)
>>> mel=(1,2,3)
>>> vin=(2,3,4)
>>> mel + vin
(1, 2, 3, 2, 3, 4)
>>> mel
(1, 2, 3)
>>> vin
(2, 3, 4)
>>> mel =mel + vin
>>> mel
(1, 2, 3, 2, 3, 4)
>>> (1, 2, 3, 2, 3, 4)
(1, 2, 3, 2, 3, 4)

>>> 
>>> a=(1,2,3)
>>> a=(1)
>>> a=(1,2,3)
>>> b=1,
>>> c=3,4,5
>>> d=tuple([1,2,3])
>>> a
(1, 2, 3)
>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class 'tuple'>
>>> type(d)
<class 'tuple'>
>>> a=(1,2,3,4,5,6,7,8)
>>> a[:3]
(1, 2, 3)
>>> a[::-1]
(8, 7, 6, 5, 4, 3, 2, 1)
>>> set
<class 'set'>
>>> a={1,2,3}
>>> type(a)
<class 'set'>
>>> a
{1, 2, 3}
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> a
{1, 2, 3}
>>> dicti={1:1,2:2}
>>> type(dicti)
<class 'dict'>
>>> type(a)
<class 'set'>
>>> a=str(mel)
>>> a
'(1, 2, 3, 2, 3, 4)'
>>> mel
(1, 2, 3, 2, 3, 4)
>>> trpe(mel)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    trpe(mel)
NameError: name 'trpe' is not defined
>>> type(mel)
<class 'tuple'>
>>> type(a)
<class 'str'>
>>> a=1+4j
>>> type(a)
<class 'complex'>
>>> a.conjugate ()
(1-4j)
>>> a.real ()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a.real ()
TypeError: 'float' object is not callable
>>> a.real
1.0
>>> a.imag
4.0
>>> a
(1+4j)
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> from random import randint
>>> from random random import randint as rn
SyntaxError: invalid syntax
>>> from random import randint as rn
>>> def inputfunction():
	a=int(input())
	assert 5<a<20

	
>>> indef inputfunction():
	a=int(input())
	assert 5<a<20
	
SyntaxError: invalid syntax
>>> def inputfunction():
	a=int(input())
	assert 5<a<20
	print (a)

	
>>> inputfunction ()
5
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    inputfunction ()
  File "<pyshell#137>", line 3, in inputfunction
    assert 5<a<20
AssertionError
>>> def inputfunction():
	a=int(input())
	assert 5<=a<=20
	print (a)

	
>>> inputfunction ()
5
SyntaxError: multiple statements found while compiling a single statement
>>> inputfunction ()
7
7
>>> inputfunction ()
71
SyntaxError: multiple statements found while compiling a single statement
>>> inputfunction ()

Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    inputfunction ()
  File "<pyshell#140>", line 2, in inputfunction
    a=int(input())
ValueError: invalid literal for int() with base 10: ''
>>> inputfunction (5)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    inputfunction (5)
TypeError: inputfunction() takes 0 positional arguments but 1 was given
>>> inputfunction()
5
5
>>> inputinputfunction ()
45
SyntaxError: multiple statements found while compiling a single statement
>>> for
SyntaxError: invalid syntax
>>> 
>>> 
>>> exec '1+2'
SyntaxError: Missing parentheses in call to 'exec'
>>> 
>>> exec('1+2')
>>> a=exec('1+2')
>>> a
>>> print(a)
None
>>> prog = 'print("The sum of 5 and 10 is", (5+10))'
>>> exec(prog)
The sum of 5 and 10 is 15
>>> a= lambda(a,b):a+b
SyntaxError: invalid syntax
>>> a= lambda a,b:a+b
>>> a(1,2)
3
>>> def add(a,b):
	return a+b

>>> add(1,3)
4
>>> a=5
>>> 
========================================== RESTART: Shell =========================================
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> 1+2
3
>>> 'mel'+'vin'
'melvin'
>>> a=5
>>> def fun():
	a=4
	global a
	
SyntaxError: name 'a' is assigned to before global declaration
>>> a=5
>>> def fun():
	global a
	a=10

	
>>> a
5
>>> def fun():
	global a
	print(a)

	
>>> fun()
5
>>> def fun():
	#global a
	print(a)

	
>>> fun()
5
>>> def fun():
	#global a
	print(a+1)

	
>>> fun()
6
>>> a
5
>>> def fun():
	global a
	a+=1
	print(a)

	
>>> fun()
6
>>> a
6
>>> [1,2,3,4,5,6,7,8,9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [1,2,3],[4,5,6],[7,8,9]
([1, 2, 3], [4, 5, 6], [7, 8, 9])
>>> 