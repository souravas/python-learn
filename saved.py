poem: str = """
everything
is good
and
"""

txt_value: str = '100'
int_value: int = 58
print(txt_value + str(int_value))
print(5.5+1) # automatic conversion to float

a: str = input('Enter a value: ')
b: str = input('Enter b value: ')
print('The result is: ', int(a)+int(b))

is_connected: bool = True
has_money: bool = False
print(int(True)) # 1
print(int(False)) # 0

my_list: list = [1, True, 'Text', [1,23,4]]

people: list[str] = ["Bob", "The", "Builder"]
print(people[0])

people.append("is bad")
print(people)
people.remove('is bad')
print(people)

people.append('something')
people.pop()
print(people)

people[0] = 'Sourav'
print(people)

people.insert(1, 'is')
print(people)

people.clear()
print(people)

# tuple can't be changed.
items1: tuple = () # empty
items2: tuple = (1,) # denotes tuple. , is required. otherwise, it's considered integer of 1.
items3: tuple = 1,2,3 # denotes tuple. () are not required for readability.
items4: tuple = (1,3,4)
print(type(items1), type(items2), type(items3), type(items4))


elements: set = {99, True, 'Bob'}
print(elements)
elements.add('James')
print(elements)
elements.remove('Bob')
elements.pop() # random element removed
elements.clear() # removes everything
empty: set = set() # {} creates dictionary. set() is required for creating empty set
# print(elements[0]) # raises error.

things: frozenset = frozenset({99, True, 1,2,3})
print(things)
# things.add('Bob') # raises error.

empty: dict = {}
users: dict = {'Bob': 1, 2: 'Luigi'}
print(users[2]) # Luigi
# print(users[192]) # raise error
weather: dict = {'time': '12:00', 'weather' : {'morning': 'rain'}}
print(weather['weather']['morning'])
users[3]='Marioo'
users[1] = 'Sourav'
print(users)
users.pop(2) # pops the key 2.
print(users)
users.clear()

no_value: None = None
users: dict = {1: 'Mario'}
print(users.get(3)) # returns None if key doesn't exist
possible_user: str | None = users.get(3) # | denotes union type. can be either of these types
print(possible_user)

name: str = 'sourav'
print(f'text {name}')
story: str = f"""
this is a story of {name}
"""
print(story)

age: int = 30
if age >= 21:
    print('you may enter')
elif 21 > age > 18:
    print(' you may or may not enter')
else:
    print('you are not allowed')

number: int = 0
if number > 0:
    result = 'wow'
else:
    result = 'no'
print(result)
result: str = 'wow' if number > 0 else 'no'
print(result)
condition: bool = True
var: str = 'True' if condition else 'False'
print(var)

text: str = 'Hello, World!'
for i in range(3):
    print(text)
people: list[str] = ['Bob', 'Sourav']
for person in people:
    if len(person) > 4:
        print(f'{person} has long name.')
    else:
        print(person)

i: int = 5
while i > 0:
    print(f'hello: {i}')
    i -= 1
connected: bool = True

import time
while connected:
    print('using internet...')
    time.sleep(5)
    connected = False
print('connection ended...')

while True:
    user_input: str = input('you: ')
    if user_input == 'hello':
        print('hi there!')
    else:
        print('yes. interesting')

number: int = 5
while number > 0:
    number -=  1
    if number == 2:
        print('break at 2')
        break
    print(number)
print('Done.')

number: int = 5
while number > 0:
    number -=  1
    if number == 2:
        print('skipping 2')
        continue
    print(number)
print('Done.')

total: int = 0
while True:
    user_input: int = int(input('Enter a number: '))
    if user_input < 0:
        print('enter positive')
        continue
    if user_input == 0:
        print(f'total: {total}')
        break
    total += user_input

for i in range(3):
    print(f'Iteration: {i}')
else:
    print('success!') # if any break happens, this isn't executed. only executed if for loop executes completely

import random
import sys

print('welcome to rock,paper,scissors')
moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
valid_moves: list[str] = list(moves.keys())
while True:
    user_input = input('choose rock, paper or scissors: ').lower()
    if user_input == 'exit':
        print('exiting...')
        sys.exit()
    if user_input not in valid_moves:
        print('invalid move...')
        continue
    ai_input: str = random.choice(valid_moves)
    print('___________________________________')
    print('You: ', moves[user_input])
    print('AI: ', moves[ai_input])
    print('___________________________________')
    if user_input == ai_input:
        print("It's a tie!")
    elif ((user_input == 'rock' and ai_input == 'scissors')
          or (user_input == 'paper' and ai_input == 'rock')
          or (user_input == 'scissors' and ai_input == 'paper')):
        print('You won!')
    else:
        print('AI won!')


from _datetime import datetime
import time

def greet():
    print('hello')

greet()

def show_time():
    now: datetime = datetime.now()
    print(f'Time: {now:%H:%M:%S}')

show_time()
time.sleep(2)
show_time()

def get_status():
    pass

for i in range(3):
    pass

def get_status_new():
    ... # same as pass

def greet(name: str, language: str, default: str = 'Hello'):
    if language == 'ja':
        print(f'Arigato {name}')
    else:
        print(f'{default} {name}')

greet('Sourav', 'ja')
greet('Sourav', 'en', )
greet('Sourav', 'en', 'Hi there!')
greet(name='Sourav', language='en')
greet(default='Hi there!', name='Sourav', language='en')

def get_length(text: str) -> int:
    return len(text)

print(get_length('Mario'))

def get_connection() -> None:
    print("connecting to internet")


def func() -> None:
    func()

print(1,2,3,4, True)
print(1,2,3,4, True, sep=':')

def add(*args: int) -> int:
    print(args)
    return sum(args)

print(add(1,2,3))

def greet(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f'{greeting} - {person} {ending}')

greet('Hello', 'Sourav','Sree', ending='!')

def pin_position(**kwargs: int) -> None:
    print(kwargs)

pin_position(x=10, y=20)

def func(*args: str, default: int, **kwargs: int) -> None:
    print(args)
    print(kwargs)
    print(default)

func('a','b', default=20, a=1,b=2)

def func(var_a: str, /, var_b: str) -> None:
    print(var_a)
    print(var_b)

# / -> everything before it should be passed as positional argument.
func('a','b')
# used when we might change the parameter name in the method.

def func(var_a: str, *, var_b: str) -> None:
    print(var_a)
    print(var_b)

# * -> everything after it should be passed as keyword argument.
func('a', var_b='b')

def func(var_a: str, /, var_b: str, *, var_c: str) -> None:
    ...


import sys
from datetime import datetime

def get_response(text: str) -> str:
    lowered: str = text.lower()

    if lowered in ['hello', 'hi', 'hey']:
        return 'Hey there!'
    elif 'how are you' in lowered:
        return "I'm good thanks!"
    elif 'your name' in lowered:
        return 'My name is: Bot :)'
    elif 'time' in lowered:
        current_time: datetime = datetime.now()
        return f"The time is {current_time:%H:%M}"
    elif lowered in ['bye', 'see you', 'goodbye']:
        return 'It was nice talking to you! Bye!'
    else:
        return f'Sorry, I do not understand: "{text}".'

while True:
    user_input: str = input('You: ')
    if user_input == 'exit':
        print('Bot: It was a pleasure talking to you!')
        sys.exit()
    bot_response: str = get_response(user_input)
    print(f'Bot: {bot_response}')


import sys

# total: int = 0
# while True:
#     user_input: str = input('enter number: ')
#     if user_input == '0':
#         print('total: ', total)
#         sys.exit()
#     try:
#         total+=int(user_input)
#     except ValueError:
#         print('Please enter a valid number.')

try:
    result: float = 10/0
    print(result)
except Exception as e:
    print(f'Error: {e}')

print('Done!')


while True:
    try:
        user_input: str = input('enter number: ')
        print(f'10 / {user_input} = { 10 /float(user_input) }')
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("Enter valid number")
    except Exception as e:
        print(f'something went wrong: {e}')

user_input: str = 'asdf'

try:
    result: float = 1/float(user_input)
    print(result)
except ValueError:
    print("you can't use random values" )
except ZeroDivisionError:
    print('dont use zero')
else:
    print('success! there were no exceptions encountered')
finally:
    print('Finally: I am always executed!')


def check_age(age: int) -> bool:
    if age<0:
        raise ValueError('not a valid age')
    elif age>=21:
        print('old enough')
        return True
    else:
        print('you are not old enough')
        return False

