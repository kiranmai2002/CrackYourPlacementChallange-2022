class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=nums
        p=[]
        l.sort()
        for i in range(len(l)-1):
            if(l[i]^l[i+1]==0):
                p.append(l[i])
        return p
