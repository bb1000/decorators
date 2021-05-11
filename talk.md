# Decorators (Advanced topics)

BB1000 Programming in Python


---

layout: false

## Decorators in Python: basic concepts

- Python function definition

~~~
def function_name(parameters):
    "function docstring"
    function body
    return [expression]
~~~

- Python class method definition

~~~
def methodname(self, parameters):
    "method docstring"
    method body
    return [expression]
~~~

* Functions are first-class objects:
    * implemented operators can be applied to function variable
    * functions can be passed as arguments to other functions
    * functions can be used as class/object variables in Class

---

## Decorators in Python: basic concepts

* passing arguments to function via args-kwargs syntax

~~~
def function name(required, *args, **kwargs):
    "function docstring"
    function body
    return[expression]
~~~

* required parameters of the function
* args are positional parameters of function (tuple)
* kwargs are key-valued parameters of the function (dict)
* Definition: a decorator extends and modified the behaviour of a callable
  (functions, ethods, and classes) without permantly modifying the callable
  itself
* Ordinary way for calling function inside another function

---

~~~
def empty_decorator(func):
    return func
    
def hello():
    return "Hello world"
    
simple_hello = empty_decorator(hello)

>>> simple_hello()
Hello world!
~~~

* Returning modified function from decorator

~~~
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
    
@uppercase
def hello():
    return "Hello world!"
    
>>> hello()
HELLO WORLD!
~~~

---
* Multiple decorators applied to single function

~~~
def strong(func):
    def wrapper():
        return '**' + func() + '**'
    return wrapper
    
def emphasis(func):
    def wrapper():
        return'!!' + func() + '!!'
    return wrapper
    
@emphasis
@strong
def hello():
    return'Hello World'
    
>>> hello()
!!**Hello World**!!
~~~

---

* Passing variables to decorator

~~~
def decorator_function(func):
    defwrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
~~~

---

* Simple example of trace decorator

~~~
def trace(func):
    def wrapper(*args, **kwargs):
        print(
            f'TRACE: calling {func.__name__}() '
            f'with {args}, {kwargs}'
        )
        original_result = func(*args, **kwargs)
        print(
            f'TRACE: {func.__name__}() '
            f'returned {original_result!r}'
        )
        return origiginal_results
    return wrapper
~~~

* Apply trace decorator to function

~~~
@trace
def say(greet, name):
    return greet + ",' +  name
~~~
~~~
>>> say("Hello", "world")
TRACE: calling say() with ('Hello', 'world'), {}
TRACE: say() returned 'Hello, world'
Hello, world
~~~

---

* Decorate a class method

~~~
def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return"<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper
    
class Person:
    def__init__(self):
        self.name = "John"
        self.family = "Doe"
        
    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family
        
~~~
~~~
my_person = Person()
print(my_person.get_fullname())
~~~

---

Comments on decorators:

* decorators is good way to avoid code duplication
* decorators allows to write more "pythonic" and clean code
* use wraptools to make your decorators debug friendly
