import zipfile

zip_file = "protected.zip" # this is the zip file that you want to crack.
wordlist = "rockyou.txt"

with zipfile.ZipFile(zip_file, 'r') as z:
    with open(wordlist, 'r', encoding="latin-1") as f:
        for password in f:
            try:
                z.extractall(pwd=password.strip().encode())
                print(f"Password found: {password}")
                break
            except:
                pass
