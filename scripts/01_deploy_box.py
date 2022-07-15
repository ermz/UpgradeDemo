from scripts.helpful_scripts import get_account
from brownie import network, Box, ProxyAdmin

def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy({"from": account})
    # box is implementation contract
    print(box.retrieve())

    proxy_admin = ProxyAdmin.deploy({"from": account})

    initialized = box.store,1
