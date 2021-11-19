# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

if __name__ == "__main__":
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True 
    assert is_prime(4) == False
    assert is_prime(72) == False
    assert is_prime(-2) == False
    assert is_prime(73) == True
    assert is_prime(5099) == True
    
    

