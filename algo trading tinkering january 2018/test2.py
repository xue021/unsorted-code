#TEST 2 - https://min-api.cryptocompare.com/data/histominute?fsym=ETH&tsym=USD&limit=60&aggregate=3
#using py 3.4.3
import urllib.request, json, time

buyPrice = 0
profitTotal = 0
def calcStoch14 (vals):
    global buyPrice
    global profitTotal
    C = vals[len(vals)-1]
    H14 = 0;
    L14 = 1000000;
    for i in range(len(vals)-14,len(vals)):
        if(vals[i]>H14):
            H14 = vals[i]
        if(vals[i]<L14):
            L14 = vals[i]
    K = 100*((C-L14))/(H14-L14)
    print("Stochastic Values - K="+str(K) +" - C="+str(C)+" H14="+str(H14)+" L14="+str(L14))
    if((K<15.0) & (buyPrice == 0.0)):
        buyPrice = C
        print("Buy price="+str(buyPrice))
    if((K>85.0) & (buyPrice != 0.0)):
        profit = C -buyPrice
        buyPrice = 0
        print("*******Sell price = "+str(C) + " for a profit of: "+str(profit))
        profitTotal = profitTotal + profit
        print("Total profit so far = "+str(profitTotal))

with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histominute?fsym=ETH&tsym=USD&limit=144&aggregate=20") as url:
    data = json.loads(url.read().decode())
#NOTE: AGGREGATE IS NUMBER OF MINS BETWEEN SAMPLE 
    

arr = data.get("Data")
print("----")

length = len(arr)
values = []
print("total number of entries: " + str(length))
buyPrice = 0
for i in range(0, length):
    print("----------")
    
    values.append(arr[i].get("close"))
    print(values[i])
    if(i>30):
        calcStoch14(values)

print("Final Profit is: "+str(profitTotal))
        