check_age(30)

raise Exception('This is a general exception. Instead of this, use something specific.')


while True:
    user_input: str = input('enter number: ')

    try:
        number: float = float(user_input)
        print(number)
    except ValueError:
        print(f'not valid : {user_input}')
    except Exception as e:
        print(f'type: {type(e)}')
        print(f'something went wrong: {e}')

import string

def is_letters_only(text: str) -> None:
    alphabet: str = string.ascii_letters + ' '

    for char in text:
        if char not in alphabet:
            raise ValueError("Only alphabets allowed!")

    print(f"{text} is alphabets only")

def main() -> None:
    while True:
        try:
            user_input: str = input("Enter text: ")
            is_letters_only(user_input)
        except ValueError:
            print("Please only enter English letters...")
        except Exception as e:
            print(f'Something went wrong {e}')

main()

# greetings.py file
from typing import Final

AUTHOR: Final[str] = 'Sourav'
VERSION: Final[int] = 1

def greet(name: str) -> None:
    print(f'Hello, {name}')

# main.py file
import greetings as g
g.greet('Sourav')
print(g.AUTHOR)

from greetings import greet
greet('Sourav')

from greetings import *
# this interferes with other imports. don't use this.
# from math import * -> everything from math will overwrite other module methods
greet('Sourav')
print(AUTHOR)


# connections.py file
import time

def connect() -> None:
    print('connecting...')
    time.sleep(1)
    print('connected')

connect()

# main.py file
import connections
# this runs the method.

connections.connect()
# this runs the method again. so, in total, it's run twice.


# connections.py file
import time

def connect() -> None:
    print('connecting...')
    time.sleep(1)
    print('connected')


if __name__ == '__main__':
    connect()

# main.py file
import connections
# this doesn't run the method which is inside if __name__ == '__main__'.

connections.connect()
# this runs the method just once. So, in total, it runs only once.


# packages
#1. create folder called 'my_package'
#2. create file inside it called __init__.py
# this file converts the folder to package
# this file is run whenever we import the package.
#3. create files internet.py & website.py inside the package.

# main.py file
from my_package import website, internet
# init.py file is run while importing.

internet.connect()
website.load('www.google.com')


# library contains a collection of packages and modules
# example: email is a library. mime is a package inside email.
# package only contains a collections of modules

# module is a book -> specific functionality
# package - section in a library -> multiple books -> groups functionality
# library - contains multiple sections  -> different sections of modules & packages

# if we moved my_package to a folder 'library', then, 'library' will be library
# and my_package will be a package inside the library.


import requests
from requests import Response


def get_response(url: str) -> Response:
    return requests.get(url)

def show_response_info(response: Response) -> None:
    print('Status: ', response.status_code)
    print('Ok: ', response.ok)
    print('Links: ', response.links)
    print('Encoding: ', response.encoding)
    print('Is redirect: ', response.is_redirect)
    print('Is permanent redirect: ', response.is_permanent_redirect)


def main() -> None:
    website: str = 'https://www.indently.io'
    response: Response = get_response(website)
    show_response_info(response)


if __name__ == "__main__":
    main()

# 1 means truth
# 0 means false

print(bool(100))  # True

print(bool([]))  # False
print(bool(None))  # False
my_dict: dict = {}  # False
my_list: list = []  # False
my_tuple: tuple = ()  # False
empty_string: str = ''  # False

users: dict = {1: 'Mario', 2: 'Luigi', 3: 'James'}

if users:
    for k, v in users.items():
        print(k, v, sep=': ')
else:
    print('No data found')


print(.1 + .2 == .3) # False

print(f'.1 + .2 = {.1 + .2}') # 0.30000000000000004

from math import isclose

a: float = 0.999
b: float = 1.000

print(a == b) # False
print(isclose(a,b,abs_tol=.002)) # True. absolute tolerance. it should be greater than difference.
print(isclose(a,b,abs_tol=.001)) # False. absolute tolerance. it should be greater than difference.
# Absolute tolerance (abs_tol) is the maximum allowed absolute difference between a and b
# isclose(a, b, abs_tol=0.002) returns True if |a - b| is at most 0.002.

print(isclose(a,b,rel_tol=.01)) # True. relative tolerance.
# Relative tolerance is the maximum allowed percentage difference (expressed as a fraction)
# isclose(a, b, rel_tol=0.01) returns True if the relative difference is at most 1%.


print(isclose(a,b,abs_tol=1, rel_tol=.01)) # If either one is satisfied, isclose returns True.



number: int = 10

def change_number() -> None:
    number = 100


print(number) # 10
change_number() # global value isn't changed.
print(number) # 10

def change_number1() -> None:
    global number
    number = 100

print(number) # 10
change_number1() # global value is changed as we used global keyword
print(number) # 100

# variables in inner scopes will override the variables in outer scope.
# variables in outer scopes is visible to all inner scopes.
# variables in inner scopes isn't visible to any outer scopes.
# don't add variables in global scopes. it becomes hard to manage.



def outer_func() -> None:
    name: str = ''
    value: int = 0

    def inner_func() -> None:
        name = 'Tom' # new variable is created
        value = 100 # new variable is created

    inner_func()
    print(name, value) # '' , 0 # variables weren't modified by inner_func()

outer_func()

def outer_func1() -> None:
    name: str = ''
    value: int = 0

    def inner_func1() -> None:
        nonlocal name, value
        name = 'Tom' # use existing variable from outer scope
        value = 100 # use existing variable from outer scope

    inner_func1()
    print(name, value) # 'Tom' , 100 # variables were modified by inner_func()

outer_func1()

numbers: list[int] = [1,2,3]
doubled: list[int] = []
for number in numbers:
    doubled.append(number*2)
print(doubled)

doubled_lc: list[int] = [number*2 for number in numbers] # [return_value for_loop]
print(doubled_lc)


names: list[str] = ['Mario', 'James', 'Luigi', 'John']
j_names: list[str] = []

for name in names:
    if name.startswith('J'):
        j_names.append(name)
print(j_names)

j_names_lc: list[str] = [name for name in names if name.startswith('J')] # [return_value for_loop condition]
print(j_names_lc)


numbers: list[int] = [1,2,3,4,6,7,10]
even_numbers: list[int] = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

even_numbers_lc: list[int] = [number for number in numbers if number%2==0]
print(even_numbers_lc)


numbers: list[int] = [1,2,3,4,5,6]
# works on list, tuples & strings.
print(numbers[0:3]) # [inclusive:exclusive] [1,2,3]
print(numbers[3:6]) # [4,5,6]
print(numbers[:3]) # [1,2,3]
print(numbers[3:]) # [4,5,6]
print(numbers[-1]) # 6
print(numbers[0:4:2]) # [1,3]
print(numbers[4:0:-2]) # [5,3]
print(numbers[::2]) # [1,3,5]
print(numbers[::-1]) # [6,5,4,3,2,1]



people: list[str] = ['Anna', 'Bob', 'Chris', 'David', 'Fred']

for person in people:
    print(f' {person} - {people.index(person)}')
    if person == 'Bob':
        print(f'removing : {person}')
        people.remove('Bob')

    # Anna - 0
    # Bob - 1
    # removing: Bob
    # David - 2 -> After removing 'Bob', 'David' moves to position 2, which skips 'Chris'
    # Fred - 3

# Do not modify the list while looping through it.
# Instead, create a new list and append to it the required data.


import sys

def welcome_message() -> None:
    print('welcome')
    print('Enter:')
    print('------------------')
    print('1 - add')
    print('2 - remove')
    print('3 - list')
    print('0 - exit')
    print('------------------')

def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'{item} added')

def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'{item} removed')
    except ValueError:
        print(f'{item} does not exist')

def display(groceries: list[str]) -> None:
    print('___LIST___')
    for index, item in enumerate(groceries):
        print(f'{index+1} : {item.capitalize()}')
    print('_'*10)

def is_an_option(text: str) -> bool:
    return text in ['1','2','3','0']

def main() -> None:
    groceries: list[str] = []

    welcome_message()
    while True:
        user_input: str = input('choose: ').lower()
        if not is_an_option(user_input):
            print('please pick a valid option...')
            continue

        if user_input == '1':
            new_item: str = input('add item: ').lower()
            add_item(new_item, groceries)
        elif user_input == '2':
            item_to_remove: str = input('remove item: ').lower()
            remove_item(item_to_remove, groceries)
        elif user_input == '3':
            display(groceries)
        elif user_input == '0':
            print('Exiting...')
            sys.exit()

