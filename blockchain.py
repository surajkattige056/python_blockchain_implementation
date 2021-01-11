# -*- coding: utf-8 -*-
#Module 1 - Creating a Blockchain
"""
Created on Thu Jun 14 12:28:32 2018

@author: suraj
"""
#To be installed:
#Flask==0.12.2: pip install Flask==0.12.2
#Postman HTTP Client: https://www.getpostman.com/
import hashlib
import datetime
import json
from flask import Flask, jsonify
import random

# Part 1 - Building a Blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0') #Previous block is 0 because it is a genesis block

    def create_block(self, proof, previous_hash):
        #Block in the blockchain will have index, timestamp (date when the block was mined), proof of work, and the hash of the previous block
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block) #Appending the block to the blockchain
        return block

    def get_previous_block(self):
        return self.chain[-1] # -1 gives the last block in the blockchain

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            #Checking if the hash matches the target requirement of the blockchains
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        #json.dumps are used to convert the block to string
        encoded_block = json.dumps(block, sort_keys=True).encode() #sort keys are used to sort the keys in dictionary before converting to string
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]

            #If the previous hash in the block is not equal to the hash of the previous block, return false
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            #Check if the hash of the block satisfies the target requirement of the blockchain
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1

        return True

#Part 2 - Mining our blockchain

# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

#Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'response': 'Congratulations! you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/is_valid', methods = ['GET'])
def is_valid():
    result = blockchain.is_chain_valid(blockchain.chain)
    if result is False:
        response = {'message':'This blockchain is not valid! We have a problem in the blockchain.'}
    else:
        response = {'message':'This blockchain is valid!'}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    


