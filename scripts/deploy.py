from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    account = accounts[0]
    # Brownie is smart and knows if you are going to make a transaction or call
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def main():
    deploy_simple_storage()
