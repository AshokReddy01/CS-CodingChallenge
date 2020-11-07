import sys
# You may change this function parameters
def findValue(values):
    minValue = min(values)
    index = values.index(minValue)
    if index == len(values)-1:
        findValue(values[:-1])
    else:
        v = max(values[index:])
        return v-minValue
    


def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    cost = []
    valu = list(predictedSharePrices)
    predictedSharePrices = list(predictedSharePrices)
    valu.sort()
    c = True
    for i in valu:
        if c:
            cost.append(findValue(predictedSharePrices))
            predictedSharePrices.remove(i)
            c=False
        elif len(predictedSharePrices)>2:
            predictedSharePrices.remove(i)
            cost.append(findValue(predictedSharePrices))
    return max(cost)


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
