def countAndSay(n):
        c = ["1", "11"]
        
        if n==1:
            return c[0]
        elif n==2:
            return c[1]
        
        else:
            while len(c)<n:
                x = 1
                z = ""
                for i in range(0, len(c[-1])-1):
                    if c[-1][i]==c[-1][i+1]:
                        x += 1
                    else:
                        z += str(x)+c[-1][i]
                        x = 1

                if c[-1][-1]!=c[-1][-2]:
                    x = "1"
                
                z += str(x)+c[-1][-1]
                    
                c.append(z)
                        
            return c[-1]
n = 4
print(countAndSay(n))

######## OUTPUT ########
'''
1211
'''