
def sliding_window_maximum(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    deque = []
    for i in range(len(nums)):
        while deque and deque[0] < i - k + 1:
            deque.pop(0)
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(nums, k))
