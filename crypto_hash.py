import json

import hashlib

def crypto_hash(data):
    """
    Return a sha-256 hash of the given data
    """
    #json.dumps dumps data into a string representation
    stringified_data = json.dumps(data)
    return hashlib.sha256(stringified_data .encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('2'): {crypto_hash(2)}")


#add if check to see if the name value is main
#if we're directly executing this file, call main method
if __name__ == '__main__':
    main()