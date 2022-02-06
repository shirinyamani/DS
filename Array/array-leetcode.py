import collections
from palindrome import Solution
#sum of three numbers equal to zero 
def threeSum(num):
    num.sort()
    set_num= set()
    for i in range(len(num)):
        l,r=i+1,len(num)-1
        while l<r:
            sum_num= num[i]+num[l]+num[r]
            if sum_num ==0:
                set_num.add((num[i],num[l],num[r])) #be ja print
                l+=1
                r-=1
            elif sum_num<0:
                l +=1
            else:
                r-=1
    return [list(i) for i in set_num]

#find anaagrams
def findAnagram(arr):
    anagram ={}
    for word in arr:
        sorted_word = "".join(sorted(word))
        if word in anagram:
            anagram[sorted_word].append(word)
        else: anagram[sorted_word]= [word]
    return anagram.values()

#find the longest substring of a list of strings
def longestsubstring(s):
    longest=""
    top=0
    for i in s:
        if i not in longest:
            longest +=i
        else:
            longest= longest.split(i)[1]+i
        if len(longest)>top:
            top=len(longest)
    return top

#only longest substring
def longestSub(s):
    longest=""
    len_longest=0
    for i in s:
        longest += i
        print(longest)
        if len(longest)>len_longest:
            len_longest=len(longest)
    return longest

#find the longest palindrome in a string
s = Solution()
print( s.longestpalindrome("babad"))

#valid palindrome no spaces, punctuation
def validPalindrome(s):
    s ="".join(i for i in s.lower() if i.isalnum())
    if s == s[::-1]:
        return True
    else: False

#find missing range of numbers in a list
def missingRanges(nums, lower, upper):
    nums.append(upper+1) #append upper+1 to nums
    nums.insert(0,lower-1) # add lower and upper to the list
    res=[]
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]>1:
            res.append(str(nums[i]+1)+"->"+str(nums[i+1]-1))
        elif nums[i+1]-nums[i]==1:
            res.append(str(nums[i]+1))
    return res

def firstuniqchar(s):
    count = collections.Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx




if __name__ == "__main__":
    print(missingRanges([0,1,3,50,75],0,99))
