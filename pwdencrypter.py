actual_passwd = input("Quel est vôtre MDP actuel ? : ")

with open("encrypt_key.txt.txt", 'r') as f:
    encryption_key = f.read()

encryption_key.replace("a", encryption_key)
