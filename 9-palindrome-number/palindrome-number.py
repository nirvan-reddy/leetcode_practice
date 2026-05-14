class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert = str(x)
        left = 0
        right = len(convert) - 1

        while left < right:
            if convert[left] != convert[right]:
                return False
            left += 1
            right -= 1

        return True

        