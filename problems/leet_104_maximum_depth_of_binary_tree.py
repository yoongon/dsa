class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root) -> int:
        if root is None:
            return 0
        l = self.max_depth(root.left)
        r = self.max_depth(root.right)
        return 1 + max(l, r)


def main():
    """
      1
     / \
    2  3
      /
     4
     height is 3
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node3.left = node4

    sol = Solution()
    print(3 == sol.max_depth(node1))


if __name__ == "__main__":
    main()
