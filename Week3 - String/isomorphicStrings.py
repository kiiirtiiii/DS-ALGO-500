def areIsomorphic(s,p):
    
    if len(s)!=len(p):
        return False
    
    for i in range(len(s)):
        if s.index(s[i])!=p.index(p[i]):
            return False
    return True
        
s = 'xudzhi'
p = 'ftakcz'
print(areIsomorphic(s, p))

s = 'aab'
p = 'xxy'
print(areIsomorphic(s, p))

s = 'aab'
p = 'xyz'
print(areIsomorphic(s, p))


######## OUTPUT ########
'''
True
True
False
'''