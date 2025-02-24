#import modules
import random

#cerating a global fixeed variable for maximum lines that can be bet on
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# creating a dictionary to store the symbols and their count in the machine

symbol_count = {
   "7" : 2,
   "🍒" : 4,
   "💎" : 6,
   "💰" : 8
}

# create dictionary for the winning prize of each stybol
symbol_value = {
   "7" : 7,
   "🍒" : 5,
   "💎" : 3,
   "💰" : 2
}

# create a function to check the winning 
def checkWinnings(columns , lines , bet , values):   
#set variable for winninng
   winnings = 0 
   winning_lines = []
# for loop iterating through each line 
   for line in range(lines):
# variable symbol to store the first symbol at every column at given line
      symbol = columns[0][line]
# for loop to iterate through the elements of the column
      for column in columns:
# create variable symbolcheck to store each column elment
         symbolCheck = column[line]
# if condition to compare symbol and symbol check
         if symbol != symbolCheck:
            break 
      
      else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

   return winnings , winning_lines

# creating a function to create columns and rows in the slot machine
def get_slotSpin(rows , cols , symbols): # here symbols is a dictionary which is passed as an argument
   all_symbols = [] #creating list to store all the symbols
   for symbol , symbol_count in symbols.items():
      for _  in range(symbol_count):
         all_symbols.append(symbol)

   columns = [] 
   for _ in range(cols):
       column = []
       current_symbols = all_symbols[:] # creating copy of symbols so that we can select from copy where already selected symbols are removes and : is used to create copy
       for _ in range(rows):
         value = random.choice(current_symbols)
         current_symbols.remove(value)
         column.append(value)

       columns.append(column)

   return columns

#creating a function to transpose the matrix 

def print_slotMachine(columns) :
   for row in range(len(columns[0])): # we add 0 because this ensures there is atleast one column and herr we are basically traversing throught the elemengts of the columns
      for i , column in enumerate(columns): # enumartes gives us the index we are doing it beecause we dont wanna print | at the end 
         if i != len(columns) - 1:
            print(column[row] , end = "|") # end is basically like /n
         else:
            print(column[row] , end = " ")
            
      print() # brings us to next line


#creating a function to collect user deposit as input
def deposit():
    while True:
        amount = input("enter deposit amount ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break 
            else:
                print("please enter amount greater than ₹0")
        else:
            print("please eneter valid amount")
    return amount


#create a function for getting the input from user for the number of lines they wanna bet on
def get_lines():
 while True:
    lines = input("enter number of betting lines on (1-" + str(MAX_LINES)+ ")? ")
    if lines.isdigit():
       lines = int(lines)
       if 1 <= lines <= MAX_LINES :
          break
       else:
          print("enter minimum one line")
    else:
       print("enter valid number of lines")
 return lines

#creating a function to get amount being bet on each line 
def get_bet():
   while True:
      amount = input("enter each line betting amount ₹")
      if amount.isdigit():
         amount = int(amount)
         if MAX_BET >= amount >= MIN_BET:
            break
         else:
            print(f"amount must be between ₹{MIN_BET} - ₹{MAX_BET}")
      else:
         print("enter valid amount")
   return amount


def game(balance):
   lines = get_lines()
   while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
         print(f"you do not have enough balance , your curret balance is only ₹{balance}")
      else:
         break
   print(f"you are betting ₹{bet} on {lines} lines. Total bet = ₹{total_bet}")
    
   slot = get_slotSpin(ROWS , COLS , symbol_count)
   print_slotMachine(slot)
   winnings ,winning_lines  = checkWinnings(slot , lines , bet , symbol_value )
   print(f"you won ₹{winnings}.")
   print(f"you won on lines", *winning_lines)
   return winnings - total_bet
    

# creating a main function
def main():
    balance = deposit()
    while True:
      print(f"current balance is ₹{balance}")
      answer = input("press enter to play (q to quit)")
      if answer == "q":
         break 
      balance += game(balance)
    print(f"you are left with balance {balance}")


    
   

main()