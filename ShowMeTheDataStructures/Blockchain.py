import datetime
import hashlib

class Node:
    def __init__(self, block, previous = None):
        self.block = block
        self.previous = None

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        previous_hash = None
        if self.tail:
            previous_hash = self.tail.block.hash

        block = Block(data, previous_hash)

        node = Node(block,  self.tail)
        if self.head == None:
            self.head = node
        else:
            block.previous = self.tail
            block.previous_hash = self.tail.block.hash

        self.tail = node

class Block:
    def __init__(self, data, previous_hash = None):
      self.timestamp = datetime.datetime.utcnow()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

print('*** Test Blockchain ***')

chain = BlockChain()

chain.add_block("some data")
assert chain.tail == chain.head, "There should be one block in the chain, which is head and tail"
assert chain.tail.block.previous_hash == None, "There should be one block in the chain, without a previous hash"
first_block_hash = chain.tail.block.hash

chain.add_block("more data")
assert chain.tail != chain.head, "There should be two blocks in the chain - head and tail"
assert chain.tail.block.previous_hash != None, "The block should have a previous hash"
second_block_hash = chain.tail.block.hash
second_block_prev_hash = chain.tail.block.hash
assert first_block_hash == second_block_prev_hash, "The second block previous hash should correspond to first block's hash"
assert second_block_hash != second_block_prev_hash, "Hash and previous hash should be different"

print('*** Success ***')
