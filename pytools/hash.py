import hashlib

def hash_digest(obj):
    return hashlib.sha224(obj).hexdigest()
