class Solution:
    def reverse(self, x: int) -> int:
        text = str(x)
        negative = -1 if "-" in text else 1
        number = int("".join(reversed(text.replace("-", ""))))

        max_result = 2**31
        return number*negative if number <= max_result else 0
