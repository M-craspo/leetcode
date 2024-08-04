class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
             return True
        # One tree is empty, and the other is not
        if not p or not q:
            return False
        # The current nodes have different values
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# Tree 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(root1, root2))  # Output: True

# Different tree
root3 = TreeNode(1)
root3.left = TreeNode(2)

print(solution.isSameTree(root1, root3))