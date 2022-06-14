
# Code Review

Code Review for the Anagram program .

# Efficiency and Correctness
Firstly , i appreciate the effort you have put in solving this problem . 
In as much as you did your best in trying to solve this problem . There are some few things i would like to bring your attention to .

I realised that you created a class without a constructor . Recall that constructors are generally used for instantiating an object
.Instances of a class almost always have instance variables, and they need to be created in __init__ to ensure that every instance automatically has them. 
In general , we start by construction .

```
class Solution:
    def __init__(self,words):
        self.words = words
    

```
In our example __self.words__ is an instance variable . Creating this is better , since every object will have its own copy of the instance attribute. 
This means that for each object of a class, the instance variable value will be different, which is good and scalable .
__Note__ that without using this method , your program can return the right results , the method exampled above can be another better solution.

On the other hand , its good to see that you created your instance method and included __self__ . 

Furthermore , in line 5 , you seem to be wanting to sort your strings and join spaces within the strings . First of all you should note that the __sorted()__ function generally accepts
an iterable as its first argument . The syntax of the __sorted()__ function is:

```
sorted(iterable, key=None, reverse=False)

```

In your solution , you could have provided the relevant iterable as your argument .
For instance ;

```
sortedWord = ''.join(sorted(word))

```

Furthermore , recall that an instance method accesses and even modify the value of attributes of an instance
. In other words instance methods are used to read or modify the state of an object.Your method is doing less of that , i suggest that you
create instance variable as suggested above and manipulate them using the method you created in line 2 .

Looking at your solution , it appears as if you are using are using the __append__ method on a dictionary . Please note this 
method applies to lists . To append an element to an existing dictionary, you have to use the dictionary name followed by square brackets with the key name and assign a value to it.

```
results[sortedWord] += [word]

```

In terms of correctness , your code does not fullfill the specifications .To further understand the logical flow and the reasoning behind grouping anagrams , i suggest that you have a look a
at this resource (https://www.geeksforgeeks.org/python-group-anagrams-from-given-list/)
# Style

In line 3 you did not indent according to Python standards . 
Indentation is key in python to define the blocks of statements. The number of spaces must be uniform in a block of code. It is preferred to use four whitespaces instead of tabs to indent in python
. For example line 3 could have been transformed to ->

```
        def groupAnagrams(self, strs):
            result = {}
```
Note that this rule is found in PEP8 .Recall that whenever you are writing a Python program, you should always adhere to the guidelines outlined in PEP8 . PEP 8 is a comprehensive styling guide for your Python code. This guide includes rules about naming objects, spacing rules, and how the code is laid out. Be sure to follow these guidelines.
Check out https://realpython.com/python-pep8/).

Going forward , please indent your code according to these standards .

Your variable names are good but they can be improved . Avoid using letters as your variable names , use more descriptive variable names . 
Your class name can be named differently as well.

```
#Instead of naming your class like this
class Solution:
    pass

# Its better this way
class GroupAnagrams:
    pass
```
# Documentation

In general , you did not document your code .
For this program , i suggest that you use Doc strings . Python documentation string or commonly known as docstring, is a string literal, and it is used in the class, module, function, or method definition.
__Note__ that Docstrings are great for understanding the functionality of the larger part of the code .

I will suggest you use doc strings instead of comments . Docstrings are similar in spirit to commenting, but they are enhanced, more logical, and useful version of commenting. Here is how you document your code using docstrings ;
```
class GroupAnagrams:
    '''This class groups anagrams'''

```

The qouted strings here are called doc strings .The standard convention is to use the triple-double quotes.
And there are placed right after the definition of a function, method, class, or module .

The most advantageous thing is that we can We can later use the __doc__  attribute to retrieve this docstring. For instance;
```
print(GroupAnagrams.__doc__)
```
Going forward , i suggest that you use doc strings to document your code as described and shown .


In conclusion , you tried your best here and i commend you for that . However i will suggest that you follow the suggestions above and resubmit !
Thank you !