if __name__ == '__main__':
    main()


class Car:
    def __init__(self, brand: str, wheels: int) -> None:
        self.brand = brand
        self.wheels = wheels

    def turn_on(self) -> None:
        print(f'turn on {self.brand}')

    def turn_off(self) -> None:
        print(f'turn off {self.brand}')

    def drive(self, km: float) -> None:
        print(f'driving {self.brand} for {km} km')

    def describe(self) -> None:
        print(f'{self.brand} is a car with {self.wheels} wheels')

def main() -> None:
    bmw: Car = Car('BMW', 4)
    bmw.turn_on()
    bmw.drive(10)
    bmw.turn_off()
    bmw.describe()

    print()

    volvo: Car = Car('Volvo', 6)
    volvo.turn_on()
    volvo.drive(11)
    volvo.turn_off()
    volvo.describe()

if __name__ == '__main__':
    main()



class Connection:
    # dunder -> double underscore
    def __init__(self, connection_type: str, cost: float):
        print(f'{connection_type} connection established for {cost}$/h')
        self.connection_type = connection_type
        self.cost = cost

    def close_connection(self):
        print(f'closing {self.connection_type} connection...')

def main() -> None:
    internet: Connection = Connection('Internet', 2)
    satellite: Connection = Connection('Satellite', 20)

    internet.close_connection()
    satellite.close_connection()


if __name__ == '__main__':
    main()


class Fruit:
    def __init__(self, name: str, grams: float):
        self.name = name
        self.grams = grams


    def eat(self):
        print(f'Eating {self.grams}g of {self.name}')


def main():
    apple: Fruit = Fruit('Apple', 25)
    print(apple.name)
    apple.eat()
    banana: Fruit = Fruit('Banana', 10)
    print(banana.name)
    banana.eat()


if __name__ == '__main__':
    main()


class Car:
    SPEED_LIMIT_KM: float = 140  # class attribute. every class will have this

    def __init__(self, brand: str):
        self.brand = brand

    def drive(self, *, speed: float):
        if speed > self.SPEED_LIMIT_KM:
            print(f'Limiter activated. Driving at {self.SPEED_LIMIT_KM}km/h')
        else:
            print(f'Driving at {speed}km/h')


def main():
    toyota: Car = Car('Toyota')
    bmw: Car = Car('BMW')

    toyota.drive(speed=200)  # 140km/h
    bmw.drive(speed=210)  # 140km/h

    Car.SPEED_LIMIT_KM = 99  # class attribute change value for entire class

    toyota.drive(speed=200)  # 99km/h
    bmw.drive(speed=210)  # 99km/h


if __name__ == '__main__':
    main()



from typing import Self

# Dunder methods are double underscore methods.
# They are not supposed to be called directly.
class Book:
    # init called automatically during initialization
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    # called when len(object) is used.
    def __len__(self):
        return self.pages

    # Can't give return type as Book. Hence, using Self.
    def __add__(self, other: Self) -> Self:
        combined_title: str = f'{self.title} & {other.title}'
        combined_pages: int = self.pages + other.pages
        return Book(combined_title, combined_pages)

def main():
    py_daily: Book = Book('Pydaily', 100)
    harry_potter: Book = Book('Harry Potter', 340)

    print(len(py_daily))

    combined_books: Book = py_daily + harry_potter
    print(combined_books.title)
    print(combined_books.pages)


if __name__ == '__main__':
    main()




class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # for showing to user or yourself
    def __str__(self):
        return f'{self.name} : {self.age} years old'

    # more technical -> for developers
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

def main():
    mario: Person = Person('Mario', 27)
    print(mario) # <__main__.Person object at 0x1051ca490>
    # print calls __repr__ method by default
    # if we override using __str__ method, then, it gets printed instead of __repr__:
    # Mario : 27 years old

    print(repr(mario)) # <__main__.Person object at 0x102b7ed90>
    # if we override using __repr__ method, then, it will print:
    # Person(name=Mario, age=27)


if __name__ == '__main__':
    main()



from typing import Self


class Car:
    def __init__(self, brand: str, car_id: int, color: str):
        self.brand = brand
        self.car_id = car_id
        self.color = color

    def __eq__(self, other: Self) -> bool:
        # return self.car_id == other.car_id
        print(self.__dict__) # {'brand': 'BMW', 'car_id': 1, 'color': 'red'}
        print(other.__dict__) # {'brand': 'BMW', 'car_id': 1, 'color': 'red'}
        return self.__dict__ == other.__dict__ # compare all values

def main():
    car1: Car = Car('BMW', 1, 'red')
    car2: Car = Car('BMW', 1, 'red')

    print(car1 == car2) # False -> check if both are same memory location
    # if we override __eq__ dunder method, it will use our method for comparison


if __name__ == '__main__':
    main()


# method is a function defined inside a class.
# function is defined outside class



from random import choice
from datetime import datetime

class ChatBot:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def get_description(self) -> str:
        return f'{self.name} is {self.age} years old'

    def get_response(self, text: str) -> str:
        lowered: str = text.lower()

        if 'hello' in lowered:
            return f'{self.name}: hey there!'
        elif 'bye' in lowered:
            return 'see you'
        elif 'time' in lowered:
            now: datetime = datetime.now()
            return f'{now:%H:%M:%S}'
        else:
            random_responses: list[str] = [
                "i don't know",
                "what?",
                "i don't understand"
            ]
            return choice(random_responses)

    def run(self):
        while True:
            user_input: str = input('you: ')
            if user_input == 'exit':
                print('thanks')
                break

            response: str = self.get_response(user_input)
            print(response)

def main():
    chatbot: ChatBot = ChatBot('Megamind', 26)
    chatbot.get_description()
    chatbot.run()

if __name__ == '__main__':
    main()


class Animal:
    def __init__(self, name: str):
        self.name = name

    def drink(self):
        print(f'{self.name} is drinking')

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def __int__(self, name: str):
        super().__init__(name)

    def bark(self):
        print(f'{self.name} barks!')

    def routine(self):
        self.eat()
        self.drink()
        self.bark()


class Cat(Animal):
    def __int__(self, name: str):
        super().__init__(name)

    def meow(self):
        print(f'{self.name} meow!')

    def routine(self):
        self.eat()
        self.drink()
        self.meow()


def main():
    dog: Dog = Dog('Boomerang')
    cat: Cat = Cat('Snowball')

    dog.bark()
    cat.meow()

if __name__ == '__main__':
    main()



# from typing import override

class Shape:
    def __init__(self, name: str, sides: int):
        self.name = name
        self.sides = sides

    def describe(self):
        print(f'{self.name} has {self.sides} sides')

    def shape_method(self):
        print(f'{self.name}: shape_method()')


class Square(Shape):
    def __init__(self, size: float):
        super().__init__('Square', 4)
        self.size = size

    # @override -> added in python 3.12
    def describe(self):
        print(f'{self.name} with size {self.size}')

class Rectangle(Shape):
    def __init__(self, length: float, height: float):
        super().__init__('Rectangle', 4)
        self.length = length
        self.height = height

    # @override -> added in python 3.12
    def describe(self):
        print(f'{self.name} with {self.height} * {self.length}')

def main():
    square: Square = Square(20)
    square.describe()
    square.shape_method()

    rectangle: Rectangle = Rectangle(15, 10)
    rectangle.describe()
    rectangle.shape_method()

if __name__ == '__main__':
    main()


class Calculator:
    def __init__(self, version: int):
        self.version = version

    @staticmethod
    def add(*numbers: float):
        return sum(numbers)

    def get_version(self):
        return self.version

def main():
    calculator: Calculator = Calculator(version=1)
    print(calculator.add(1,2,3,4))

    print(Calculator.add(1,2,3,4))

if __name__ == '__main__':
    main()




from typing import Self


class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    @classmethod
    def change_limit(cls, new_limit: int):
        cls.LIMITER = new_limit
        # self.LIMITER only changes for single object.
        # cls.LIMITER updates for all objects

    def display_info(self):
        print(f'{self.brand} (max={self.max_speed}, limiter={self.LIMITER})')


