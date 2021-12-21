from brownie import SimpleStorage, accounts, config


def read_contract():
    # Always retrieves the most recent deployment
    simple_storage = SimpleStorage[-1]
    # Go take the index thats one less than the length
    # ABI => Brownie knows what the ABI when you compile it.
    # Address => Brownie already knows the address automatically
    print(simple_storage.retrieve())


def main():
    read_contract()
