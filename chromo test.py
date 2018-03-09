#create some chromosomes
import random
def getGene(minValue,maxValue,datatype,digitsAfterDecimal=0):
    value = -1
    if(datatype == "int"):
        value = random.randint(minValue,maxValue)
    elif(datatype == "decimal"):
        multiplier = pow(10,digitsAfterDecimal)
        minValue = minValue*multiplier
        maxValue = maxValue*multiplier
        value = random.randint(minValue,maxValue)/multiplier
    
    return value

value_sum = 0
for i in range(0,100000):
    #print(getChromo(0,1,"int"))
    #print(getChromo(0,1,"decimal",5))
    value_sum = value_sum+getGene(-2,2,"decimal",8)

print(value_sum/100000)
