class Solution:
    def isPalindrome(self, x: int) -> bool:
        end = -1

        for num in str(x):
            if num == str(x)[end]:
                end -= 1
            else:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
