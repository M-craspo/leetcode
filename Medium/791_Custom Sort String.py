class Solution(object):
    def customSortString(self, order, s):

        def get_index(x):
            return order.index(x) if x in order else len(order)
        
        # Sort string using custom key function
        return ''.join(sorted(s, key=get_index))

s = Solution()
print(s.customSortString("cba", "abcd"))  # Output: "cba"