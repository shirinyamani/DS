
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

def findAnagram(arr):
    anagram ={}
    for word in arr:
        sorted_word = "".join(sorted(word))
        if word in anagram:
            anagram[sorted_word].append(word)
        else: anagram[sorted_word]= [word]
    return anagram.values()


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

def longestSub(s):
    longest=""
    len_longest=0
    for i in s:
        longest += i
        print(longest)
        if len(longest)>len_longest:
            len_longest=len(longest)
    return longest

def palindromicSub(s):
    s = longestSub(s)
    print(s)
    if s == s[::-1]:
        return s
    



def validPalindrome(s):
    s ="".join(i for i in s.lower() if i.isalnum())
    if s == s[::-1]:
        return True
    else: False

if __name__=="__main__":
    print(longestSub("babad"))
