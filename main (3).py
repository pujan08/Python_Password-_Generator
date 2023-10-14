#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_count=len(letters)
numbers_count=len(numbers)
symbols_count=len(symbols)

answer=''
if nr_letters<=letter_count:
  
  for gen_letter in range(1,nr_letters+1):
    ans_letter=random.choice(letters)
    answer+=ans_letter
else:
  print("you enter a wrong number for letters")

if nr_symbols<=symbols_count:
  for gen_symbol in range(1,nr_symbols+1):
    ans_symbols=random.choice(symbols)
    answer+=ans_symbols
else:
  print("you enter a wrong number for symbols")

if nr_numbers<=numbers_count:
  for gen_number in range(1,nr_numbers+1):
    ans_number=random.choice(numbers)
    answer+=ans_number
else:
  print("you enter a wrong number for numbers")
  

print(f"your password is:{answer}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordlist=[]
if nr_letters<=letter_count:
  for gen_letter in range(1,nr_letters+1):
    ans_letter=random.choice(letters)
    passwordlist.append(ans_letter)
else:
  print("you enter a wrong number for letters")

if nr_symbols<=symbols_count:
  for gen_symbol in range(1,nr_symbols+1):
    ans_symbols=random.choice(symbols)
    passwordlist.append(ans_symbols)
else:
  print("you enter a wrong number for symbols")

if nr_numbers<=numbers_count:
  for gen_number in range(1,nr_numbers+1):
    ans_number=random.choice(numbers)
    passwordlist.append(ans_number)
else:
  print("you enter a wrong number for numbers")
  
random.shuffle(passwordlist)
hardanswer=''
for password in passwordlist:
  hardanswer+=password

print(f"your random password is: {hardanswer} ")



