def test_bank(SimpleBank, accounts):
    simple_bank = SimpleBank.deploy({'from': accounts[0]})
    assert simple_bank.getContractBalance() == 0

def test_bank_deposit(SimpleBank, accounts):
    simple_bank = SimpleBank.deploy({'from': accounts[0]})
    simple_bank.deposit({'from': accounts[1], 'value': 100})
    assert simple_bank.getContractBalance() == 100
    assert simple_bank.getBalance(accounts[1],{'from': accounts[1]}) == 100

def test_bank_withdraw(SimpleBank, accounts):
    simple_bank = SimpleBank.deploy({'from': accounts[0]})
    simple_bank.deposit({'from': accounts[1], 'value': 100})
    simple_bank.withdraw(90, {'from': accounts[1]})
    assert simple_bank.getContractBalance() == 10
    assert simple_bank.getBalance(accounts[1],{'from': accounts[1]}) == 10