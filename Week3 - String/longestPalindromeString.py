def longestPalindrome(S):                                
    x = 0
    palindromes = []
    
    if len(S)>1:
        while x<len(S):
            p = S[x]
            u = ""
            
            for i in range(x, len(S)):
                u += S[i]
                v = u[::-1]
                
                if u==v:
                    if len(p)<len(u):
                        p = u
                
            palindromes.append(p)            
            x += 1
          
        if len(palindromes)!=0:  
            n = palindromes[0]
            for i in palindromes:
                if len(i)>len(n):
                    n = i
            return n
            
    else:
        return S
    
S = "aaaabbaa"
print(longestPalindrome(S))


##### OUTPUT #####
'''
aabbaa
'''