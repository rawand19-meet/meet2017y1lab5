Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=
SyntaxError: invalid syntax
>>> a=['she','sells','sea','shells','by','the','sea','shore',]
>>> b="selfish shellfish"
>>> c=[1,1,2,3,5,8,13]
>>> a[1]
'sells'
>>> b[3:4]
'f'
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[8:11]
[]
>>> a[:-6]
['she', 'sells']
>>> a[2:4]
['sea', 'shells']
>>> c[1]+c[2]
3
>>> a[2]
'sea'
>>> a[3]
'shells'
>>> c[5]
8
>>> a*3
['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> "by'in a
SyntaxError: EOL while scanning string literal
>>> self in b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    self in b
NameError: name 'self' is not defined
>>> a[2]==a[6]
True
>>> [1,2,5] in c
False
>>> 'sh' in c
False
>>> a[3]==b[8:13]
False
>>> dog='dalmatian'
>>> len(dog)
9
>>> dogs=[dog,'poodle','boxer'0
      
SyntaxError: invalid syntax
>>> dogs=[dog,'poodle','boxer']
>>> len(dogs)
3
>>> 
====== RESTART: /home/student/rawand19_lab5/meet2017y1lab5/stringfun.py ======
>>> string_test
<function string_test at 0x7fbf343a4488>
>>> string_test("amir")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    string_test("amir")
  File "/home/student/rawand19_lab5/meet2017y1lab5/stringfun.py", line 2, in string_test
    if len >2 and s[0]==s[-1]:
TypeError: unorderable types: builtin_function_or_method() > int()
>>> 
====== RESTART: /home/student/rawand19_lab5/meet2017y1lab5/stringfun.py ======
>>> string_test([1,2,3,4,5,1])
T
>>> string_test[2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    string_test[2]
TypeError: 'function' object is not subscriptable
>>> string_test([2])
F
>>> 
