class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root, x, y):
        if root in [x, y, None]:
            return root

        l = self.lowest_common_ancestor(root.left, x, y)
        r = self.lowest_common_ancestor(root.right, x, y)

        if l == None and r == None:
            return None
        if l == None:
            return r
        if r == None:
            return l
        return root


def main():
    """
      1
     / \
    2  3
      /
     4
    x      : 2
    y      : 4
    return : 1
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node3.left = node4

    sol = Solution()
    print(node1 == sol.lowest_common_ancestor(node1, node2, node4))


if __name__ == "__main__":
    main()
