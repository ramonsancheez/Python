#Write a function that will check whether the permutation of an input string is a palindrome.
def permute_a_palindrome (input): 
    oddTotal = 0
    for letters in input:
        lettersNumber = input.count(letters)
        if lettersNumber % 2 == 0:
            continue
        elif lettersNumber % 2 !=0:
            oddTotal += 1
            if oddTotal <= 1:
                continue
            else:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    assert permute_a_palindrome("a") == True
    assert permute_a_palindrome("aab") == True 
    assert permute_a_palindrome("racecars") == False
    assert permute_a_palindrome("baabcd") == False
    assert permute_a_palindrome("") == True