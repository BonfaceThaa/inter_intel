# Hashing
This is process of transforming a string of characters into a key or value that represents the original string in a different manner. A good hash function should have the following properties:
1.Efficiently computable
2.Uniformly distribute keys
Some of the popular use cases for hashing include hashing values before they are stored in the database. This technique can also be used to hash values and index them for faster retrieval from a database. MD5 and SHA(secure Hash Algorithm) are the most popular hashing algorithms that generate short values called digests. 

## Hashing passwords
Storing passwords in plain text is highly discouraged even for very simple applications. The best practice is to storing the hashed value and comparing it with what the user provides. Subsequently, if the two passwords match it means the passwords are the same and the user is authenticated. Storing password with salt is even more encouraged. The salt can be a random string that is joined with the password and hashed before storing the password. The string is generally random which ensures that even passwords of similar nature generate different hashes.

## Hashlib
The hashlib python module implements an interface to secure hash and digest algorithms. The module allows for randomized hashing that protects a system against collision attacks. The various functions of the module take an argument convert it to a binary form and convert it to a fixed length sequence.

## Creating a Python hashing function
Python3 has standard hashing module in-built. This allows  us to create the hashing function without import third party libraries. The `salt_hashing.py` has two main functions. The `hash_pass` function receives the password as an argument and generates a random salt before combining it with the password and hashing. The salt is encoded in ASCII to contain only 0-9 and alphabet letters only while the password is encoded in utf-8 so that it contain different types of characters.  Lastly, the function returns the hash and the salt string.

The other function (`test_hass_pass`) tests whether the provide password is okay or not. Basically, this function accepts the provided password, extracts the salt, counter checks the stored value with the hashing of the provided password plus the salt. Finally, the original hash is compared to the new hash via the assertion method. This is what that actually raises the error in the script.

## Running the script
To run the script, change directory to the hashing folder and use the following command:
`python salt_hashing.py`

Next, run the test script using the following command:
`python test_soap.py`

### Areas of improvement
Even though the use-case applied is simple, the script can be improved in the following ways:
1. Adding clear testing functions.
2. Persisting the hash generated
3. Providing a friendlier interface to interact with the program.