# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm."
           Information sciences 179.13 (2009): 2232-2248.
Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

Purpose: Main file of Gravitational Search Algorithm(GSA)
            for minimizing of the Objective Function

Code compatible:
 -- Python: 2.* or 3.*
"""

import random
import numpy
import math
from solution import solution
import time
import massCalculation
import gConstant
import gField
import move


def GSA(objf,lb,ub,dim,PopSize,iters):
    # GSA parameters
    ElitistCheck =1
    Rpower = 1

    s=solution()

    """ Initializations """

    vel=numpy.zeros((PopSize,dim))
    fit = numpy.zeros(PopSize)
    M = numpy.zeros(PopSize)
    gBest=numpy.zeros(dim)
    gBestScore=float(0)

    v = [950, 940, 920, 1300, 12, 10, 1000, 13, 10, 1200,950, 940, 920, 1300, 12, 10, 1000, 13, 10, 1200]
    w = [52, 49, 45, 64, 75, 87, 30, 59, 82, 51,52, 49, 45, 64, 75, 87, 30, 59, 82, 51]
    W = 600

    pos=numpy.random.uniform(0,1,(PopSize,dim)) *(ub-lb)+lb

    convergence_curve=numpy.zeros(iters)

    


    for l in range(0,iters):
        for i in range(0,PopSize):
            l1 = [None] * dim
            l1=numpy.clip(pos[i,:], lb, ub)
            pos[i,:]=l1

            #Calculate objective function for each particle
            fitness=[]
            fitness=objf(l1,W,v,w)
            fit[i]=fitness


            if(gBestScore<fitness):
                gBestScore=fitness
                gBest=l1


        """ Calculating Mass """
        M = massCalculation.massCalculation(fit,PopSize,M)

        """ Calculating Gravitational Constant """
        G = gConstant.gConstant(l,iters)

        """ Calculating Gfield """
        acc = gField.gField(PopSize,dim,pos,M,l,iters,G,ElitistCheck,Rpower)

        """ Calculating Position """
        pos, vel = move.move(PopSize,dim,pos,vel,acc)

        convergence_curve[l]=gBestScore

        if(l%1==0):
            print(['At iteration '+ str(l+1)+ ' the best fitness is '+ str(gBestScore)]);
    for i in gBest:
        if (i < 50):
            print(0,end = ' ')
        else:
            print(1,end = ' ')
    print(" ")