def main():
    bmw: Car = Car('BMW', 240)
    toyota: Car = Car('Toyota', 190)

    bmw.display_info()
    toyota.display_info()

    Car.change_limit(150)
    # toyota.change_limit(140) # this will also set limiter for all instances.
    # toyota.LIMITER = 140 # only sets for toyota instance. not for other instances.

    bmw.display_info()
    toyota.display_info()


if __name__ == '__main__':
    main()




from typing import Self


class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    @classmethod
    def change_limit(cls, new_limit: int):
        cls.LIMITER = new_limit
        # self.LIMITER only changes for single object.
        # cls.LIMITER updates for all objects

    @classmethod
    def autogenerate_max_speed(cls, brand: str):
        lowered: str = brand.lower()
        max_speed: int = 200

        if lowered=='toyota':
            max_speed = 270
        elif lowered=='bmw':
            max_speed = 290

        return cls(brand, max_speed)

    def display_info(self):
        print(f'{self.brand} (max={self.max_speed}, limiter={self.LIMITER})')


def main():
    bmw: Car = Car.autogenerate_max_speed('BMW')
    bmw.display_info()

    ferrari: Car = Car.autogenerate_max_speed('Ferrari')
    ferrari.display_info()

if __name__ == '__main__':
    main()


from abc import ABC, abstractmethod

class Appliance(ABC): #AbstractBaseClass
    def __init__(self, brand: str, version_no: int):
        self.brand = brand
        self.version_no = version_no
        self.is_turned_on: bool = False

    @abstractmethod
    def turn_on(self):
        ...

    @abstractmethod
    def turn_off(self):
        ...

class Lamp(Appliance):
    def __init__(self, brand: str, version_no: int):
        super().__init__(brand, version_no)

    def turn_on(self):
        if self.is_turned_on:
            print(f'{self.brand} already turned on')
        else:
            self.is_turned_on = True
            print(f'{self.brand} turned on')

    def turn_off(self):
        if self.is_turned_on:
            self.is_turned_on = False
            print(f'{self.brand} turned off')
        else:
            print(f'{self.brand} already turned off')

class Oven(Appliance):
    def __init__(self, brand: str, version_no: int):
        super().__init__(brand, version_no)

    def turn_on(self):
        # raise NotImplementedError instead of pass, as it gives proper error message
        raise NotImplementedError('Need to add functionality for turn_on()')

    def turn_off(self):
        # raise NotImplementedError instead of pass, as it gives proper error message
        raise NotImplementedError('Need to add functionality for turn_off()')

def main():
    lamp: Lamp = Lamp('Z-Lite', 1)
    lamp.turn_on()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()

    oven: Oven = Oven('Bosch', 2)
    oven.turn_on()
    oven.turn_off()

if __name__ == '__main__':
    main()



class Car:
    __YEAR: int = 2000 # name mangling
    # this cannot be used in subclasses.
    # if we want to use it in subclass, use _YEAR in Car class, instead of __YEAR
    # _YEAR -> tells developer that it should only be used in classes & subclasses.

    def __init__(self, brand: str, fuel_type: str):
        self.__brand = brand # name mangling
        self.__fuel_type = fuel_type # name mangling

        self.var: str = 'red'
        # this breaks the code in Toyota subclass.
        # to fix it, jus tuse self.__var for this variable in Car class.
        # self.__var: str = 'red'

    def drive(self):
        print(f'driving: {self.__brand}')

    def __get_description(self): # name mangling with methods
        print(f'{self.__brand}: {self.__fuel_type}')

    def display_color(self):
        self.__get_description() # mangled names can be accessed easily inside the class
        print(f'{self.__brand} is {self.var.capitalize()}') # this breaks code in Toyota subclass.
        # print(f'{self.__brand} is {self.__var.capitalize()}') # this fixes the AttributeError in Toyota subclass

class Toyota(Car):
    def __init__(self, fuel_type: str):
        super().__init__('Toyota', fuel_type)
        self.var = 100 # has the same name as super class var, which is string.
        # this breaks the code in

    def get_year(self):
        return self.__YEAR # raise AttributeError.
        # if we want to use it in subclass, use _YEAR in Car class.
        # this just tells developer that it should only be used in classes & subclasses.

def main():
    car: Car = Car('Toyota', 'Electric')
    car.drive()

    # name mangling ensure that we use the mangled names only inside the classes.
    # to use it outside, we have to follow the below weird syntax:
    print(car._Car__brand) # Toyota
    # print(car.__get_description()) # raises error. Car has no method
    car._Car__get_description() # Toyota: Electric

    toyota: Toyota = Toyota('Electric')
    toyota.display_color() # AttributeError: 'int' object has no attribute 'capitalize'
    # we defined 'var' as a int in Toyota.
    # it's already used in super class for display_color()
    # To fix this issue, just use __var for the Car class.

if __name__ == '__main__':
    main()



print(True)
print(1,2,True,['a','b'])
print('a','b','c', sep='-', end='.\n') # a-b-c.
print('Bob')
people: list[str] = ['Mario', 'James', 'Hannah']
print(people) # ['Mario', 'James', 'Hannah']
print(*people) # Mario James Hannah
print(*people, sep=', ', end='.\n') # Mario, James, Hannah.



elements: list[str] = ['A', 'B', 'C']

for index, element in enumerate(elements, start=1): # starting value is set as 1
    print(f'{index}: {element}')
    # 1: A
    # 2: B
    # 3: C




a: float = 200.312399
b: float = 18.12132
c: float = 47.12312
result: float = a+b+c
print(result) # 265.55683899999997

rounded: float = round(result, 2) # round to 2 decimal places
print(rounded) # 265.56

print(round(result, 2)) # 265.56
print(round(result, 1)) # 265.6
print(round(result, 0)) # 266.0
print(round(result, -1)) # 270.0 -> round actual number.
print(round(result, -2)) # 300.0


my_range: range = range(1,6)
print(my_range) # range(1, 6) -> range object
print(list(my_range)) # [1, 2, 3, 4, 5]

my_range: range = range(0,10,2)
print(my_range)
print(list(my_range)) # [0, 2, 4, 6, 8]

my_range: range = range(0,-5,-1)
print(my_range)
print(list(my_range)) # [0, -1, -2, -3, -4]

for i in range(3):
    print(i)


numbers: list[int] = [1,2,3,4,5]
print(numbers[2:4]) # [3, 4]

text: str = 'Hello, World!'
first_three: slice = slice(0,3)
print(text[first_three]) # Hel

reverse_slice: slice = slice(None, None, -1) # [::-1]
print(text[reverse_slice]) # !dlroW ,olleH

step_two: slice = slice(None, None, 2) # [::2]
print(text[step_two]) # Hlo ol!


from typing import Any

print(globals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x102585a50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/souravas/Developer/PythonProject/main.py', '__cached__': None, 'Any': typing.Any}
# everything visible in the global space
# if we import everything from math, then, it will pollute the global space
# if function is defined, it will also be present in globals()

def func():
    ...

my_globals: dict[str, Any] = dict(globals()) # create copy of globals
# if we use globals directly, it can create runtime errors if globals() changes while iterating
for k, v in my_globals.items():
    print(f'{k}: {v}')
    # __name__: __main__
    # __doc__: None
    # __package__: None
    # __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x100eb1a50>
    # __spec__: None
    # __annotations__: {'my_globals': dict[str, typing.Any]}
    # __builtins__: <module 'builtins' (built-in)>
    # __file__: /Users/souravas/Developer/PythonProject/main.py
    # __cached__: None
    # Any: typing.Any
    # func: <function func at 0x100ed8720>


print(locals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x104b51a50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/souravas/Developer/PythonProject/main.py', '__cached__': None}
# in the outer scope, locals & globals are same

def add(a: int, b: int):
    result: int = a + b
    print(result)

    print('add() has these locals: ', locals())
    # add() has these locals:  {'a': 1, 'b': 1, 'result': 2}
    print('add() has these globals: ', globals())
    # add() has these globals:  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10488da50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/souravas/Developer/PythonProject/main.py', '__cached__': None, 'add': <function add at 0x1048b4720>}
    # add is also defined in globals() -> we can call add() again from inside add() -> recursion
add(1,1)


wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

if wifi_enabled and has_electricity and has_subscription:
    print('Connected to internet')

requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]
if all(requirements):
    print('Connected to internet')

people_voted: list[int] = [1,1,1,0,1,0,1,1,1,0]
if all(people_voted):
    print('Everyone voted')
else:
    print('Some people did not vote...')

if not all(people_voted):
    print('Someone did not vote...')
else:
    print('Everyone voted!')


people_voted: list[int] = [0,1,0,0,0]

if any(people_voted):
    print('At least 1 person voted')
else:
    print('No one voted!')


number: int = 10
pi: float = 3.14
text: str = 'banana'
my_list: list[int] = [1,2,3]

# actual value is checked in isinstance.
print(isinstance(number, int)) # True
print(isinstance(number, str)) # False
print(isinstance(my_list, list)) # True
print(isinstance(pi, int | float)) # True

class Animal:
    pass

class Cat(Animal):
    pass

print(isinstance(Cat(), Animal)) # True. Cat is an Animal
print(isinstance(Animal(), Cat)) # False. Animal is not a Cat



from difflib import get_close_matches

def get_best_match(user_question: str, knowledge: dict) -> str | None:
    questions: list[str] = [q for q in knowledge] # knowledge.keys() and knowledge are same while iterating
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6) # 1 result. 60 percent match

    if matches:
        return matches[0]
    # returns None by default if no result

