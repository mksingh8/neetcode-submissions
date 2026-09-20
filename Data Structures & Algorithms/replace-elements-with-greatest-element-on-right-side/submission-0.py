class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr
        max_from_right = arr[-1]
        arr[-1] = -1
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = max_from_right
            max_from_right = max(max_from_right, temp)
        return arr
        