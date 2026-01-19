import my_module

my_module.greeting("Bonny")

my_module.person1["name"] = "Bonny"
my_module.person1["age"] = 25
my_module.person1["country"] = "KENYA"

print(f"Name: {my_module.person1['name']}, Age: {my_module.person1['age']}, Country: {my_module.person1['country']}")

#Python built-in modules
import math
import datetime
import platform
print(f"Square root of 16 is: {math.sqrt(16)}")
print(f"Current date and time: {datetime.datetime.now()}")
print(f"Platform information: {platform.platform()}")


my_Datetime = dir(datetime)
print(f"Available attributes and methods in datetime module: {my_Datetime}")

from my_module import person1

print(f"Imported person1 age from my_module is: {person1 ['age']}")

today = datetime.datetime
print(f"Today's date is: {today.now().date()}")
