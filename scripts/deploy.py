from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    account = accounts[0]
    # Brownie is smart and knows if you are going to make a transaction or call
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)


def main():
    deploy_simple_storage()
