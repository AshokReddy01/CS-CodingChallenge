
def findValues(m,prices):
    cost = []
    try:
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if (prices[j]-prices[i]) == m:
                    cost.append (str(i+1)+' '+str(j+1))
                    break
        return cost[-1]
    except :
        return cost[-1]


def find_min_days(prices, profit):
    data=[]
    for i in profit:
        data.append(findValues(i,prices))
    for i in data:
        print(i,end=', ')


    return ""

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line