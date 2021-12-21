from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # This works ONLY for local Ganache chains.
    account = get_account()
    # Brownie is smart and knows if you are going to make a transaction or call
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
