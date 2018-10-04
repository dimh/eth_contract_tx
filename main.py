import argparse

from address_info import ContractAddressInfo

parser = argparse.ArgumentParser(
    description="Get contract address's block and transaction hashes")
parser.add_argument('contract_address', help='contract address')
parser.add_argument('--host', required=True, help='web3 host domain')

args = parser.parse_args()

address = args.contract_address
host = args.host

try:
    address_info = ContractAddressInfo(host, address)
    receipt = address_info.get_info()
    print(f"Block Hash: { receipt['blockHash'] }")
    print(f"Transaction Hash: { receipt['transactionHash'] }")
except Exception as err:
    print(f"ERROR: {err}")
