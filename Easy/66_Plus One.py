class Solution(object):
    def plusOne(self, digits):
        # Start from the last digit and work backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If all digits are 9, the result will be a list of 1 followed by all 0s
        return [1] + [0] * len(digits)

