import collections


class Solution:
    def is_bipartite(self, vertices, edges) -> bool:
        visited = set()
        men, women = set(), set()
        for v in vertices:
            if v not in visited:
                q = [v]
                men.add(v)
                while q:
                    nq = []
                    for n in q:
                        if n in visited:
                            continue
                        visited.add(n)
                        for nn in edges[n]:
                            if n in men and nn in men:
                                return False
                            if n in women and nn in women:
                                return False
                            if n in men:
                                women.add(nn)
                            if n in women:
                                men.add(nn)
                            nq.append(nn)
                    q = nq
        return True


def main():
    """
        1
      / | \
     2  |  3
      \ | /
        4

    vertices  : [1, 2, 3, 4]
    edges     : {1: [2, 3, 4], 2: [1, 4], 3:[1,4], 4:[1, 2, 3]}
    return    : False (It's not bipartite)
    """
    vertices = [1, 2, 3, 4]
    edges = {1: [2, 3, 4], 2: [1, 4], 3:[1,4], 4:[1, 2, 3]}
    sol = Solution()
    print(sol.is_bipartite(vertices, edges))


if __name__ == '__main__':
    main()
