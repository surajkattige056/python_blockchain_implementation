# python_blockchain_implementation

Description:
-------------
This is an example of a blockchain. The program uses Flask programming to send and receive requests from the user.
A block is mined using proof of work and generating a nonce to while mining a block.
The program also prints the blockchain and also the also checks for the blockchain's validity

Requirements:
-------------
Python =3.6 or above
Flask = 0.12.2 or above

Commands:
---------
1) http://127.0.0.1:5000/mine_block - This will be used to mine the block. Insert JSON headers as similar as shown below
Example json header:
{
    "index": 3,
    "previous_hash": "1ce167b8733883b9d2afc63eeb8f3989e21c25432f084c558ca97d29ec4f5c80",
    "proof": 45293,
    "response": "Congratulations! you just mined a block!",
    "timestamp": "2018-06-19 18:22:07.885042"
}

2) http://127.0.0.1:5000/is_valid - This will be used to check the validity of the blockchain. This will return two values
"True" if the blockchain is valid
"False" if the blockchain is invalid

3) http://127.0.0.1:5000/get_chain - This command will be used to print the blockchain
