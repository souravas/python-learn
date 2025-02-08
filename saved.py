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





