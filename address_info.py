from web3 import Web3


class ContractAddressInfo:
    def __init__(self, host, address):
        self._w3 = Web3(Web3.HTTPProvider(host))
        self._validate_connection()
        self._begin_block = 0
        self._end_block = self._w3.eth.blockNumber
        self._address = address
        self._validate_address_format()
        self._address = self._w3.toChecksumAddress(self._address)
        self._validate_exists_address()

    def get_info(self):
        block_number = self._get_block(self._begin_block, self._end_block)
        receipt = self._get_receipt(self._get_transactions(block_number))
        if (receipt is None):
            raise Exception("contract address info doesn't found")
        return self._format_receipt(receipt)

    def _format_receipt(self, receipt):
        return {
            'blockHash': Web3.toHex(receipt['blockHash']),
            'transactionHash': Web3.toHex(receipt['transactionHash'])
        }

    def _validate_connection(self):
        if (not self._w3.isConnected()):
            raise Exception('no connection with host, please try again')

    def _validate_address_format(self):
        if (not self._w3.isAddress(self._address)):
            raise Exception('address is not valid, please try again')

    def _validate_exists_address(self):
        code = self._get_code(self._end_block)
        if (self._validate_address_not_found(code)):
            raise Exception('address not found, please try again')

    def _get_block(self, begin_block, end_block):
        position = int((begin_block + end_block) / 2)
        if (self._validate_address_not_found(self._get_code(position))):
            return self._get_block(position, end_block)
        else:
            code = self._get_code(position-1)
            if (self._validate_address_not_found(code)):
                return position
            else:
                return self._get_block(begin_block, position)

    def _get_code(self, position):
        return self._w3.eth.getCode(self._address, position)

    def _validate_address_not_found(self, code):
        return self._w3.toInt(code) == 0

    def _get_transactions(self, block_number):
        block = self._w3.eth.getBlock(block_identifier=block_number)
        return block.transactions

    def _get_receipt(self, transactions):
        for tx in transactions:
            receipt = self._w3.eth.getTransactionReceipt(tx)
            address_condition = receipt['contractAddress'] == self._address
            to_condition = receipt['to'] is None
            if (address_condition and to_condition):
                return receipt
        return None
