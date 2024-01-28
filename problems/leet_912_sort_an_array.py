class Solution:
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        m = len(nums) // 2
        i, j, combine = 0, 0, []
        left = self.merge_sort(nums[:m])
        right = self.merge_sort(nums[m:])
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                combine.append(left[i])
                i += 1
            else:
                combine.append(right[j])
                j += 1
        for k in range(i, len(left)):
            combine.append(left[k])
        for k in range(j, len(right)):
            combine.append(right[k])
        return combine

    def sort_array(self, nums):
        return self.merge_sort(nums)


def main():
    """
    nums        : [4, 2, 3, 1, 5, 6]
    return      : [1, 2, 3, 4, 5, 6]
    """
    sol = Solution()
    print([1, 2, 3, 4, 5, 6] == sol.sort_array([4, 2, 3, 1, 5, 6]))


if __name__ == "__main__":
    main()
