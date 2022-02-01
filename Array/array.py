def missingNum(nums):
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)

def findPairs(nums,target):
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i] + nums[j]==target:
                return [i,j]

def findPairs2(nums,target):
    for i in enumerate(nums):
        if target-i[1] in nums:
            print(i[0],nums.index(target-i[1]))

def threeSum(num):
    num.sort()
    for i in range(len(num)):
        if i>0 and num[i]==num[i-1]:
            continue
        l,r=i+1,len(num)-1
        while l<r:
            if num[i]+num[l]+num[r]==0:
                print(num[i],num[l],num[r])
                l+=1
                r-=1
            elif num[i]+num[l]+num[r]<0:
                l+=1
            else:
                r-=1

def maxProduct(nums):
    maxproduct=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] * nums[j] > maxproduct:
                maxproduct= nums[i] * nums[j]
                num=[nums[i],nums[j]]
                pairs= list(map(str,num))
    print(pairs)
    print(maxproduct)


def isUnique(mylist):
    mylist.sort()
    for i in range(len(mylist)-1):
        if mylist[i+1]==mylist[i]:
            return False
    return True

def rotateMatrix(matrix):
    pass







def permutation(list1,list2):
    map(sorted,list1,list2)
    return list1==list2


num=[-1,0,1,2,-1,-4,-2,-3,5]
nums=[2,2,3,5,0,1,3,4]

if __name__=="__main__":
    print(permutation(nums))
    #print(threeSum(num))

