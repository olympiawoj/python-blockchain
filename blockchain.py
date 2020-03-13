from block import Block

class Blockchain: 
    """
    Blockchain: a public ledger of transactions
    Implemented as a list of blocks - data set of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()] # list of block items

    #override default behavior of print by implementing repr method, this becomes the official string representation of the blockchain class
    def __repr__(self):
        return f"Blockchain: {self.chain}"
        
    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data)) #make instance of block and append to chain

def main():
    #make instance of Blockchain
    blockchain = Blockchain()
    # add blocks of data
    blockchain.add_block("one")
    blockchain.add_block("two")

    #output is memory address ofblockchain object we created, under hood python gives every object it's own address that way it can keep track of your object as it executes your code
    print(blockchain)


    print(f'blockchain.py__name__: {__name__}')


if __name__ == "__main__":
    main()