import os

def generate_key():
    # This is the "Infrastructure First" logic
    if not os.path.exists("vault"):
        os.makedirs("vault")
    
    key_path = "vault/master.key"
    if not os.path.exists(key_path):
        with open(key_path, "wb") as f:
            f.write(os.urandom(32))
        print("[VAULT] Master Key Created.")
    else:
        print("[VAULT] Master Key Verified.")