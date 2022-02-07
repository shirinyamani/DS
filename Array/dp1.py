class Solution:
    def getallsub(arr):
        return [arr[i:j] for i in range(len(arr)) for j in range(len(i+1, len(arr)-1))]


s=Solution()
print(s.getallsub([2,3,5,6,7,-1]))       