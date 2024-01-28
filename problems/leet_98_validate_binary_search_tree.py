import math


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def check(self, root, left_limit, right_limit):
        if not root:
            return True

        return left_limit < root.val < right_limit \
            and self.check(root.left, left_limit, root.val) \
            and self.check(root.right, root.val, right_limit)

    def is_valid_bst(self, root) -> bool:
        return self.check(root, -math.inf, math.inf)


def main():
    """
        2
     /    \
    1     4
         / \
        3   5

    :return: True
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node2.left = node1
    node2.right = node4
    node4.left = node3
    node4.right = node5

    sol = Solution()
    print(sol.is_valid_bst(node2))


if __name__ == "__main__":
    main()
