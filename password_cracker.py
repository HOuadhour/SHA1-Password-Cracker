import hashlib
passwords = open("./top-10000-passwords.txt", "r").readlines()
salts = open("./known-salts.txt").readlines()


def crack_sha1_hash(hash, use_salts=False):
  for password in passwords:
    original = password.strip()
    if use_salts:
      for salt in salts:
        salt = salt.strip()
        salted = [salt + original, original + salt, salt + original + salt]
        for i in range(3):
          hashed = hashlib.sha1(salted[i].encode())
          hashed = hashed.hexdigest()
          if hashed == hash:
            return original
    else:
      hashed = hashlib.sha1(original.encode())
      hashed = hashed.hexdigest()
      if hashed == hash:
        return original

  return "PASSWORD NOT IN DATABASE"


print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True))


# for salt in salts:
#   salt = salt.strip()
#   passwd = (salt + "superman")
#   hashed = hashlib.sha1(passwd.encode())
#   print(hashed.hexdigest())
