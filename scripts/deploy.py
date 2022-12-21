from brownie import SimpleBank, accounts
def main():
    account = accounts.load('main')
    SimpleBank.deploy({'from': account})