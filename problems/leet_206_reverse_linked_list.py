class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def helper(self, node):
        if not node or not node.next:
            return node, node
        head, tail = self.helper(node.next)

        tail.next = node
        node.next = None
        return head, node

    def reverse_list(self, node):
        return self.helper(node)[0]


def main():
    """
    nodes       : 1 > 2 > 3 > 4 > 5 > None
    return      : 5 > 4 > 3 > 2 > 1 > None
    """
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    sol = Solution()
    res = sol.reverse_list(node1)
    while res:
        print(res.val)
        res = res.next


if __name__ == "__main__":
    main()
