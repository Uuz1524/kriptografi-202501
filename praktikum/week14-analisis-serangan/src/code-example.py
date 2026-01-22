import bcrypt
import time

def bcrypt_hash_password(password: str, cost: int = 12) -> str:
    """
    Hash password menggunakan bcrypt dengan salt
    
    Args:
        password: plaintext password
        cost: work factor (2^cost iterations)
              Default 12 = 4,096 iterations
    
    Returns:
        bcrypt hash (includes salt)
    """
    # Generate salt dan hash
    salt = bcrypt.gensalt(rounds=cost)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def bcrypt_verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify password against stored bcrypt hash
    """
    return bcrypt.checkpw(password.encode(), stored_hash.encode())

# Demonstration
if __name__ == "__main__":
    print("=" * 70)
    print("BCRYPT PASSWORD HASHING DEMONSTRATION")
    print("=" * 70)
    
    password = "linkedin_password_123"
    
    # Hash dengan cost factors berbeda
    for cost in [10, 12, 14]:
        print(f"\nCost factor: {cost} (2^{cost} = {2**cost:,} iterations)")
        
        start = time.time()
        hashed = bcrypt_hash_password(password, cost)
        elapsed = time.time() - start
        
        print(f"  Hash: {hashed}")
        print(f"  Time: {elapsed:.4f} seconds")
    
    # Verification
    print("\n" + "=" * 70)
    print("PASSWORD VERIFICATION")
    print("=" * 70)
    
    stored_hash = bcrypt_hash_password(password, cost=12)
    print(f"Stored hash: {stored_hash}")
    
    # Correct password
    start = time.time()
    valid = bcrypt_verify_password(password, stored_hash)
    elapsed = time.time() - start
    print(f"\nCorrect password: {valid} (time: {elapsed:.4f}s)")
    
    # Wrong password
    start = time.time()
    invalid = bcrypt_verify_password("wrong_password", stored_hash)
    elapsed = time.time() - start
    print(f"Wrong password: {invalid} (time: {elapsed:.4f}s)")
    
    # Salt demonstration
    print("\n" + "=" * 70)
    print("SALT DEMONSTRATION")
    print("=" * 70)
    
    same_password = "password123"
    hash1 = bcrypt_hash_password(same_password)
    hash2 = bcrypt_hash_password(same_password)
    
    print(f"Password: {same_password}")
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print(f"Hashes identical: {hash1 == hash2}")
    print("\nNote: Different salts → different hashes (prevents rainbow tables)")
