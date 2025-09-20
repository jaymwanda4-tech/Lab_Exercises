name = input("Hello, what is your name?")
print(f"Hello, {name}!")

birth_year = int(input("What year were you born? "))

from datetime import datetime
current_year = datetime.now().year


age = current_year - birth_year


print(f"{name}, you are {age} years old.")
