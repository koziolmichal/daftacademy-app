import hashlib
import encodings

def dehash(password: str):
    h = hashlib.sha512()
    h.update(bytes(password, encodings.normalize_encoding('utf8')))
    return h.hexdigest()