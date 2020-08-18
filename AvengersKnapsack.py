class Avenger(object):
  def __init__(self, n, v, w):
      self.name = n
      self.value = v
      self.wt = w
  def getValue(self):
      return self.value
  def getCost(self):
      return self.wt
  def density(self):
      return self.getValue()/self.getCost()
  # def __str__(self):
  #     return self.name + ': <' + str(self.value) + ', ' + str(self.wt) + '>'

def buildMenu(names, values, costs):
  """names, values, cost lists of same length.
     name a list of strings
     values and cost lists of numbers
     returns list of Avengers"""
  menu = []
  for i in range(len(values)):
      menu.append(Avenger(names[i], values[i],
                        costs[i]))
  return menu

def greedy(items, maxCost, keyFunction):
  """Assumes items a list, maxCost >= 0,
       keyFunction maps elements of items to numbers"""
  itemsCopy = sorted(items, key = keyFunction,
                     reverse = True)
  result = []
  totalValue, totalCost = 0.0, 0.0
  for i in range(len(itemsCopy)):
      if (totalCost+itemsCopy[i].getCost()) <= maxCost:
          result.append(itemsCopy[i])
          totalCost += itemsCopy[i].getCost()
          totalValue += itemsCopy[i].getValue()
  return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
  taken, val = greedy(items, constraint, keyFunction)
  print('Total value of items taken =', val)
  for item in taken:
      print(item.name)

def testGreedys(avengers, maxUnits):

  print('Spend by value', maxUnits,
        'dollars')
  testGreedy(avengers, maxUnits, Avenger.getValue)
  print('\nSpend by cost', maxUnits,
        'dollars')
  testGreedy(avengers, maxUnits,
             lambda x: 1/Avenger.getCost(x))
  print('\nSpend by density', maxUnits,
        'dollars')
  testGreedy(avengers, maxUnits, Avenger.density)

def testDP(avengers,maxUnits):

# Construct the table and find maximum obtainable value
  result=[]
  n=len(avengers)
  W=maxUnits
  dp=[[0 for j in range(maxUnits+1)] for i in range(n+1)]

  for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                continue
            elif avengers[i-1].getCost() <= w: 
                dp[i][w] = max(avengers[i-1].getValue() + dp[i-1][w-avengers[i-1].getCost()],  dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 

# Print values in knapsack
  i=n
  j=maxUnits
  while(j>=0 and i>=0):
    if(dp[i][j]!=dp[i-1][j]):
      result.append(avengers[i-1].name)
      j-=avengers[i-1].getCost()
      i-=1
      
    else:
      i-=1
  # print(dp)
   
  return result,dp[n][maxUnits]
          


      

##initialise values, weights, names and call the functions


values = [ 10, 9, 10 ,10 ,9,
          4 , 8, 7, 7.5, 8.5,
          8.5, 1, 7.5, 3, 2,
          1, 1.5, 2, 1, 5,
          9, 1, 7, 5.5, 4 ] 

names=['ironman','captain america','scarlet witch','captain marvel','thor',
        'antman','spiderman','hulk','black panther','doctor strange',
        'black widow','rocket','gamora','war machine','groot',
        'star lord','wasp','wong','mantis','nebula',
        'loki','drax','vision','hawkeye','winter soldier']

weights = [5,5,5,5,5,
      4,4,4,4,4,
      3,3,3,3,3,
      2,2,2,2,2,
      1,1,1,1,1] 

Maxweight = 15



avengers = buildMenu(names, values, weights)
testGreedys(avengers, W)
res,val=testDP(avengers,Maxweight)
print("With dynamic Programming, avengers chosen are:\n")
for avenger in res:
  print(avenger)
print("Maximum value: ",val)







