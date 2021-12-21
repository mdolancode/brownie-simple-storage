from brownie import accounts, config


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    # account = accounts[0]
    # print(account)

    # This works for encrypted Private Keys.
    # account = accounts.load("freecodecamp-account")
    # print(account)

    # This works for env varibales and yaml.
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
