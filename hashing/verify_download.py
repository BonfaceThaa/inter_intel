import hashlib


def verify_download(file_path, provided_hash):
    '''
    Function to verify file downloaded correctly
    :param file_path: path of downloaded file
    :param provided_hash: the hash of
    :return:
    '''
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            file_hash.update(data)
    return file_hash.hexdigest() == provided_hash


if __name__ == '__main__':
    verify_download('../data/commandr-1.6.0.tar.gz', 'e3f1ccef330e216349c550a54576350e')