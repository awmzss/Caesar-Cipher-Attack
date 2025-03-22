# Caesar Cipher Brute-Force Attack

This Python script performs a brute-force attack on text encrypted using the Caesar cipher. It systematically tries all 26 possible keys, evaluates the likelihood of each decryption being correct by checking word validity against the Oxford Learners' Dictionary, and presents the user with the top-scoring possibilities.

## Prerequisites
Ensure you have the following dependencies installed:
```sh
pip install requests beautifulsoup4
```

## Features
- Automatically tries all 26 shift keys.
- Assigns a score based on the number of valid English words in the decrypted text.
- Fetches word existence from the Oxford Learners' Dictionary.
- Uses a priority queue (heap) to efficiently rank the best decryption results.
- Allows the user to specify the number of top-ranked outputs to display.

## Usage
- Run the script:
```sh
python caesar_bruteforce.py
```
- Enter the encrypted text when prompted.
- Specify how many of the top-ranked decrypted texts you want to see.
- The script will output the most likely plaintext versions.
