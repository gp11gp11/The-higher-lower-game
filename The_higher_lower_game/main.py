from art import logo,vs
from game_data import data
from replit import clear
from random import randint #or can use choice
def print_Account(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  print(f"{account_name},{account_description},from {account_country}")

#display art
print(logo)
count = 0
flag = True
while flag:
  #Generate a random account from the game_data
  account_1 = data[randint(0,49)] 
  account_2 = data[randint(0,49)]
  if account_1==account_2:
    account_2 = data[randint(0,49)]
  print("A:")
  print_Account(account_1)
  print(f"follower count {account_1['follower_count']}")
  print(vs)
  print("B:")
  print_Account(account_2)
  
  #ask user to guess
  
  guess = input("What is your guess?Who has more followers?type A or B")
  #check user guess is correct or not
  account1_Follower = account_1["follower_count"]
  account2_Follower = account_2["follower_count"]
  if account1_Follower > account2_Follower:
    a_Greater = True
  else:
    a_Greater = False
  clear() 
  if guess== "A" and a_Greater == True:
    print("guessed correctly")
    count+=1
  elif guess == "B" and a_Greater == False:
    print("guessed correctly")
    count+=1
  else: 
    print("wrong guess")
    flag = False
 
  print(f"A:{account1_Follower}\nB:{account2_Follower}")
  
print(f"your score is {count}")
  
  
 