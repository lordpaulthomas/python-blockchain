# Initializing our blockchain list
blockchain = []

def get_last_blockchain_value():
  """ Returns the last value of the current location """
  if len(blockchain) < 1:
      return None
  return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
  """ Append a new value as well as the last blockchain value to the blockchain 
  Arugments: 
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transaction (default [1]).
  """
  if last_transaction == None:
      last_transaction = [1]
  blockchain.append([last_transaction, transaction_amount])
    

def get_transaction_value():
    """ Returns the input of the user ( a new transaction amount) as a float """
    return float(input('Your transaction amount please: ')) 

def get_user_choice():
  user_input = input("Your choice: ")
  return user_input

def print_blockchain_elements():
  for block in blockchain:
      print('Outputting Block')
      print(block)
# Get the first transactioninput and add th evalue to the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

while True:
  print("Please choose: ")
  print("1: Add a new transaction")
  print('2: Output the blockchain blocks')
  print('3: Quit')
  user_choice = get_user_choice()
  if user_choice == 1:
    tx_amount= get_transaction_value()
    add_transaction(tx_amount, get_last_blockchain_value())
  elif user_choice == 2:
    print_blockchain_elements()
  elif user_choice == 3:
    break
  else:  
    print('Input was invalid, please pick a value on the list!')
  print('Choice registered')  

print('Done!')