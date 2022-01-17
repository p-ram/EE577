# -*- coding: utf-8 -*-
"""
Process variation for Isub and Id

@author: pram
"""

import numpy as np
import math

mu,sigma=0.48,0.05

s=np.random.normal(mu,sigma,1000)


def f(x):
    Io=0.00001
    # KT/q at 25C => 0.02569
    Isub=Io*(math.exp(-x/0.038535))
    
    Id=0.00009*0.5*((1.2-x)**2)
    
    return Isub,Id

text=open("variation_analysis.txt","w")

for count,value in enumerate(s):
    text.write(str(count)+" "+ str(value)+" "+str(f(value)[0])+" "+str(f(value)[1])+"\n")
    
    Isub=f(value)[0]
    Id=f(value)[1]
    
    #min max for Isub
    if count==0:
        Ismax=Isub
        Ismin=Isub
        
        Idmax=Id
        Idmin=Id
    
    else:
        if Isub>Ismax:
            Ismax=Isub
        
        if Isub<Ismin:
            Ismin=Isub
    
        if Id>Idmax:
            Idmax=Id
        
        if Id<Idmin:
            Idmin=Id

text.write("1000"+" --- "+str(Ismax/Ismin)+" "+ str(Idmax/Idmin))
text.close()

