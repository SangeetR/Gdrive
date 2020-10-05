import hashlib

with open("Download\Friends - [7x11] - The One with All the Cheesecakes.mkv", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.digest())
print(file_hash.hexdigest())
9ad8881bcbc70a68c9e7b3986fce0ffc
9ad8881bcbc70a68c9e7b3986fce0ffc