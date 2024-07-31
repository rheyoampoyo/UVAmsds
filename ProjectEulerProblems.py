#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math


# In[5]:


# Problem 1 ProjectEuler
## Find the sum of all the multiples of 3 or 5 below 1000
def multiples_of_3_and_5(n):
    lst = []
    if n > 0:
        for i in range(1,n):
            if (i % 3) and (i % 5) == 0:
                lst.append(i)
            elif (i % 3) == 0:
                lst.append(i)
            elif (i % 5) == 0:
                lst. append(i)
        return sum(lst)
    else:
        return ('Enter a positive integer')

print(f'The sum of all the multiples of 3 or 5 below 1000 is {multiples_of_3_and_5(1000)}')


# In[6]:


# Problem 2 ProjectEuler
## By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def sum_even_fibbonaci_terms(n):
    lst = [1,2]
    final_sum = []
    
    while lst[-1] < n:
        term_3 = lst[-2] + lst[-1]
        lst.append(term_3)
        
    final_sum = [i for i in lst if (i % 2) == 0]

        
    return(sum(final_sum))
    
print(f'The sum of the even-valued terms whose values do not exceed four million is {sum_even_fibbonaci_terms(4000000)}')


# In[53]:


# Problem 3 ProjectEuler
## What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    if (n == 0) or (n == 1) or (n == 2):
        return n
    else:
        factors = [i for i in range(2, int(math.sqrt(n)+1)) if (n%i == 0)]
    
    final_factors = []
    
    for i in factors:
        for j in range(1,int(i/2)+1):
            if (i % j == 0):
                final_factors.append(j)

        
        
    return max(final_factors)

print(f'The largest prime factor of the number 600851475143 is {largest_prime_factor(600851475143)}')
    


# In[ ]:




