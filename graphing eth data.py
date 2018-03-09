#BASED ON TEST3.py
#provide a given initial investment in USD
#buy into chosen crypto when indicators signal to buy


import urllib.request, json, time
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

## GLOBAL VARS
capitalInitial = 500.00
capitalCurrent = capitalInitial
cryptoSymbol = "ETH"
cryptoHeld = 0 #store current amount of the chosen crypto being stored
marginSellProfit = 1.05  #make this higher or lower?
marginSellStopLoss = .97 # NYI, make this higher or lower?
buyPrice = 0
targetSellPriceInitial = 100000000
targetSellPrice = targetSellPriceInitial


## END GLOBAL VARS

## START FUNCTIONS
def calculateStochatics(numDays,symbol):

    #get daily data
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histoday?fsym="+str(symbol)+"&tsym=USD&limit="+str(numDays)+"&aggregate=1") as url:
        dataForDaily = json.loads(url.read().decode())
    #NOTE: AGGREGATE IS NUMBER OF MINS BETWEEN SAMPLE 
    dataDaily = dataForDaily.get("Data")

    #load closing price values in dataDailyClose
    dataDailyClose = []
    for i in range(0, len(dataDaily)):
        #print("----------")    
        dataDailyClose.append(dataDaily[i].get("close"))
        #print(str(numDays-i)+") $"+str(dataDailyClose[i]))

    for i in range(0,len(dataDailyClose)):
        High= 0;
        Low = 1000000;
        for i in range(len(dataDailyClose)-numDays,len(dataDailyClose)):
            if(dataDailyClose[i]>High):
                High = dataDailyClose[i]
            if(dataDailyClose[i]<Low):
                Low = dataDailyClose[i]
    print(str(numDays)+" Day High/Low: "+str(High)+" / "+str(Low))
    C = getCurrentPrice(cryptoSymbol)
    K =(C-Low)/(High - Low)
    print("Stoch("+str(numDays)+"): "+str(K))
    return K
    
def getCurrentPrice(symbol):
    with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym="+str(symbol)+"&tsyms=USD") as url:
        data = json.loads(url.read().decode())
    #NOTE: AGGREGATE IS NUMBER OF MINS BETWEEN SAMPLE 
    dataCurrent = data.get("USD")
    #print("Current Price of "+symbol+": "+str(dataCurrent))
    return dataCurrent

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()

## END FUNCTIONS
x_plot=[]
y_plot=[]


plt.scatter(x_plot, y_plot, c="r")
plt.xlabel("Time")
plt.ylabel("Price")

## START SCRIPT
for i in range (0,8640):
    print("time: "+str(time.clock()))
    k = calculateStochatics(7,cryptoSymbol)
    currentPrice = getCurrentPrice(cryptoSymbol)
    x_plot.append(time.clock())#time
    y_plot.append(currentPrice)#price

    update_line(plt,[time.clock(),currentPrice])
    
    print("Current Price of "+cryptoSymbol+": "+str(currentPrice))

    if(targetSellPrice < targetSellPriceInitial):
        print(" with a target sell price of "+str(targetSellPrice))
    
    if((k<.25) & (capitalCurrent>0)):
        #trigger a buy
        
        cryptoHeld = capitalCurrent/ currentPrice
        capitalCurrent = 0        
        targetSellPrice=currentPrice*marginSellProfit
        print("***BUYING "+str(cryptoHeld)+" "+cryptoSymbol+"@"+str(getCurrentPrice(cryptoSymbol)))
        print("***WITH A TARGET SELL PRICE OF: "+str(targetSellPrice))
    if(currentPrice >=targetSellPrice):
        #trigger a sell for profit
        capitalCurrent = cryptoHeld*currentPrice
        targetSellPrice = 100000000
        print("***SOLD "+str(cryptoHeld)+"@"+str(currentPrice)+" FOR: "+str(capitalCurrent))
        cryptoHeld = 0
    print("Current Capital = "+str(capitalCurrent)+", Current Value of Assets = "+str(currentPrice*cryptoHeld)) 
    print("--------------")   

    


    time.sleep(10)

    
        

print("##### END OF SCRIPT #####")
# END SCRIPT
