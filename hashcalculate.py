import hashlib

with open("Download/fg-01.bin", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.digest())
md5 = file_hash.hexdigest()
print(md5)
inp = input("Enter Hash")
if str(md5) == str(inp):
    print("Congo $$$$$$$ It's a match")
else:
    print("Better Luck Next Time")