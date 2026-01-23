import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        values = nums[:]
        left = [-1] * n
        right = [-1] * n
        removed = [False] * n

        for i in range(n):
            if i > 0:
                left[i] = i - 1
            if i < n - 1:
                right[i] = i + 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (values[i] + values[i + 1], i))

        # Count initial decreases
        decrease = 0
        for i in range(n - 1):
            if values[i] > values[i + 1]:
                decrease += 1

        ops = 0

        while decrease > 0:
            s, i = heapq.heappop(heap)
            j = right[i]

            if j == -1 or removed[i] or removed[j]:
                continue
            if values[i] + values[j] != s:
                continue

            ops += 1

            # decrease correction
            if values[i] > values[j]:
                decrease -= 1

            li = left[i]
            rj = right[j]

            # fix left neighbor
            if li != -1:
                if values[li] > values[i] and values[li] <= s:
                    decrease -= 1
                elif values[li] <= values[i] and values[li] > s:
                    decrease += 1

            # fix right neighbor
            if rj != -1:
                if values[j] > values[rj] and s <= values[rj]:
                    decrease -= 1
                elif values[j] <= values[rj] and s > values[rj]:
                    decrease += 1

            # merge
            values[i] = s
            removed[j] = True
            right[i] = rj
            if rj != -1:
                left[rj] = i

            # push new pairs
            if li != -1:
                heapq.heappush(heap, (values[li] + values[i], li))
            if rj != -1:
                heapq.heappush(heap, (values[i] + values[rj], i))

        return ops
