import collections


class Solution:
    def bst_advanced(self, vertices, edges):
        visited = set()
        for v in vertices:
            if v not in visited:
                q = [v]
                while q:
                    nq = []
                    for n in q:
                        if n in visited:
                            continue
                        visited.add(n)
                        print(n)
                        for nn in edges[n]:
                            nq.append(nn)
                    q = nq


def main():
    """
        1
      /   \
     2     3     5-6
      \   /
        4

    vertices  :   [1, 2, 3, 4, 5, 6]
    edges     :   {1: [2, 3], 2: [1, 4], 3:[1,4], 4:[2,3], 5:[6], 6:[5]}
    print     :   1 2 3 4 5 6
    """
    vertices = [1, 2, 3, 4, 5]
    edges = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3], 5: [6], 6: [5]}
    sol = Solution()
    sol.bst_advanced(vertices, edges)


if __name__ == '__main__':
    main()
