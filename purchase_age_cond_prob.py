from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
N=100000
for num in range(N):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = random.random()
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1
        
    
#now find the probability of purchasing something given you are in 30's
#P(E|F) where E is purchase and F is being in 30's
# first probability of purchasing something AND being in 30's 
#Look at purchases, sum, inverse * #in 30's
#BUT can just do 

PEF= float(purchases[30])/float(totals[30])
#same as (float(purchases[30])/N )* N/float(totals[30])