def run_chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input('You: ')

        best_match: str | None = get_best_match(user_input, knowledge)
        response: str | None = knowledge.get(best_match)

        if response:
            print(f'Bot: {response}')
        else:
            print(f'Bot: I do not understand...')

def main():
    brain: dict[str, str] = {'hello':'hey there!',
                             'how are you?': 'I am good, thanks!',
                             'what time is it?': 'No clue',
                             'what can you do?': 'I can answer questions!',
                             'ok': 'Great'}
    run_chatbot(knowledge=brain)


if __name__ == '__main__':
    main()



fruit: str = 'apple'
number: int = 10

def fun():
    print("fun() was called!")


print(f'callable(): {callable(fruit)}') # False
# fruit() -> cannot be used as it's not callable

print(f'callable(): {callable(fun)}') # True
# fun() -> can be called with ()

print(f'callable(): {callable(range)}') # True
print(f'callable(): {callable(str)}') # True


if callable(fun):
    fun()
else:
    print('object was not called!')



numbers: list[int] = list(range(1,21))
print(numbers)

def is_even(number: int) -> bool:
    return number%2==0

even_numbers: filter = filter(is_even, numbers)
print(even_numbers) # <filter object at 0x104299a80>
print(list(even_numbers)) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


even_numbers: filter = filter(lambda n: n % 2 == 0, numbers)
print(even_numbers)
print(list(even_numbers)) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

people: list[str] = ['Anna', 'Bob', 'Betty', 'James', 'John']
long_names: filter = filter(lambda name: len(name) > 4, people)
print(list(long_names)) # ['Betty', 'James']

long_names_ls : list[str] = [name for name in people if len(name)>4]
print(long_names_ls) # ['Betty', 'James']

# filter is more memory efficient as it doesn't load everything in memory.
# filter can be useful for loops with large number of values.
# list comprehension is more popular,but loads everything in memory.


numbers: list[int] = [1,2,3,4,5]

def double(number: int) -> int:
    return number*2

doubled: map = map(double, numbers)
print(doubled) # <map object at 0x102d69c90>
print(list(doubled)) # [2, 4, 6, 8, 10]

doubled: map = map(lambda n: n*2, numbers)
print(list(doubled)) # [2, 4, 6, 8, 10]

doubled_ls: list[int] = [number*2 for number in numbers]
print(doubled_ls) # [2, 4, 6, 8, 10]


numbers: list[int] = [1,2,3,4,5]
letters: list[str] = ['a','b','c']

def combine_elements(number:int, letter:str) -> tuple[int,str]:
    return number, letter

combined: map = map(combine_elements, numbers, letters)
print(list(combined)) # [(1, 'a'), (2, 'b'), (3, 'c')]
# stops when the shortest list runs out of elements. 4 & 5 are skipped.

combined: map = map(lambda n, l: (n,l), numbers, letters)
print(list(combined)) # [(1, 'a'), (2, 'b'), (3, 'c')]
# stops when the shortest list runs out of elements. 4 & 5 are skipped.




numbers: list[int] = [1,10,5,3]

sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers) # [1, 3, 5, 10]

people: list[str] = ['Mario', 'James', 'Anna', 'Tom']
sorted_names: list[str] = sorted(people) # ['Anna', 'James', 'Mario']
# sort by ascii value. # A - 65 / a - 97
print(sorted_names)

sorted_names: list[str] = sorted(people, reverse=True)
print(sorted_names) # ['Tom', 'Mario', 'James', 'Anna']

sorted_names: list[str] = sorted(people, key=lambda x: len(x))
print(sorted_names) # ['Tom', 'Anna', 'Mario', 'James']



class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name}={self.weight}kg'

cat: Animal = Animal('Cat', 10)
dog: Animal = Animal('Dog', 5)
kangaroo: Animal = Animal('Kangaroo', 50)

sorted_animals: list[Animal] = sorted([cat, dog, kangaroo], key=lambda animal: animal.weight)
print(sorted_animals) # [Dog=5kg, Cat=10kg, Kangaroo=50kg]

result: int = eval('1+10+100')
print(result)  # 111

x: int = 5
y: int = 10
print(eval('x+y'))  # 15

while True:
    user_input: str = input('enter math: ')  # can do math
    print(eval(user_input))

# be careful while taking user input and executing using eval()
# it can execute any code entered by user.



# eval -> evaluates the code & return something
# exec -> executes the code & doesn't return anything. execute several lines of code.

code: str = """
x: int = 10
y: int = 20
print(x+y)
"""
exec(code) # 30

while True:
    user_input: str = input('Command: ')
    exec(user_input)

# be careful while taking user input and executing using exec()
# it can execute any code entered by user.


numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ['a', 'b', 'c', 'd']
symbols: list[str] = ['!', '$', '&']

zipped: zip = zip(numbers, letters)
print(zipped)  # <zip object at 0x100eb1dc0>
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# zip never goes past the shortest element.
for n, l, s in zip(numbers, letters, symbols):
    print(n, l, s, sep=' : ')

for n, l, s in zip(numbers, letters, symbols, strict=True):  # strict -> raises error if all are not of equal length
    print(n, l, s, sep=' : ')


class User:
    """
    Base class for creating users.
    This is a docstring. If you hover over the module, it will show this docstring.
    """

    def __init__(self, user_id: int):
        self.user_id = user_id

    def show_id(self):
        """prints the user_id as an int"""
        print(self.user_id)


def user_exists(user: User, database: set[User]) -> bool:
    """
    Checks if a user is inside a database.

    :param user: The user to check for
    :param database: The database to check inside
    :return: bool
    """
    return user in database

def main():
    user: User = User(1)
    print(User.__doc__)

main()



var: int = 10

def add(a: int, b: int) -> int:
    return a + b

print(f'{var=}') # var=10
print(f'{add(5,10) = }') # add(5,10) = 15

big_number: float = 123456789
print(f'{big_number:,}') # 123,456,789 -> 1000 digit separator
print(f'{big_number:_}') # 123_456_789 -> 1000 digit separator

big_number: float = 123_456_789 # easier to read
print(big_number) # 123456789

fraction: float = 1234.5678
print(f'{fraction:.2f}') # 1234.57 -> round last 2 decimal places
print(f'{fraction:,.2f}') # 1,234.57 -> round last 2 decimal places & with 1000 digit separator

percent: float = 0.5
print(f'{percent:.2%}') # 50.00% -> round to 2 decimal places.
print(f'{percent:.0%}') # 50% -> round to whole number.

percent: float = 55.5555555555
print(f'{percent:_.3%}') # 5_555.556% -> round to 3 decimal places & with 1000 digit separator

var: str = 'BOB'
print(f'{var:10}: Hello') # occupy 10 spaces left aligned including the var. #BOB       : Hello
print(f'{var:<10}: Hello') # occupy 10 spaces left aligned including the var. #BOB       : Hello
print(f'{var:>10}: Hello') # occupy 10 spaces with right aligned including the var. #       BOB: Hello
print(f'{var:^10}: Hello') # occupy 10 spaces with center aligned including the var. #   BOB    : Hello
print(f'{var:.>10}') # occupy 10 spaces with right aligned including the var. fill empty space with '.' #.......BOB
print(f'{var:.<10}') # occupy 10 spaces with left aligned including the var. fill empty space with '.' #BOB.......
print(f'{var:.^10}') # occupy 10 spaces with center aligned including the var. fill empty space with '.' #...BOB....

