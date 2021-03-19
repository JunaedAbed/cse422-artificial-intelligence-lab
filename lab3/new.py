import math

import numpy as np


def minimax(position,d,values,maximizingPlayer,count):
  if d==depth:
    return values[position],count+1
  if maximizingPlayer:
    maxEval=-math.inf
    for i in range(0,branches):
      eval,count=minimax(position*2+i,d+1,values,False,count)
      maxEval=max(maxEval,eval)
    return maxEval,count
  else:
    minEval=math.inf
    for i in range(0,branches):
      eval,count=minimax(position*2+i,d+1,values,True,count)
      minEval=min(minEval,eval)
    return minEval,count

def minimaxwithab(position,d,values,alpha,beta,maximizingPlayer,count):
  if d==depth:
    return values[position],count+1
  if maximizingPlayer:
    maxEval=-math.inf
    for i in range(0,branches):
      eval,count=minimaxwithab(position*2+i,d+1,values,alpha,beta,False,count)
      maxEval=max(maxEval,eval)
      alpha=max(alpha,maxEval)
      if beta<=alpha:
        count-1
        break
    return maxEval,count
  else:
    minEval=math.inf
    for i in range(0,branches):
      eval,count=minimaxwithab(position*2+i,d+1,values,alpha,beta,True,count)
      minEval=min(minEval,eval)
      beta=min(beta,minEval)
      if beta<=alpha:
        count-1
        break
    return minEval,count



turns=int(input("Number of turns for Riyad:"))
depth=turns*2
branches=int(input("Number of notes from which the choice has to be made at certain time :"))
# a,b = input("Minimum and Maximum value for the range of notes ").split()
# values=np.random.randint(low=a,high=b,size=branches**depth)
values = [10,17,6,1,17,18,9,18,16]
print(values)
amount,abcount=minimaxwithab(0,0,values,-math.inf,math.inf,True,0)
amount1,mncount=minimax(0,0,values,True,0)
print("Depth:",depth )
print("Branch: ",branches)
print("Terminal States:" , branches**depth)
print("Maximun amount: ", amount)
print("Comparisons before alpha beta pruning: ", mncount)
print("Comparisons after alpha beta pruning: ", abcount)
