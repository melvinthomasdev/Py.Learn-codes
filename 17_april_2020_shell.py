Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> stck=[]
>>> a= input("What do you want to add?")
What do you want to add?12
>>> stck.append(a)
>>> atck
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    atck
NameError: name 'atck' is not defined
>>> stck
['12']
>>> stck.extent("melvin")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    stck.extent("melvin")
AttributeError: 'list' object has no attribute 'extent'
>>> stck.extend("melvin")
>>> stck
['12', 'm', 'e', 'l', 'v', 'i', 'n']
>>> ls=[0 for i in range(10)]
>>> ls
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> ls=['a' for i in range(10)]
>>> ls
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
>>> import random
>>> a=[random.randint(50) for i in range(10)]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a=[random.randint(50) for i in range(10)]
  File "<pyshell#14>", line 1, in <listcomp>
    a=[random.randint(50) for i in range(10)]
TypeError: randint() missing 1 required positional argument: 'b'
>>> a=[random.randint(1,50) for i in range(10)]
>>> a
[39, 1, 32, 34, 14, 24, 39, 6, 7, 39]
>>> a=[[0,0,0] for i in range(5)]
>>> a
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> for i in a:
	print(a)

	
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> for i in a:
	print(i)

	
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
>>> def addmat(m1,m2):
	pass

>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	c2=len(m2[0])
	if r1 = r2 and c1 = c2:
		
SyntaxError: invalid syntax
>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	c2=len(m2[0])
	m3=[[o for i in range(c1)] for j in range(r1)]
	if r1 == r2 and c1 == c2:
		for i in range(r1):
			for j in range(c1):
				m3[i][j] = m1[i][j]+m2[i][j]
		for i in m3:
			print(i)
	else:
		print("Invalid input!!!")

		
>>> m1=[[random.randint(1,5) for i in range(3)] for j in range(4)]
>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	print("Input")
	for i in m1:
		print(i)
	for i in m2:
		print(i)
	c2=len(m2[0])
	m3=[[o for i in range(c1)] for j in range(r1)]
	if r1 == r2 and c1 == c2:
		for i in range(r1):
			for j in range(c1):
				m3[i][j] = m1[i][j]+m2[i][j]
		print("Matrix after aadding:")
		for i in m3:
			print(i)
	else:
		print("Invalid input!!!")

		
>>> m1=[[random.randint(1,5) for i in range(3)] for j in range(4)]
>>> m2=[[random.randint(1,5) for i in range(3)] for j in range(4)]
>>> 
>>> addmat (m1,m2)
Input
[5, 5, 4]
[1, 4, 3]
[1, 1, 4]
[2, 4, 4]
[2, 3, 1]
[5, 4, 1]
[2, 5, 3]
[3, 2, 1]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    addmat (m1,m2)
  File "<pyshell#47>", line 11, in addmat
    m3=[[o for i in range(c1)] for j in range(r1)]
  File "<pyshell#47>", line 11, in <listcomp>
    m3=[[o for i in range(c1)] for j in range(r1)]
  File "<pyshell#47>", line 11, in <listcomp>
    m3=[[o for i in range(c1)] for j in range(r1)]
NameError: name 'o' is not defined
>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	print("Input")
	for i in m1:
		print(i)
	for i in m2:
		print(i)
	c2=len(m2[0])
	m3=[[0 for i in range(c1)] for j in range(r1)]
	if r1 == r2 and c1 == c2:
		for i in range(r1):
			for j in range(c1):
				m3[i][j] = m1[i][j]+m2[i][j]
		print("Matrix after aadding:")
		for i in m3:
			print(i)
	else:
		print("Invalid input!!!")

		
>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	print("m1")
	for i in m1:
		print(i)
	print()
	print('m2')
	for i in m2:
		print(i)
	print()
	c2=len(m2[0])
	m3=[[o for i in range(c1)] for j in range(r1)]
	if r1 == r2 and c1 == c2:
		for i in range(r1):
			for j in range(c1):
				m3[i][j] = m1[i][j]+m2[i][j]
		print("Matrix after aadding:")
		for i in m3:
			print(i)
	else:
		print("Invalid input!!!")

		
