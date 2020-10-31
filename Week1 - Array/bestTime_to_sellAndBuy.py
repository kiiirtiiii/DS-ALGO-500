def maxProfit(prices):
    if len(prices):
        small = max(prices)+1
    else:
        return 0
    best = 0
    for i in prices:
        if i<small:
            small = i
            
        best = max(best, i-small)
        
    return best

prices = [7,1,5,3,6,4]
x = maxProfit(prices)
print("Max Profit: ", x)


########## OUTPUT ##########
'''
Max Profit:  5
'''