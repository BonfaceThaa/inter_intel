import os
import hashlib, binascii


def hash_pass(password):
    '''
    Function for hashing passwords before storage
    :param password:
    :return: pass_hash
    '''
    salt_text = hashlib.sha3_256(os.urandom(60)).hexdigest().encode('ascii')
    pass_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt_text, 100000)
    pass_hash = binascii.hexlify(pass_hash)
    return (salt_text + pass_hash).decode('ascii')


def test_hash_pass(password, test_pass):
    '''
    Test if hash_pass function works as expected
    :param password:
    :param test_pass:
    :return:
    '''
    salt_text = password[:64]
    passw = password[64:]
    pass_hash = hashlib.pbkdf2_hmac('sha512', test_pass.encode('utf-8'), salt_text.encode('ascii'), 100000)
    pass_hash = binascii.hexlify(pass_hash).decode('ascii')
    assert passw == pass_hash


if __name__ == '__main__':
    pass_text = 'testpass2021'
    original_pass = hash_pass(pass_text)
    # Test with same password
    test_hash_pass(original_pass, pass_text)
    # Test with wrong password
    test_hash_pass(original_pass, 'testnotpass')
