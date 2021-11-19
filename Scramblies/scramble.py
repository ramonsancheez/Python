# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false
def scramble(s1, s2):
    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
        else:
            pass
    return True

if __name__ == "__main__":
    assert scramble('rkqdlw', 'world') == False
    assert scramble('cedewaraaossoqqyt', 'codewars') == True
    assert scramble('katas', 'steak') == False
    assert scramble('scriptjava', 'javascript') == True
    assert scramble('scriptingjava', 'javascript') == True
    assert scramble('scriptjavx', 'javascript') == False