import hashlib

with open("Friends - [7x08] - The One Where Chandler Doesn't Like Dogs.mkv", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.digest())
print(file_hash.hexdigest())