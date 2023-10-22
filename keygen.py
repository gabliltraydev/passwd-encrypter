import random

randint_key = random.randint(0,19378286477653757395947392597)
encrypt_key = randint_key
enc_key_str = str(encrypt_key)

with open("encrypt_key.txt", 'w') as f:
    f.write(enc_key_str)

