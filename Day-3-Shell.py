Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> def fun(st):
	c,v,d,s,sp=0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: %s\nConsonants: %s\nDigits: %s\nSpecial Charecters: %s"%(v,c,d,s,sp))

	
>>> st='this is a test string with 1234 numbers !@#$"
SyntaxError: EOL while scanning string literal
>>> st='this is a test string with 1234 numbers !@#$'
>>> fun (st)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fun (st)
  File "<pyshell#17>", line 2, in fun
    c,v,d,s,sp=0
TypeError: cannot unpack non-iterable int object
>>> def fun(st):
	c,v,d,s,sp=0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: %d\nConsonants: %d\nDigits: %d\nSpecial Charecters: %d"%(v,c,d,s,sp))

	
>>> fun (st)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fun (st)
  File "<pyshell#22>", line 2, in fun
    c,v,d,s,sp=0
TypeError: cannot unpack non-iterable int object
>>> def fun(st):
	c,v,d,s,sp=0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: ",v,"Consonants: ",c,'Digits: ',d,'Spaces: ',s,'Special Charecters: ',sp)

	
>>> fun (st)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fun (st)
  File "<pyshell#25>", line 2, in fun
    c,v,d,s,sp=0
TypeError: cannot unpack non-iterable int object
>>> def fun(st):
	c=v=d=s=sp=0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: %s\nConsonants: %s\nDigits: %s\nSpecial Charecters: %s"%(v,c,d,s,sp))

	
>>> fun (st)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    fun (st)
  File "<pyshell#28>", line 15, in fun
    print("Vowels: %s\nConsonants: %s\nDigits: %s\nSpecial Charecters: %s"%(v,c,d,s,sp))
TypeError: not all arguments converted during string formatting
>>> st='this is a test string with 1234 numbers !@#$'
>>> def fun(st):
	c,v,d,s,sp=0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: ",v,"Consonants: ",c,'Digits: ',d,'Spaces: ',s,'Special Charecters: ',sp)

	
>>> fun (st)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fun (st)
  File "<pyshell#32>", line 2, in fun
    c,v,d,s,sp=0
TypeError: cannot unpack non-iterable int object
>>> def fun(st):
	c,v,d,s,sp=0,0,0,0,0
	vowels='AEIOUaeiou'
	for i in st:
		if i in vowels:
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: ",v,"Consonants: ",c,'Digits: ',d,'Spaces: ',s,'Special Charecters: ',sp)

	
>>> fun (st)
Vowels:  8 Consonants:  20 Digits:  4 Spaces:  8 Special Charecters:  4
>>> st='this is a test string with 1234 numbers !@#$'
>>> def fun(st):
	c,v,d,s,sp=0,0,0,0,0
	#vowels='AEIOUaeiou'
	for i in st:
		if i in "AIEOUaieou":
			v+=1
		elif i in string.ascii_letters:
			c+=1
		elif i in string.digits:
			d+=1
		elif i == ' ':
			s+=1
		else:
			sp+=1
	print("Vowels: ",v,"Consonants: ",c,'Digits: ',d,'Spaces: ',s,'Special Charecters: ',sp)

	
>>> fun (st)
Vowels:  8 Consonants:  20 Digits:  4 Spaces:  8 Special Charecters:  4
>>> 3/2
1.5
>>> 3//2
1
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> fabs(-1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    fabs(-1)
NameError: name 'fabs' is not defined
>>> math.fabs (-1)
1.0
>>> math.factorial (3)
6
>>> math.floor(2.34)
2
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'fun', 'math', 'st', 'string']
>>> from math import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'fun', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'math', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'st', 'string', 'tan', 'tanh', 'tau', 'trunc']
>>> import random
>>> random.randint(1,6)
5
>>> random.randint(1,6)
2
>>> random.randint(1,6)
4
>>> random.randint(1,6)
5
>>> random.randint(1,6)
2
>>> random.randint(1,6)
4
>>> random.randint(1,6)
3
>>> random.random()
0.8437020264442667
>>> random.choice([1,2,3,4,5,6,7,8,9]
	      )
7
>>> random.choice('mel')
'e'
>>> random.choice ((1,2,3,4,5))
4
>>> random.choice ({1,2,3,4,5,6,7})
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    random.choice ({1,2,3,4,5,6,7})
  File "C:\Python\Python 38 64\lib\random.py", line 291, in choice
    return seq[i]
