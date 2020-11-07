# You may change this function parameters
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    cost = []
    try:
        m = max(predictedSharePrices)
        for i in range(numOfPredictedTimes):
            if predictedSharePrices[i] == m:
                pass
            elif predictedSharePrices[i]<predictedSharePrices[i+1]:
                cost.append(predictedSharePrices[i+1]-predictedSharePrices[i])

        return sum(cost)
    
    except:
        return sum(cost)



def main():
    line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()