>>> addmat (m1,m2)
m1
[5, 5, 4]
[1, 4, 3]
[1, 1, 4]
[2, 4, 4]

m2
[2, 3, 1]
[5, 4, 1]
[2, 5, 3]
[3, 2, 1]

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    addmat (m1,m2)
  File "<pyshell#55>", line 14, in addmat
    m3=[[o for i in range(c1)] for j in range(r1)]
  File "<pyshell#55>", line 14, in <listcomp>
    m3=[[o for i in range(c1)] for j in range(r1)]
  File "<pyshell#55>", line 14, in <listcomp>
    m3=[[o for i in range(c1)] for j in range(r1)]
NameError: name 'o' is not defined
>>> def addmat(m1,m2):
	r1= len(m1)
	c1= len(m1[0])
	r2=len(m2)
	print("m1")
	for i in m1:
		print(i)
	print()
	print('m2')
	for i in m2:
		print(i)
	print()
	c2=len(m2[0])
	m3=[[0 for i in range(c1)] for j in range(r1)]
	if r1 == r2 and c1 == c2:
		for i in range(r1):
			for j in range(c1):
				m3[i][j] = m1[i][j]+m2[i][j]
		print("Matrix after aadding:")
		for i in m3:
			print(i)
	else:
		print("Invalid input!!!")

		
>>> addmat (m1,m2)
m1
[5, 5, 4]
[1, 4, 3]
[1, 1, 4]
[2, 4, 4]

m2
[2, 3, 1]
[5, 4, 1]
[2, 5, 3]
[3, 2, 1]

Matrix after aadding:
[7, 8, 5]
[6, 8, 4]
[3, 6, 7]
[5, 6, 5]
>>> def mtrans(m1):
	r=len(m)
	c=len(m[0])
	print('m1')
	for i in m1:
		print(i)
	print()
	tm=[[0 for i in range(c)] for j in range(r)]
	for i in range(r):
		for j in range(c):
			tm[j][i]=m1[i][j]
	for i in tm:
		print(i)

		
>>> m1=[[random.randint(1,5) for i in range(3)] for j in range(4)]
>>> for i in m1:
	print(i)

	
[5, 1, 3]
[2, 2, 3]
[4, 2, 1]
[4, 3, 5]
>>> m1=[[random.randint(1,5) for i in range(3)] for j in range(4)]
>>> for i in m1:
	print(i)

	
[3, 2, 2]
[4, 5, 4]
[4, 1, 4]
[1, 1, 1]
>>> def mtrans(m1):
	r=len(m)
	c=len(m[0])
	print('m1')
	for i in m1:
		print(i)
	print()
	tm=[[0 for i in range(c)] for j in range(r)]
	for i in range(r):
		for j in range(c):
			tm[j][i]=m1[i][j]
	for i in tm:
		print(i)

		
