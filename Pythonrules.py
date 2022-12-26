For path specification, python uses forward slashes. Hence if you are working with a file, the default path for the file in case of Windows OS will have backward slashes, which you will have to convert to forward slashes to make them work in your python script.
For window's path C:\folderA\folderB relative python program path should be C:/folderA/folderB

In python, there is no command terminator, which means no semicolon ; or anything.
So if you want to print something as output, all you have to do is:

print ("Hello, World!")
Oops! we just shared the first python program too with you. Yes, just one single statement.

In one line only a single executable statement should be written and the line change act as command terminator in python.
To write two separate executable statements in a single line, you should use a semicolon ; to separate the commands. For example,

print ("Hello, World!") ; print ("This is second line")


In python, you can use single quotes '', double quotes "" and even triple quotes ''' """ to represent string literals.
word = 'word'
sentence = "This is a one line sentence."
para = """This is a paragraph 
which has multiple lines"""
In python, you can write comments in your program using a # at the start. A comment is ignored while the python script is executed.
# this is a comment
print ("Hello, World!")
# this is a 
# multiline comment
Line Continuation: To write a code in multiline without confusing the python interpreter, is by using a backslash \ at the end of each line to explicitly denote line continuation. For example,
sum =  123 + \
       456 + \
       789

Expressions enclosed in ( ), [ ] or { } brackets don't need a backward slash for line continuation. For example,

vowels = ['a', 'e', 'i',
          'o', 'u']
Blank lines in between a program are ignored by python.
Code Indentation: This is the most important rule of python programming. In programming language like Java, C or C++, generally curly brackets { } are used to define a code block, but python doesn't use brackets, then how does python knows where a particular code block ends. Well python used indentation for this.
It is recommended to use tab for indentation, although you can use spaces for indentation as well, just keep in mind that the amount of indentation for a single code block should be same.

if True:
print ("Yes, I am in if block");
# the above statement will not be 
# considered inside the if block
the correct way would be,

if True:
    # this is inside if block 
    print ("Yes, I am in if block")
Also, the following code will give error, as the statements are differently indented:

if True:
    # this is inside if block 
    print ("Yes, I am in if block")
    # this will give error
        print ("me too")
again, the correct way to do so is to keep all the statements of a particular code block at same indentation.


if True:
    # this is inside if block 
    print ("Yes, I am in if block")
    print ("me too")
So these are some basic rules that you must know so that it becomes easier for us to learn various concepts of python programming in the coming tutorials.

First Python Program
We already shared the first python program with you while learning the syntax. Yes, we were not joking, it's just one single line, nothing above it, nothing below it. To print Hello, World! on screen, all you have to do is:

print ("Hello, World!")

You can write and execute this code in IDLE, or you can save this code in a python code file, name it test.py(you can name it anything, just keep the extension of the file as .py).

To run the test.py python script, open IDLE, go to the directory where you saved this file using the cd command, and then type the following in command prompt or your terminal:

python test.py
This will execute the python script and will show you the output in the line below.

From the next tutorial we will start learning the various concepts of python programming language.

← Prev
Next →
  Python MCQ Tests
Best Python questions to crack job interview.
Python  Python Code Examples
Python Programs, How-tos and lot more.
studytonight.com  
   

About Us

Testimonials

Privacy Policy

Terms

Contact Us

Suggest

We are Hiring!

© 2022 Studytonight Technologies Pvt. Ltd.

  Learn Coding (for beginners)
  Tutorial Library
  Interview Tests
  Curious
  Practice Coding
Coding Courses
Learn Go Lang
Learn JavaScript
Learn CSS
Learn HTML
Resources
C Language
C++/STL
Java
DBMS
Python
PHP
Android
Game Development
Data Structure & Alog.
Operating System
Computer Network
Computer Architecture
Docker
GO Language
GIT Guide
Linux Guide
More...
Interview Tests
Java Interview Tests
Python Interview Tests
DBMS Interview Tests
Linux Interview Tests
Aptitude Tests
GATE 2022 Tests
More...
Projects/Programs
Python Projects
C Projects
Python Programs
C Programs
C++ Programs
Java Programs

