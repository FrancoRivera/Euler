import unittest

def isPalindrome(number):
    cadena = str(number)
    for i in range(int(len(cadena)/2)):
        if cadena[i] != cadena[len(cadena)-1-i]:
            return False
    return True


class Prob4Tests(unittest.TestCase):

    def test(self):
        # Given
        number = 12321
        # When
        result = isPalindrome(number)
        # Then
        self.assertEqual(result, True)

largest = 0

for i in range(0, 999):
    for j in range(0, 999):
        number = i*j
        if isPalindrome(number):
            if number > largest:
                largest = number

print(largest)

# 906609
