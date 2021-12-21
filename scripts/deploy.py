from brownie import accounts
import os


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    # account = accounts[0]
    # print(account)

    # This works for encrypted Private Keys.
    # account = accounts.load("freecodecamp-account")
    # print(account)

    # This works for env varibales and yaml.
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)


def main():
    deploy_simple_storage()
