import hashlib
import json
import datetime


class Block:
    def __init__(self, timestamp, data, index=0, previous_hash=' '):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previuos_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(str(self.index) + self.previuos_hash + self.timestamp
                              + json.dumps(self.data).hexdigest())

    def print_block(self):
        print("index - ", self.index)
        print("timestamp - ", self.timestamp)
        print("data - ", self.data)
        print("previous hash - ", self.previuos_hash)
        print("current hash - ", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block(datetime.datetime.now(), "Genesis block", 0, "0")

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_bock(self, new_block):
        new_block.index = self.get_latest_block().index + 1
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previuos_hash != previous_block.hash:
                return False
        return True

    def print_blockchain(self):
        for i in self.chain:
            i.print_block()