numbers: list[int] = [1,100,1_000,10_000]
for number in numbers:
    print(f'{number:_>5}: counting!')
    # ____1: counting!
    # __100: counting!
    # _1000: counting!
    # 10000: counting!

for number in numbers:
    print(f'{number:>5}: counting!')
    #     1: counting!
    #   100: counting!
    #  1000: counting!
    # 10000: counting!

path: str = '\\Users\\sourav\\Documents' # escape \ character
print(path) # \Users\sourav\Documents

path: str = r'\Users\sourav\Documents' # considers as a raw string.
print(path) # \Users\sourav\Documents

user: str = 'Sourav'
path: str = fr'\Users\{user}\Documents' # f string & raw string
print(path) # \Users\Sourav\Documents



def start_program(db: dict[int, str]) -> None:
    assert db, 'Database is empty' # useful for development. not for production as code is already deployed.

    print('Loaded:', db)
    print('Program started.')

def main():
    db1: dict[int,str] = {0:'a'}
    start_program(db=db1)

    db2: dict[int,str] = {}
    start_program(db=db2) # AssertionError: Database is empty


if __name__ == '__main__':
    main()

var: int = 10
assert var > 0, f'{var} is not more than 0'


a, b = 5, 10
print(a,b) # 5 10

a, b = [5, 10]
print(a,b) # 5 10

a,*b = 'abcdef'
print(a,b) # a ['b', 'c', 'd', 'e', 'f']

a,*b, c = 'abcdef'
print(a,b,c) # a ['b', 'c', 'd', 'e'] f

*_, last = 'abdef' # if we only care about any value, we use '_' -> convention for not important
print(last) # f

def add(a: int, b: int):
    print(f'{a+b=}')

numbers: dict[str, int] = {'a':5,'b':10}
# add(5,10)
add(**numbers) # unpacking the dictionary # a+b=15

numbers: list[int] = [1,2,3,4,5]
params: dict[str,str] = {'sep':'-', 'end': '.'}
print(*numbers, **params) # 1-2-3-4-5.



a: int = 200
b: int = 200

print(a==b) # True. a and b are equal.
print(a is b) # True. memory address of a can be equal to b for small values

a: int = 2000
b: int = int('2000')

print(a==b) # False. a and b are equal.
print(a is b) # False. memory address of a is not equal to b for large values
print(f'{id(a)=}') # id(a)=4331661680
print(f'{id(b)=}') # id(b)=4331667248

# for None, we use 'is None' instead of '=='
# None is singleton -> only one instance of None in memory.
# Hence, is None checks is most reliable.
# == checks for equality, meaning it depends on how __eq__ method is implemented for object being compared.
var: int | None = None
if var is None: # condition is true.
    print('there is no var...')
else:
    print(f'var is: {var}')


class Animal:
    ...

cat: Animal = Animal()
dog: Animal = Animal()

print(cat is dog) # False



from dataclasses import dataclass

@dataclass
class Coin:
    name: str
    value: float
    id: str

# class Coin:
#     def __init__(self, name: str, value: float, coin_id: str):
#         self.name = name
#         self.value = value
#         self.coin_id = coin_id # id can't be used as value in normal classes. so, we are using coin_id here.
#         # id can be used in dataclasses
#     def __repr__(self):
#         ...
#     def __eq__(self, other):
#         ...

def main():
    bitcoin: Coin = Coin('Bitcoin', 10_000, 'BTC')
    bitcoin2: Coin = Coin('Bitcoin', 10_000, 'BTC')
    ripple: Coin = Coin('Ripple', 200, 'XRP')

    print(bitcoin) # Coin(name='Bitcoin', value=10000, id='BTC')
    print(ripple) # Coin(name='Ripple', value=200, id='XRP')

    print(bitcoin==ripple) # False -> check values by default.
    print(bitcoin==bitcoin2) # True -> check values by default.

    print(bitcoin.value == ripple.value) # False

if __name__ == '__main__':
    main()



from dataclasses import dataclass, field

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    edible: bool = field(default=True) # default value will be True for this variable
    # default values should be last.
    # for simple values, we can directly use the value:
    # edible: bool = True

    related_fruits: list[str] = field(default_factory=list) # create a new list every time it's called.
    # related_fruits: list[str] = [] # does not create a new list everytime it's called. hence, we have to use field()


def main():
    apple: Fruit = Fruit('Apple', 100, 5)
    print(apple) # Fruit(name='Apple', grams=100, price_per_kg=5, edible=True, related_fruits=[])

    pear: Fruit = Fruit('Pear', 250, 10, related_fruits=['Apple', 'Orange'])
    print(pear) # Fruit(name='Pear', grams=250, price_per_kg=10, edible=True, related_fruits=['Apple', 'Orange'])
    print(pear.related_fruits) # ['Apple', 'Orange']


if __name__ == '__main__':
    main()



from dataclasses import dataclass, field

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    total_price: float = field(init=False) # this will be initialized later
    # we can't initialize it here if it's value depends on other values.

    def __post_init__(self): # called automatically after initialization. only runs once.
        self.total_price = (self.grams/1000)*self.price_per_kg

    def describe(self):
        print(f'{self.grams}g of {self.name} costs ${self.total_price}')

def main():
    apple: Fruit = Fruit('Apple', 1500, 5)
    orange: Fruit = Fruit('Orange', 2500, 10)

    print(apple) # Fruit(name='Apple', grams=1500, price_per_kg=5, total_price=7.5)
    print(orange) # Fruit(name='Orange', grams=2500, price_per_kg=10, total_price=25.0)

    apple.describe() # 1500g of Apple costs $7.5
    orange.describe() # 2500g of Orange costs $25.0

if __name__ == '__main__':
    main()



from dataclasses import dataclass, field, InitVar

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    is_rare: InitVar[bool | None] = None  # is_rare can only be used for initialising our post_init. it can't be used outside.
    total_price: float = field(init=False) # this will be initialized later
    # we can't initialize it here if it's value depends on other values.

    def __post_init__(self, is_rare: bool | None): # called automatically after initialization. only runs once.
        if is_rare:
            self.price_per_kg *= 2
        self.total_price = (self.grams/1000)*self.price_per_kg

    def describe(self):
        print(f'{self.grams}g of {self.name} costs ${self.total_price}')

def main():
    apple: Fruit = Fruit('Apple', 1500, 5)
    orange: Fruit = Fruit('Orange', 2500, 10)
    passion: Fruit = Fruit('Passion', 100, 50, is_rare=True)

    print(apple) # Fruit(name='Apple', grams=1500, price_per_kg=5, total_price=7.5)
    print(orange) # Fruit(name='Orange', grams=2500, price_per_kg=10, total_price=25.0)
    print(passion) # Fruit(name='Passion', grams=100, price_per_kg=100, total_price=10.0)

    apple.describe() # 1500g of Apple costs $7.5
    orange.describe() # 2500g of Orange costs $25.0
    passion.describe() # 100g of Passion costs $10.0 -> price is doubled.



if __name__ == '__main__':
    main()


from dataclasses import dataclass, field, InitVar

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float

    @property # @property makes sure we get the most upto date value each time we use the variable total_price
    def total_price(self):
        # we can treat it as a variable.
        # obj.total_price -> can be called from outside, instead of object.total_price()
        return (self.grams/1000) * self.price_per_kg

    def describe(self):
        print(f'{self.grams}g of {self.name} costs ${self.total_price}')

def main():
    apple: Fruit = Fruit('Apple', 1500, 5)

    print(apple) # Fruit(name='Apple', grams=1500, price_per_kg=5)
    apple.price_per_kg = 20 # this doesn't change total price from __post_init__. now, it's called from @property. hence, value will be updated.
    print(apple) # Fruit(name='Apple', grams=1500, price_per_kg=20)
    apple.describe() # 1500g of Apple costs $30.0
    print(apple.total_price) # 30.0


if __name__ == '__main__':
    main()


from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self):
        self.id = uuid4()

