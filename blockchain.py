class Block: 
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, data):
        self.data = data 
    def __repr__(self):
        return f'Block - data: {self.data}'

class Blockchain: 
    """
    Blockchain: a public ledger of transactions
    Implemented as a list of blocks - data set of transactions
    """

    def __init__(self):
        self.chain = [] # list of block items

    #override default behavior of print by implementing repr method, this becomes the official string representation of the blockchain class
    def __repr__(self):
        return f"Blockchain: {self.chain}"
        
    def add_block(self, data):
        self.chain.append(Block(data)) #make instance of block and append to chain

#make instance of Blockchain
blockchain = Blockchain()
# add blocks of data
blockchain.add_block("one")
blockchain.add_block("two")

#output is memory address ofblockchain object we created, under hood python gives every object it's own address that way it can keep track of your object as it executes your code
print(blockchain)


