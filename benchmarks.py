# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm."
           Information sciences 179.13 (2009): 2232-2248.

Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

 -- Purpose: Defining the benchmark function code
              and its parameters: function Name, lowerbound, upperbound, dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math



def F1(individual , capacity , v , w):
    index = 0
    weight = 0
    profit = 0
    for i in individual:
        if i > 50 :
            weight += w[index]
            profit += v[index]
            if weight > capacity :
                profit = 0
                return profit
        index+=1
    return profit



def getFunctionDetails(a):
  # [name, lb, ub, dim]
  param = {  0: ["F1",0,100,20],
            }
  return param.get(a, "nothing")
