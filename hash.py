import hashlib

choice = input("1. Hash a file\n2. Enter Text to hash\n3. check file integrity\n4. exit\nEnter your choice: ")

if choice == "1":
    hasher = input("Choose the hash algorithm (SHA256, SHA512, SHA1, md5): ")

    if hasher == "SHA256":
        try:
            file_path = input("Enter the file path: ")
            print(f"using {hasher} algorithm")
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                print("hash value is :", file_hash)
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "SHA512":
        try:
            file_path = input("Enter the file path: ")
            print(f"using {hasher} algorithm")
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha512(f.read()).hexdigest()
                print("hash value is :", file_hash)

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "SHA1":
        try:
            file_path = input("Enter the file name: ")
            print(f"using {hasher} algorithm")
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha1(f.read()).hexdigest()
                print("hash value is :", file_hash)

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "md5":
        try:
            file_path = input("Enter the file name: ")
            print(f"using {hasher} algorithm")
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                print("hash value is :", file_hash)

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    else:
        print("Invalid hash algorithm. Please choose either SHA256, SHA512, SHA1 or md5.")

if choice == "2":

    hasher = input("Choose the hash algorithm (SHA256, SHA512, SHA1, md5): ")

    if hasher == "SHA256":
        text = input("Enter the text to hash: ")
        print(f"using {hasher} algorithm")
        text_hash = hashlib.sha256(text.encode()).hexdigest()
        print("hash value is :", text_hash)

    elif hasher == "SHA512":
        text = input("Enter the text to hash: ")
        print(f"using {hasher} algorithm")
        text_hash = hashlib.sha512(text.encode()).hexdigest()
        print("hash value is :", text_hash)

    elif hasher == "SHA1":
        text = input("Enter the text to hash: ")
        print(f"using {hasher} algorithm")
        text_hash = hashlib.sha1(text.encode()).hexdigest()
        print("hash value is :", text_hash)

    elif hasher == "md5":
        text = input("Enter the text to hash: ")
        print(f"using {hasher} algorithm")
        text_hash = hashlib.md5(text.encode()).hexdigest()
        print("hash value is :", text_hash)

    else:
        print("Invalid hash algorithm. Please choose either SHA256, SHA512, SHA1 or md5.")

if choice == "3":
    file_path = input("Enter the file name: ")
    expected_hash = input("Enter the expected hash value: ")
    hasher = input("Choose the hash algorithm (SHA256, SHA512, SHA1, md5): ")

    if hasher == "SHA256":
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                if file_hash == expected_hash:
                    print("File integrity verified. The hash values match.")
                else:
                    print("File integrity verification failed. The hash values do not match.")

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "SHA512":
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha512(f.read()).hexdigest()
                if file_hash == expected_hash:
                    print("File integrity verified. The hash values match.")
                else:
                    print("File integrity verification failed. The hash values do not match.")

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "SHA1":
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha1(f.read()).hexdigest()
                if file_hash == expected_hash:
                    print("File integrity verified. The hash values match.")
                else:
                    print("File integrity verification failed. The hash values do not match.")

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    elif hasher == "md5":
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash == expected_hash:
                    print("File integrity verified. The hash values match.")
                else:
                    print("File integrity verification failed. The hash values do not match.")

        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

    else:
        print("Invalid hash algorithm. Please choose either SHA256, SHA512, SHA1 or md5.")

if choice == "4":
    print("Thanks for using the file hasher. Kakfacodes")
