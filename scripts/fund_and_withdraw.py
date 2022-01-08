# in test we want to work independtly without ganache or other network
from scripts.helpful_scripts import get_account
from brownie import FundMe


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    tx = fund_me.fund({"from": account, "value": 2500000})
    tx.wait(1)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
