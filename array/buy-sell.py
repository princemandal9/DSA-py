def stockBuySell( arr):
    min=arr[0]
    maxProfit=0
    for i in range(0,len(arr)):
        if min> arr[i]:
            min=arr[i]
        profit=arr[i]-min
        maxProfit=max(maxProfit,profit)
    return maxProfit

arr=[10, 7, 5, 8, 11, 9]
print(stockBuySell(arr))