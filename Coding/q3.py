
def fun(s):
    ans = []

    def funback(path,con) : 
        if len(path)==len(s):
            ans.append("".join(path))
            return
        
        for i in range(len(s)):
            if not con[i]:
                con[i]=True
                path.append(s[i])
                funback(path,con)
                path.pop()
                con[i] = False
        
    funback([],[False]*len(s))
    return ans


print(fun("abc"))
print(fun("ab"))

#Time Complexity : O(n*n!)
# Space Complexity : O(n*n!)