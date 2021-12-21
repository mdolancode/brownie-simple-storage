from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)


def main():
    deploy_simple_storage()