class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None):
        self.author = author

        if notes is None:
            self._notes = [] # _variables shouldn't be used outside class.
        else:
            self._notes = notes

        self.display_instructions()

    @staticmethod
    def display_instructions():
        print('Welcome')
        print('Commands:')
        print('1 - new note')
        print('2 - edit note')
        print('3 - delete note')
        print('4 - display all notes')

    def _add_note(self):
        title: str = input('title: ')
        body: str = input('body: ')

        note: Note = Note(title, body)
        self._notes.append(note)
        print('note added')

    def _edit_note(self):
        print('which note to edit?')
        self._show_notes()

        try:
            note_index: int = int(input('Index: ')) - 1 # convert 1 based index from user input to 0 based index
            current: Note = self._notes[note_index]

            new_title: str = input('new title: ')
            new_body: str = input('new body: ')

            current.title = new_title
            current.body = new_body
            print('note updated')
        except IndexError:
            print('please select a valid note index')
            self._edit_note()
        except ValueError:
            print('index cannot be empty')
            print('Aborting operation')

    def _delete_note(self):
        print('which note to delete?')
        self._show_notes()

        try:
            note_index: int = int(input('Index: ')) - 1  # convert 1 based index from user input to 0 based index
            del self._notes[note_index]
            print('note deleted')
        except IndexError:
            print('please select a valid note index')
            self._delete_note()
        except ValueError:
            print('index cannot be empty')
            print('Aborting operation')

    def _show_notes(self):
        if not self._notes:
            print('no notes')
            return

        for i, note in enumerate(self._notes, start = 1):
            print(f'[{i}] {note.title} : {note.body}')


    def _select_option(self, user_input: str):
        if user_input not in ['1', '2', '3', '4']:
            print('please pick valid option')
            return

        if user_input == '1':
            self._add_note()
        elif user_input == '2':
            self._edit_note()
        elif user_input == '3':
            self._delete_note()
        elif user_input == '4':
            self._show_notes()

    def run_app(self): # only public method in the class
        while True:
            user_input: str = input('You: ')
            self._select_option(user_input)


def main():
    sample_notes: list[Note] = [
        Note(title='Title1', body='Hello there, sourav!'),
        Note(title='Title2', body='More text!'),
    ]
    note_app: NoteApp = NoteApp(author='sourav', notes=sample_notes)
    note_app.run_app()

if __name__ == '__main__':
    main()



import asyncio
from asyncio import Task
from datetime import datetime

async def fetch_data(input_data: int)-> dict:
    print('fetching data')
    start_time: datetime = datetime.now()
    await asyncio.sleep(3)
    end_time: datetime = datetime.now()
    print('data retrieved')
    return {
        'input': input_data,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
        }


async def main():
    task1: Task[dict] = asyncio.create_task(fetch_data(1))
    task2: Task[dict] = asyncio.create_task(fetch_data(2))

    data1: dict = await  task1
    data2: dict = await task2

    print(f'{data1=}')
    print(f'{data2=}')

if __name__=='__main__':
    asyncio.run(main=main())



import asyncio
from asyncio import Task
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int) -> dict:
    print('fetching data')
    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()
    print('data retrieved')
    return {
        'input': input_data,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }


async def main():
    task: Task[dict] = asyncio.create_task(fetch_data(1, delay=3))
    await asyncio.sleep(1)
    print('running other code.')
    data: dict = await task
    print(data)


    task: Task[dict] = asyncio.create_task(fetch_data(2, delay=10))
    await asyncio.sleep(1)
    task.cancel(msg='Took too long') # cancelling task
    await asyncio.sleep(1) # to register that task has been cancelled can task some time. So, we are adding delay here.
    print(task.cancelled()) # True . # if we don't add delay, then, this could be False as task cancellation might not be registered yet.
    try:
        data: dict = await task
        print(data)
    except asyncio.CancelledError as e:
        print('Task was cancelled...')
        print(e)
        print(task.cancelled()) # True . # if we don't add delay, then, this could be False as task cancellation might not be registered yet.


    task: Task[dict] = asyncio.create_task(fetch_data(3, delay=3))
    await asyncio.sleep(1) # task takes 3 seconds. but we are sleeping for only 1 second.
    try:
        data: dict = task.result() # we are not waiting for the task to complete. which will give error.
        print(data)
    except asyncio.InvalidStateError as e:
        print(e) # Result is not set


    task: Task[dict] = asyncio.create_task(fetch_data(4, delay=3))
    print(task.done()) # False
    data: dict = await task # Task is completed here.
    print(data)
    print(task.done()) # True
    if task.done():
        data = task.result() # Only fetch result if task is done


    task: Task[dict] = asyncio.create_task(fetch_data(5, delay=30))
    try:
        data: dict = await asyncio.wait_for(task, timeout=3)
        print(data)
    except asyncio.TimeoutError:
        print('Request took too loong...')

if __name__ == '__main__':
    asyncio.run(main=main())



import asyncio
from asyncio import Task, Future
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int, fails: bool) -> dict:
    print('fetching data')
    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()
    if fails:
        raise Exception('Something went wrong...')

    print('data retrieved')
    return {
        'input': input_data,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }

async def main():
    tasks: Future = asyncio.gather(
        fetch_data(1,delay=1, fails=False),
        fetch_data(2, delay=2, fails=False),
        fetch_data(3, delay=1, fails=True), # this will fail
        return_exceptions=True # if exceptions occur, then return exception instead of failing.
    )
    results: list[dict] = await tasks
    for result in results:
        print(result)
        # {'input': 1, 'start_time': '08:08:06', 'end_time': '08:08:07'}
        # {'input': 2, 'start_time': '08:08:06', 'end_time': '08:08:08'}
        # Something went wrong...

if __name__ == '__main__':
    asyncio.run(main=main())



from datetime import datetime
from asyncio import Future
import asyncio

import requests
from requests import Response

async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time: datetime = datetime.now()

    return {
        'website': url,
        'status': response.status_code,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }

async def main():
    tasks: Future = asyncio.gather(
        check_status('https://bing.com'),
        check_status('https://google.com'),
        check_status('https://apple.com'),
        check_status('https://lol'),
        return_exceptions=True
    )

    results: list[dict] = await tasks
    print(results)
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main=main())



# static type checkers like mypy can be used.
items: list[str] = ['cup', 'apple', True, [1,2,3]] # gives warning for True, [1,2,3]

def fun(default: int = None): # gives warning for default with int type has None value.
    ...


# walrus operator is controversial. can be more difficult to read

def description(numbers: list[int]):
    # n_length: int = len(numbers)
    # n_sum: int = sum(numbers)
    # n_mean: float = n_sum/n_length
    #
    # details: dict = {
    #     'length': n_length,
    #     'sum': n_sum,
    #     'mean': n_mean
    # }
    details: dict = {
        'length': (n_length := len(numbers)),
        'sum': (n_sum := sum(numbers)),
        'mean': (n_mean := n_sum/n_length)
    }


    return details

def main():
    numbers: list[int] = [1,10,5,200,-4,7]
    print(description(numbers))

    print(x := 1 > 0)
    print(x)

    items: dict[int, str] = {1: 'Cup', 2: 'Chair'}
    if item := items.get(3):
        print(f'you have : {item}')
    else:
        print('no item found...')

main()



from typing import Callable

p = lambda x: print(x)

p(10)
p('Hello')

add = lambda a,b: a + b
print(add(5,11))

def use_all(f: Callable, values: list[int]):
    for value in values:
        f(value)

use_all(lambda v: print(f'{v * "X"}'), [2,4,10])
# XX
# XXXX
# XXXXXXXXXX

def multiply_x(value: int):
    print(f'{value * "X"}')

use_all(multiply_x, [2,4,10])
# XX
# XXXX
# XXXXXXXXXX


names: list[str] = ['Bob', 'James', 'Samantha', 'Luigi', 'Joe']
sorted_names: list[str] = sorted(names, key=lambda x: len(x))
print(sorted_names)
# ['Bob', 'Joe', 'James', 'Luigi', 'Samantha']



from typing import Generator

def five_numbers() -> Generator:
    for i in range(1,6):
        yield i

numbers: Generator = five_numbers()
print(next(numbers)) # 1
print(next(numbers)) # 2
print(next(numbers)) # 3
print(list(numbers)) # [4,5]
print(list(numbers)) # []


def huge_data():
    for i in range(1, 100_000_000_000):
        yield i

data: Generator = huge_data() # memory efficient
print(next(data)) # 1
for i in range(200):
    print(next(data))


def generate_vowels() -> Generator:
    vowels: str = 'aeiou'
    for vowel in vowels:
        yield vowel

vowels: Generator = generate_vowels()
try:
    print(next(vowels)) # a
    print(next(vowels)) # e
    print(next(vowels)) # i
    print(next(vowels)) # o
    print(next(vowels)) # u
    print(next(vowels)) # StopIteration error
