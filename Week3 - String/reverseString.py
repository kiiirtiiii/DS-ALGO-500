def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    return s

s = ["h","e","l","l","o"]
print(reverseString(s))


######### OUTPUT #########
'''
['o', 'l', 'l', 'e', 'h']
'''