TypeError: 'set' object is not subscriptable
>>> random.choice ({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    random.choice ({1:1,2:2})
  File "C:\Python\Python 38 64\lib\random.py", line 291, in choice
    return seq[i]
KeyError: 0
>>> max(1,2,4,6,19)
19
>>> min(1,2,4,6,19)
1
>>> max([1,2,3,4,5])
5
>>> max('mel')
'm'
>>> max('Mmel')
'm'
>>> ord('m')
109
>>> ord('M')
77
>>> 
=================================================== RESTART: Shell ==================================================
>>> ord("M")
77
>>> ord('m')
109
>>> chr(109)
'm'
>>> divmod(3/2)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    divmod(3/2)
TypeError: divmod expected 2 arguments, got 1
>>> divmod(3,2)
(1, 1)
>>> divmod(5,2)
(2, 1)
>>> a=int(input("Enter number: "))
Enter number: 
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a=int(input("Enter number: "))
ValueError: invalid literal for int() with base 10: ''
>>> int(input())
23
23
>>> import pylearn
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    import pylearn
  File "C:\Python\Python 38 64\pylearn.py", line 1, in <module>
    fun()
NameError: name 'fun' is not defined
>>> import pylearn
hello world
>>> help(pylearn )
Help on module pylearn:

NAME
    pylearn

FUNCTIONS
    fun()
    
    isprime(n)

FILE
    c:\python\python 38 64\pylearn.py


>>> import pylearn
>>> 
>>> help(pylearn )
Help on module pylearn:

NAME
    pylearn - #print("hello world")

FUNCTIONS
    fun()
    
    isprime(n)

FILE
    c:\python\python 38 64\pylearn.py


>>> 
=================================================== RESTART: Shell ==================================================
>>> import pylearn
>>> help(pylearn )
Help on module pylearn:

NAME
    pylearn - #print("hello world")

FUNCTIONS
    fun()
        Function to print Hello World
    
    isprime(n)
        Function to check whether an input number is prime

FILE
    c:\python\python 38 64\pylearn.py


>>> def fun_D(nr,ns=6):
	import random
	for i in range(nr):
		pass

	
>>> fun1(a,b=3):
	
SyntaxError: invalid syntax
>>> def fun1(a,b=3):
	print("a: ",a)
	print("b:", b)

	
>>> fun1(2)
a:  2
b: 3
>>> 
>>> fun1(2,5)
a:  2
b: 5
>>> fun(1,2)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    fun(1,2)
NameError: name 'fun' is not defined
>>> fun1(1,2)
a:  1
b: 2
>>> fun1(b=2,a=1)
a:  1
b: 2
>>> def fun_D(nr,ns=6):
	import random
	for i in range(nr):
		print(random.randint(1,ns))
	print("Thats all")

	
>>> fun_D(3)
2
4
2
Thats all
>>> fun_D(3,10)
6
3
7
Thats all
>>> a='sam'
>>> b='eem'
>>> a+b
'sameem'
>>> a*3
'samsamsam'
>>> vowels='AEIOUaeiou'
>>> 'Q' in vowels
False
>>> 'Q' not  in vowels
True
>>> A=a*3
>>> A
'samsamsam'
>>> a.find ('s')
0
>>> a.find('s',a.find('s'))
0
>>> A.find('s',a.find('s'))
0
>>> A.find('s',1)
3
>>> A.find('s',a.find(('s')+1))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    A.find('s',a.find(('s')+1))
TypeError: can only concatenate str (not "int") to str
>>> A.find('s',A.find('s'))
0
>>> A.find('s',A.find('s')+1)
3
>>> def strfind(st,,k,o):
	si = 0
	while o > 0:
		si=st.find(k)
		
SyntaxError: invalid syntax
>>> st='melvin'
>>> st.isalpha ()
True
>>> st='Melvin'
>>> st.lower()
'melvin'
>>> st
'Melvin'
>>> st = '   melvin   '
>>> st
'   melvin   '
>>> st.strip ()
'melvin'
>>> st
'   melvin   '
>>> st.strip ()
'melvin'
>>> st.lstrip()
'melvin   '
>>> st.rstrip()
'   melvin'
>>> title ="A Is The First Letter Of The Albhabet"
>>> title.istitle ()
True
>>> st = 'sameem'
>>> st.replace ('s','l')
'lameem'
>>> st
'sameem'
>>> st = "this is string with s"
>>> st.replace ('s','l')
'thil il ltring with l'
>>> " ".join('m','e','l','v','i','n')
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    " ".join('m','e','l','v','i','n')
TypeError: join() takes exactly one argument (6 given)
>>> " ".join(['m','e','l','v','i','n'])
'm e l v i n'
>>> " ".join('melvin')
'm e l v i n'
>>> st = 'string to partition'
>>> st.partition ('to')
('string ', 'to', ' partition')
>>> st.partition ('t')
('s', 't', 'ring to partition')
>>> st = 'string to partition'
>>> st.split()
['string', 'to', 'partition']
>>> st = "this is string with s"
>>> st.split('s')
['thi', ' i', ' ', 'tring with ', '']
>>> st.split()
['this', 'is', 'string', 'with', 's']
>>> def ispalindrome(st):
	#flag=0
	l=len(st)
	for i in range(l):
		if st[i]!=st[l-1-i]:
			return False
	return True

>>> st="malayalam"
>>> ispalindrome (st)
True
>>> st="alen"
>>> 
>>> ispalindrome (st)
False
>>> a=345
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    a[1]
TypeError: 'int' object is not subscriptable
>>> def ispalindrome(n):
	while n>0:
		d=n%10
		n//=10	j=j*10+d
		
SyntaxError: invalid syntax
>>> def ispalindrome(n):
	while n>0:
		d=n%10
		n//=10	j=j*10+d
		
SyntaxError: invalid syntax
>>> def ispalindrome(n):
	while n>0:
		d=n%10
		n//=10	j=j*10+d
		
SyntaxError: invalid syntax
>>> def ispalindrome(n):
	j=0
	m=n
	while n>0:
		d=n%10
		n//=10
		j=j*10+d
	if j == m:
		return True
	else:
		return False

	
>>> ispalindrome (101)
True
>>> ispalindrome (100)
False
>>> ispalindrome (010)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> ispalindrome (10)
False
>>> def main(s):
	for i in range(len(s)):
		if i%2==0:
			print(s[i],end='')

			
>>> main('melvin')
mli
>>> 