except StopIteration:
    print('reached the end of iteration')




status: int = 403

match status:
    case 200:
        print('connected')
    case 403:
        print('forbidden')
    case 404:
        print('not found')
    case _: # everything else which is not defined
        print('unknown')

user_input: str = input('enter command: ') # enlarge cat.jpg 20
command: list[str] = user_input.split()
match command:
    case 'find', *images: # find cat.jpg banana.jpg
        print(f'Finding: {images}...')
    case 'enlarge', image, amount: # enlarge cat.jpg 20
        print(f'you enlarged {image} by {amount}x') # you enlarged cat.jpg by 20x
    case 'rename', image, new_name if len(new_name) > 3:
        print(f'{image} was renamed to {new_name}')
    case 'x' | 'delete', *images:
        print(f'deleting: {images}')
    case _:
        print('command not found')



import time
from typing import Callable
from functools import wraps

def get_time(func: Callable) -> Callable:
    """Times how long it takes to execute a function"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time: float = time.perf_counter()

        print(f'Time: {end_time - start_time:.3f}s')

    return wrapper

@get_time
def calculate() -> None:
    """calculate() docstring"""

    print('Calculating')
    for i in range(200_000_000):
        pass
    print('Done')


calculate()
print(calculate.__name__)
print(calculate.__doc__)


import time
from typing import Callable, Any
from functools import wraps

def repeat(number: int) -> Callable:
    """repeat a function call x amount of times"""

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            value: Any = None
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator

@repeat(number=3)
def greet(name: str):
    """a function to greet people"""
    print(f'hello, {name}')


greet('Sourav')



from enum import Enum

class State(Enum):
    OFF: int = 0
    ON: int = 1

state: State = State.OFF


if state == State.ON:
    print('device on')
elif state == State.OFF:
    print('device off')
else:
    print('unknown device state')

class Color(Enum):
    RED: str = 'R'
    GREEN: str = 'G'
    BLUE: str = 'B'

red: Color = Color.RED
print(red) # Color.RED
print(red.value) # R
print(red.name) # RED
print(Color('R')) # Color.RED



from functools import cache

@cache
def fibonacci(n):
    if n<3:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(500))
print(fibonacci.cache_info()) # CacheInfo(hits=497, misses=500, maxsize=None, currsize=500)
fibonacci.cache_clear()
print(fibonacci.cache_info()) # CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)



import time
from functools import cached_property

class DataSet:
    def __init__(self, data: list[float]):
        self._data = data

    def show_data(self):
        print(self._data)

    @cached_property
    def sum(self):
        print('calculating')
        time.sleep(2)
        return sum(self._data)

    @cached_property
    def mean(self):
        print('calculating mean.')
        time.sleep(2)
        return sum(self._data) / len(self._data)

def main():
    ds: DataSet = DataSet([1.5,2.4,10,7])
    ds.show_data()

    while True:
        user_input: str = input('You: ').lower()
        if user_input == 'clear sum':
            del ds.sum
            print('sum cleared')
        elif user_input == 'clear mean':
            del ds.mean
            print('mean cleared')
        elif user_input == 'sum':
            print(ds.sum)
        elif user_input == 'mean':
            print(ds.mean)
        else:
            print('unknown commands..')

main()



import time

class Internet:
    def __init__(self, provider: str):
        self.provider = provider

    def connect(self):
        print(f'{self.provider} connecting.')
        time.sleep(2)
        print(f'{self.provider} connected')

def test_connect():
    print('you are now connected')

def main():
    internet: Internet = Internet('Verizon')
    internet.connect = test_connect # monkey patching.
    internet.connect() # instant response.

main()




from timeit import timeit, repeat

a: str = 'list(range(1000))'
b: str = 'list(range(1000))'

warm_up: float = timeit(stmt=a, number=100_000) # warm up -> makes sure interpreter is running correctly.

a_time: float = timeit(stmt=a, number=100_000)
b_time: float = timeit(stmt=b, number=100_000)

print(f'a: {a_time:.3f}s') # a: 0.643s
print(f'b: {b_time:.3f}s') # b: 0.639s

a: str = 'list(range(1000))'
b: str = 'list(range(1000))'
c: str = 'set(range(1000))'

a_time: list[float] = repeat(stmt=a, repeat=5, number=100_000)
print(a_time) # [0.6400190419954015, 0.6399103330040816, 0.6456580419908278, 0.6451402080128901, 0.6411222080059815]

a_time: float = min(repeat(stmt=a, repeat=5, number=100_000))
b_time: float = min(repeat(stmt=b, repeat=5, number=100_000))
c_time: float = min(repeat(stmt=c, repeat=5, number=100_000))

print(f'a: {a_time:.3f}s') # a: 0.642s
print(f'b: {b_time:.3f}s') # b: 0.642s
print(f'c: {c_time:.3f}s') # c: 1.169s


math_power_time: float = timeit(stmt='math.pow(100,66)', setup='import math')
print(f'math.pow: {math_power_time:.3f}s')

power_time: float = timeit('a**b', setup='a,b=100,66')
print(f'a**b : {power_time:.3f}s')

setup: str = """
import math

a:int = 10
b: int = 3
"""

math_power_time: float = timeit(stmt='math.pow(a, b)', setup=setup)
print(f'math.pow: {math_power_time:.3f}s')

power_time: float = timeit('a**b', setup='a,b=100,66')
print(f'a**b : {power_time:.3f}s')

file_path: str = 'info.txt'

with open(file_path, 'r') as f:
    print(f.read())
    # new file is created.
    # new file is added.
    # new file should be closed.

try:
    with open('random_file_not_exist.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(f'No file path found')

with open(file_path) as f:  # default is read mode
    print(f.read())
    # new file is created.
    # new file is added.
    # new file should be closed.
    print(f.read())  # empty. once everything is read, we can't read again.

with open(file_path) as f:  # default is read mode
    text: str = f.read()  # store in variable if we want to repeat it.
    print(text)  # can be repeated
    print(text)  # can be repeated

with open(file_path) as f:  # default is read mode
    print(f.read(5))  # new f -> only 5 characters are read
    print(f.read(5))  # ile i -> next 5 characters are read

with open(file_path) as f:  # default is read mode
    print(f.readline())  # print adds new line automatically. so, extra new line can be there.
    # new file is created.
    #
    print(f.readline(), end='')  # print new line is removed.
    # new file is added.

with open(file_path) as f:  # default is read mode
    print(f.readline(5), end='')
    print(f.readline(3), end='')
    print(f.readline(), end='')
    # new file is created.

with open(file_path) as f:  # default is read mode
    print(f.readlines())
    # ['new file is created.\n', 'new file is added.\n', 'new file should be closed.']

with open(file_path, 'a') as f:  # default is read mode
    # write single line
    f.write('I am newly added text!\n')  # new line added at the end.

    # write multiple lines
    f.writelines(
        ['eggs\n', 'ham\n', 'spam\n']
    )
    # new file is created.
    # new file is added.
    # new file should be closed.
    # I am newly added text!
    # I am newly added text!
    # eggs
    # ham
    # spam

with open('file_does_not_exist.txt',
          'a') as f:  # if file does not exist, 'a' will create it instead of raising exceptions
    f.writelines('hi')

# write removes all the existing lines
with open('info1.txt', 'w') as txt:
    txt.write('hello\n')
    txt.write('world\n')



import json

file_path: str = 'data.json'

with open(file_path, 'r') as file:
    data: dict = json.load(file) # load -> convert from file
    print(data) # {'name': 'mario', 'age': 33, 'friends': ['Luigi', 'Toad'], 'other_info': None}

my_json: str = '''
{
  "name": "mario",
  "age" : 33,
  "friends": ["Luigi", "Toad"],
  "other_info": null
}
'''
data: dict = json.loads(my_json) # loads -> load string -> convert from string.
print(data)
# {'name': 'mario', 'age': 33, 'friends': ['Luigi', 'Toad'], 'other_info': None}


data: dict = {
    'name': 'Bob', 'age': 43, 'job': None
}

with open('new_json.json', 'w') as file:
    json.dump(data, file) # {"name": "Bob", "age": 43, "job": null} -> adds to file.

json_format: str = json.dumps(data) # returns string of json.
print(json_format) # {"name": "Bob", "age": 43, "job": null}


