import random

cookies=[1,2,3]
name = input("\nPlease enter your name: ")
print(f"\nHere comes your fortune, Mr.{name}")
s = random.choice(cookies)
if s == 1 :
    print("\nToday will be a lucky day")
elif s == 2 :
    print("\nYou will meet someone new and interesting")
else :
    print("\nWatch out for obstacles in your path")
print(f"\nWelcome Mr.{name}")