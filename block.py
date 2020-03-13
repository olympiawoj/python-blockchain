
import time 

class Block: 
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp 
        self.last_hash = last_hash 
        self.hash = hash
        self.data = data 

    def __repr__(self):
        '''
        String representation of the Block class
        '''
        return ('Block('
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash},'
            f'data: {self.data})')
    
    @staticmethod 
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data
        """
        timestamp = time.time_ns() #returns unique num based on counting num of nanoseconds since jan 1 1970
        last_hash = last_block.hash #found by looking at hash of last block
        hash = f'{timestamp}-{last_hash}' #temp implementation of hash
        
        return Block(timestamp, last_hash, hash, data)
    
    @staticmethod 
    def genesis():
        """
        Generate the genesis block, hard coded w/ data as empty list
        """
        return Block(1, 'genesis_last_hash', "genesis_hash", [])


def main():
    # block = Block('foo')
    # print(block)
    # print(f'block.py__name__: {__name__}')

    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == "__main__":
    main()
