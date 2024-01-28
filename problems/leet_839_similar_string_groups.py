class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, s):
        if s == self.parent[s]:
            return s
        p = self.find(self.parent[s])
        self.parent[s] = p
        return p

    def union(self, s1, s2):
        p1, p2 = self.find(s1), self.find(s2)
        self.parent[p2] = p1


class Solution:
    def similar(self, s1, s2):
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) == 2:
            if s1[diff[0]] == s2[diff[1]]:
                return True
        return False

    def num_similar_groups(self, strs) -> int:
        uf = UnionFind()
        for s in strs:
            uf.parent[s] = s

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                s1, s2 = strs[i], strs[j]
                if self.similar(s1, s2):
                    uf.union(s1, s2)
        ss = set()
        for s in strs:
            ss.add(uf.find(s))
        return len(ss)


def main():
    """
    strs    : ["tars","rats","arts","star"]
    return  : 2  # {tars, rats, arts}, {star}
    """
    sol = Solution()
    print (sol.num_similar_groups(["tars","rats","arts","star"]))


if __name__ == "__main__":
    main()
