import hashlib


def calhash(file_path,md5check):
    # file_path = str(input("Please Enter Full path of file "))
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    print(file_hash.digest())
    md5 = file_hash.hexdigest()
    print(md5)
    # inp = input("Enter Hash")
    if str(md5) == str(md5check):
        print("Congo $$$$$$$ It's a match")
    else:
        print("Better Luck Next Time")


# calhash('Download\Mirzapur.S02EP07.720p.HEVC.AMZN.WEB-DL.DDP2.0.H.265-RONIN.mkv',"a39ba97b51f39b51113005e1937e8b2b")