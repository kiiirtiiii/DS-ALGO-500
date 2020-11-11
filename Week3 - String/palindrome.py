def isPlaindrome(S):
    for i in range(len(S)//2):
        if S[i]!=S[len(S)-1-i]:
            return 0
    return 1

S = "abba"
print(isPlaindrome(S))

S = "abc"
print(isPlaindrome(S))


####### OUTPUT #######
'''
1
0
'''