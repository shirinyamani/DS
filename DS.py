def openRussionDoll(doll):
    if doll==1: #when we reach to the end!
        print('all dolls are opened!')
    else:
        openRussionDoll(doll-1) #call the function on smaller pieces!

def Recursion(n):
    if n < 1:
        print(f'{n} is less than 1')
    else:
        Recursion(n-1)
        print(n)

def factorial(n):
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)

def fibonnacci(n):
    assert n>=0 and int(n)==n, 'fibonacci gotta be possitive!'
    if n <1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

def sumdigit(n):
    if n ==0:
        return 0
    else: return int(n%10) + sumdigit(int(n/10))
     
def powernum(base,exp):
    if exp ==1:
        return base
    elif exp==0:
        return 1
    
    return base * powernum(base, exp) 

def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

def convertDecimaltobinary(n):
    if n==0:
        return 0
    else: return n%2 + 10 * convertDecimaltobinary(int(n/2))

#if __name__=="__main__":
   # print(Recursion(4))
    #print(factorial(5))
    #print(convertDecimaltobinary(13))
def isPalindrome(strng):
    if len(strng) <=1:
        return True
    elif strng[::] != strng[::-1]:
        return False
    else: return True

def isPalindrome2(strng):
    if len(strng) <=1:
        return True
    elif strng[0] != strng[-1]:
        return False
    else: return isPalindrome2(strng[1:-1])

def flatten(arr):
    resultarr=[]
    for i in arr:
        if type(i) is list:
            resultarr.extend(flatten(i))
        else:
            resultarr.append(i)
    return resultarr

a=["shiti", "cat"]
def capital(arr):
    result=[]
    for i in arr:
        result.append(i.capitalize())
    return result

def capitalizefirst(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0][0].upper()+arr[0][1:])
    return result + capitalizefirst(arr[1:])

def stringifynumbers(obj):
    for key in obj:
        if type(obj[key]) is int:
            obj[key] = str(obj[key])
        elif type(obj[key]) is dict:
            obj[key] = stringifynumbers(obj[key])
    return obj
a= {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
print(stringifynumbers(a))
