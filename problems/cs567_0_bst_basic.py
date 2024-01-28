class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def bst_basic(self, root):
        q = [root] if root else []
        res = []
        while q:
            nq = []
            for n in q:
                print(n.val)
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq
        return res


def main():
    """
        1
       /  \
      2    3
     /    /
    4    5
     \
      6

    print:   1 2 3 4 5 6
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node4.right = node6

    sol = Solution()
    print(sol.bst_basic(node1))


if __name__ == '__main__':
    main()
