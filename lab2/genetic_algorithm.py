# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JXHzX9FtvzDBhECNDTAFIE4Hxp4mZIuS

## CSE422 lab: Genetic Algorithm

# Genetic Algorithm Pseudo code:

**function** GENETIC-ALGORITHM( population, FITNESS-FN) **returns** an individual 
 
> **inputs:** population- a set of individuals/chromosomes; FITNESS-FN- a function that measures the fitness of an individual

>**repeat** 
new_population $\leftarrow$ empty set 
>>**for** $i=1$ **to** size ($ population$) **do**
$$
\begin{array}{l}
x \leftarrow \text { RANDOM-SELECTION }(\text { population, FITNESS-FN }) \\
y \leftarrow \text { RANDOM-SELECTION }(\text { population, FITNESS-FN }) \\
child  \leftarrow \operatorname{CROSSOVER}(x, y)
\end{array}
$$
>>>**if** (some_random_number < mutation_threshold) **then** child$\leftarrow$ MUTATE ( child ) 

>>>add child to new_population 

>>population $\leftarrow$ new_population 

>**until** some individual is fit enough, or enough time has elapsed

>**return** the best individual in population, according to FITNESS-FN"""


import random

import numpy as np

"""### Fitness function"""

def fitness(population, n):

  h_collisions = sum([population.count(queen) - 1 for queen in population]) / 2
  
  maxFitness = (n * (n - 1)) /2
   
  length = len(population)
  left_diag = [0] * 2 * length
  right_diag = [0] * 2 * length
  
  for i in range(length):
    left_diag[i + population[i] - 1] += 1
    right_diag[len(population) - i + population[i] - 2] += 1
  
  d_collisions = 0
  
  for i in range(2 * length - 1):
    count = 0
    if left_diag[i] > 1:
      count += left_diag[i] - 1
    if right_diag[i] > 1:
      count += left_diag[i] - 1
    d_collisions += count / (length - abs(i - length - 1))
  
  return int(maxFitness - (h_collisions + d_collisions))

"""### Random Selection function

This built-in function might help to create the weighted random selection:

`numpy.random.choice(a, size, replace, p)` 

`p` are the weights of the individuals- value between 0 and 1; refers to the probability of each individual being selected.

`a` is the array

`size` how many samples to return

`replace = True`
"""

def select(population, fit):
  ''' take input:  population and fit
      fit contains fitness values of each of the individuals 
      in the population  
      
      return:  one individual randomly giving
      more weight to ones which have high fitness score'''
    # a = [0,1,2,3,4]
    # size = 1
    # p = [.31, .29, 0.26, 0.14]
  

  
  return

"""### Crossover function


**function** CROSSOVER $(x, y)$ **returns** an individual 

>**inputs**: $x, y$  which are the parent individuals

>$n \leftarrow \mathrm{LENGTH}(x) ; c \leftarrow$ random number from 1 to $n$ 

>**return** APPEND(SUBSTRING $(x, 1, c),$ SUBSTRING $(y, c+1, n))$
"""

def crossover(x, y):
  '''take input: 2 parents - x, y. 
     Generate a random crossover point. 
     Append first half of x with second 
     half of y to create the child
     
     returns: a child chromosome'''

     
  return

"""###Mutation function"""

def mutate(child):
  '''take input: a child
     mutates a random 
     gene into another random gene
     
     returns: mutated child'''
  

  return

"""### Genetic Algorithm Function"""

def GA(population, n, mutation_threshold = 0.3):
  '''implement the pseudocode here by
     calling the necessary functions- Fitness, 
     Selection, Crossover and Mutation
     
     print: the max fitness value and the 
     chromosome that generated it which is ultimately 
     the solution board'''




  return

"""Running the Genetic Algorithm function"""

'''for 8 queen problem, n = 8'''
n = 8

start_population = 10 

mutation_threshold = 0.3

population = np.random.randint(0, n, (start_population, n))

# GA(population, n, mutation_threshold)