>>> 
>>> mtrans (m1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    mtrans (m1)
  File "<pyshell#79>", line 2, in mtrans
    r=len(m)
NameError: name 'm' is not defined
>>> def mtrans(m):
	r=len(m)
	c=len(m[0])
	print('m1')
	for i in m:
		print(i)
	print()
	tm=[[0 for i in range(c)] for j in range(r)]
	for i in range(r):
		for j in range(c):
			tm[j][i]=m[i][j]
	for i in tm:
		print(i)

		
>>> mtrans (m1)
m1
[3, 2, 2]
[4, 5, 4]
[4, 1, 4]
[1, 1, 1]

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    mtrans (m1)
  File "<pyshell#83>", line 11, in mtrans
    tm[j][i]=m[i][j]
IndexError: list assignment index out of range
>>> def mtrans(m):
	r=len(m)
	c=len(m[0])
	print('m')
	for i in m:
		print(i)
	print()
	tm=[[0 for i in range(c)] for j in range(r)]
	for i in range(r):
		for j in range(c):
			tm[i][j]=m[j][i]
	for i in tm:
		print(i)

		
>>> mtrans (m1)
m
[3, 2, 2]
[4, 5, 4]
[4, 1, 4]
[1, 1, 1]

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    mtrans (m1)
  File "<pyshell#86>", line 11, in mtrans
    tm[i][j]=m[j][i]
IndexError: list index out of range
>>> def mtrans(m):
	r=len(m)
	c=len(m[0])
	print('m')
	for i in m:
		print(i)
	print()
	tm=[[0 for i in range(r)] for j in range(c)]
	for i in range(r):
		for j in range(c):
			tm[i][j]=m[j][i]
	for i in tm:
		print(i)

		
>>> mtrans (m1)
m
[3, 2, 2]
[4, 5, 4]
[4, 1, 4]
[1, 1, 1]

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    mtrans (m1)
  File "<pyshell#89>", line 11, in mtrans
    tm[i][j]=m[j][i]
IndexError: list index out of range
>>> def mtrans(m):
	r=len(m)
	c=len(m[0])
	print('m')
	for i in m:
		print(i)
	print()
	tm=[[0 for i in range(r)] for j in range(c)]
	for i in range(c):
		for j in range(r):
			tm[i][j]=m[j][i]
	for i in tm:
		print(i)

		
>>> mtrans (m1)
m
[3, 2, 2]
[4, 5, 4]
[4, 1, 4]
[1, 1, 1]

[3, 4, 4, 1]
[2, 5, 1, 1]
[2, 4, 4, 1]
>>> def diagmat(m):
	r=len(m)
	c=len(m[0])
	if r == c:
		for i in range (r):
			print (m[i][i],end=' ')
		for i in range(r)
			print(m[i][c-i],end=' ')
			
SyntaxError: invalid syntax
>>> 
>>> def diagmat(m):
	r=len(m)
	c=len(m[0])
	if r == c:
		for i in range (r):
			print (m[i][i],end=' ')
		for i in range(r):
			print(m[i][c-i],end=' ')

			
>>> m1
[[3, 2, 2], [4, 5, 4], [4, 1, 4], [1, 1, 1]]
>>> diagmat(m1)
>>> def diagmat(m):
	r=len(m)
	c=len(m[0])
	if r == c:
		for i in range (r):
			print (m[i][i],end=' ')
		for i in range(r):
			print(m[i][c-i],end=' ')
	else:
		print("Invalid input!!!")

		
>>> diagmat(m1)
Invalid input!!!
>>> m1=[[random.randint(1,5) for i in range(3)] for j in range(3)]
>>> m1
[[1, 1, 2], [5, 4, 3], [1, 2, 4]]
>>> for i in m1:
	print(i)

	
[1, 1, 2]
[5, 4, 3]
[1, 2, 4]
>>> diagmat (m1)
1 4 4 Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    diagmat (m1)
  File "<pyshell#111>", line 8, in diagmat
    print(m[i][c-i],end=' ')
IndexError: list index out of range
>>> def diagmat(m):
	r=len(m)
	c=len(m[0])
	if r == c:
		for i in range (r):
			print (m[i][i],end=' ')
		for i in range(r):
			print(m[i][-(i+1)],end=' ')
	else:
		print("Invalid input!!!")

		
>>> diagmat (m1)
1 4 4 2 4 1 
>>> def diagmat(m):
	r=len(m)
	c=len(m[0])
	if r == c:
		for i in range (r):
			print (m[i][i],end=' ')
		print()
		for i in range(r):
			print(m[i][-(i+1)],end=' ')
	else:
		print("Invalid input!!!")

		
>>> diagmat (m1)
1 4 4 
2 4 1 
>>> for i in m:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    for i in m:
NameError: name 'm' is not defined
>>> for i in m1:
	print(i)

	
[1, 1, 2]
[5, 4, 3]
[1, 2, 4]
>>> diagmat (m1)
1 4 4 
2 4 1 
>>> 