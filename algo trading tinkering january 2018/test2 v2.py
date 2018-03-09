#TEST 2 - https://min-api.cryptocompare.com/data/histominute?fsym=ETH&tsym=USD&limit=60&aggregate=3
#using py 3.4.3
import urllib.request, json, time

buyPrice = 0
sellForProfitPrice = -1
profitTotal = 0
currencyHeld = 0.43457985
numberOfTransactions = 0
def calcStoch14 (vals):
    global buyPrice
    global profitTotal
    global sellForProfitPrice
    global ethHeld
    global numberOfTransactions
    
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
    if((K<=20.0) & (buyPrice == 0.0)):
        buyPrice = C
        sellForProfitPrice=C*1.04#percent profit i want
        print("******Buy price="+str(buyPrice))
        print("******Target Sell Price="+str(sellForProfitPrice))
        numberOfTransactions = numberOfTransactions + 1
    if((C >= sellForProfitPrice) & (buyPrice !=0.0)):
       profit = (C-buyPrice)*currencyHeld
       buyPrice = 0
       sellForProfitPrice = -1
       print("*******Sell price = "+str(C) + " for a profit of: "+str(profit))
       profitTotal = profitTotal + profit
       print("Total profit so far = "+str(profitTotal))
       numberOfTransactions = numberOfTransactions + 1

# OLD SELL CRITERIA
##    if((K>=80.0) & (buyPrice != 0.0)):
##        profit = C -buyPrice
##        buyPrice = 0
##        print("*******Sell price = "+str(C) + " for a profit of: "+str(profit))
##        profitTotal = profitTotal + profit
##        print("Total profit so far = "+str(profitTotal))

agg=5
limit=1000
currencySymbol = "ETH"#implement this in api
with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histominute?fsym=ETH&tsym=USD&limit="+str(limit)+"&aggregate="+str(agg)) as url:
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
    if(i>15):
        calcStoch14(values)

initialCapital = currencyHeld*values[0]
print("Initial Capital: "+str(initialCapital)+" USD")
print("Number of Transactions: "+str(numberOfTransactions))
print("Final Profit is: "+str(profitTotal))
runtime = length*agg
print("Total run time: "+str(runtime))
print("Total # of times run: "+str(length))
ppm = profitTotal/runtime
print("Profit Per Min: "+str(ppm))
ppd = ppm*1440
print("Profit Per Day: "+str(ppd))



        
