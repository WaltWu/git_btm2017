import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    with open(client_filename,'a') as file:
        file.write(client_name+"\n")
      
def add_transaction(debtor, creditor, amount):
    pass
        
def get_clients():
    pass

def get_transactions():
    transactions_list = []
    with open(transaction_filename,'r') as file:
        for line in file:
            transactions_list.append(line.split(" "))
        
    return transactions_list