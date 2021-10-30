# O(n) Time | O(n) Space
def isPalindrome(string):
    """
    Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a
    palindrome.
    """
    if string[::-1] == string:
        return True
    return False


# O(n) Time | O(1) space
# Takes advantage of the fact that's letter is equal to respective last letter, like a mirror reflection.
def isPalindromeBetter(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True
