from collections import Counter

def fun(s,t) :
    n = Counter(t)
    left = count = 0
    ans = ""

    for right,c in enumerate(s):
        if c in n:
            n[c]-= 1
            if n[c]>=0:
                count+=1
        while count == len(t):
            if not ans or right-left+1<len(ans):
                ans = s[left:right+1]
            if s[left] in n:
                if n[s[left]] == 0:
                    count-=1
                n[s[left]]+=1
            left+=1
    return ans


print(fun("ADOBECODEBANC","ABC"))
print(fun("a","a"))

# Time Complexity : O(s+t)
# Space Coplexity : O(t)
