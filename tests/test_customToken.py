# pass -s to the flag to see print statements
import brownie
from brownie import accounts


def test_account_balance():
    balance = accounts[0].balance()
    accounts[0].transfer(accounts[1], "1 ether", gas_price=0)
    assert balance - "1 ether" == accounts[0].balance()

def test_staking(TestableCustomToken):
    token = accounts[0].deploy(TestableCustomToken)
    token.initialize(accounts[0], 1000, 1000000, 0, 1000, 2, TestableCustomToken[0])

    token.transfer(accounts[1], 300)
    token.initializeBalance(accounts[1])
    token.stake(accounts[1], 1)

    assert token.stakeOf(accounts[1]) == 1
    assert token._balances(accounts[1]) == 299

    token.unstake(accounts[1])
    assert token._balances(accounts[1]) == 300

    token.transfer(accounts[2], 200)
    token.initializeBalance(accounts[2])

    token.stake(accounts[2], 10)
    assert token._balances(accounts[2]) == 190
    token.stake(accounts[1], 10)
    assert token._balances(accounts[1]) == 290

    token.unstake(accounts[2])
    assert token._balances(accounts[2]) == 200
    token.unstake(accounts[1])
    assert token._balances(accounts[1]) == 300
