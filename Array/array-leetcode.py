
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



def lenlongestSubstring(word):
    pass



l1=["cat","rat","bat", "tac"]
print("".join(sorted(l1)))





#if __name__=="__main__":
    #print(threeSum([-1, 0, 1, 2, -1, -4]))

