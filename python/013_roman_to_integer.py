class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        values = [conversions[x] for x in s]

        for x in range(len(values)):
            if x + 1 < len(values) and values[x] < values[x + 1]:
                sum -= values[x]
            else:
                sum += values[x]
        return sum


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
