import hashlib

def crack_sha1_hash(hash, use_salts = False):
    salts = []
    if use_salts:
        with open("known-salts.txt") as file:
            for line in file:
                line = line.strip()
                salts.append(line)

    with open("top-10000-passwords.txt") as file:
        for line in file:
            line = line.strip()

            if use_salts:
                for salt in salts:
                    sha1 = hashlib.sha1()
                    sha1.update(f"{salt}{line}".encode('utf-8'))
                    hashed_password = sha1.hexdigest()

                    if(hashed_password == hash):
                        return line

                    sha1 = hashlib.sha1()
                    sha1.update(f"{line}{salt}".encode('utf-8'))
                    hashed_password = sha1.hexdigest()

                    if(hashed_password == hash):
                        return line
            else:
                sha1 = hashlib.sha1()
                sha1.update(line.encode('utf-8'))
                hashed_password = sha1.hexdigest()

            if(hashed_password == hash):
                return line

    return "PASSWORD NOT IN DATABASE"