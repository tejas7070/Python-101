def stock(price):
    n =len(price)
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):

           res = max(res,price[j]-price[i])
    return res
        
price =[23,10,56,12,8]
print(stock(price))  