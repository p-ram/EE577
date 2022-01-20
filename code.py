# -*- coding: utf-8 -*-
"""
input text_in.txt, if the word ‘THE’ (case-insensitive) occurs even number of times you should rewrite the words in the paragraph with all the words staring with – 
‘a,e,i,o,u’ in UPPER CASE. All other words should be in lower case. If the word ‘THE’ does not occur in a sentence, then you should still rewrite the words in the paragraph 
with all the words staring with – ‘a,e,i,o,u’ in UPPER CASE. All other words should be in lower case.
If, however, the number of occurrences of the word ‘THE’ (case-insensitive) is odd then sentence should be written as it is in the text_in.txt file.
"""

import re

textin=open("text_in.txt","r")
text=textin.read()

#split para into sentence list
a=text.split('.')[:-1]

#open output text
textout=open("text_out1.txt","w")

for i in a:
    
    # count 'the' all combinations
    print(i)
    z0=len(re.findall('the\s',i))
    z1=len(re.findall('The\s',i))
    z2=len(re.findall('THE\s',i))
    z3=len(re.findall('tHe\s',i))
    z4=len(re.findall('THe\s',i))
    z5=len(re.findall('thE\s',i))
    z6=len(re.findall('tHE\s',i))
    z7=len(re.findall('ThE\s',i))
    
    total=z0+z1+z2+z3+z4+z5+z6+z7
    
    #if odd no of the, write to textout 
    if (total)%2!=0:
        textout.write(i+' ('+str(total)+')'+'.\n')
        print("1")
    
    else:
        sp=i.split()
        #list1=re.findall("[aeiouAEIOU]\w+",i)
        for j in sp:
            
            if re.match("[aeiouAEIOU]\w+",j):
                up=j.upper()
                print(up)
                textout.write(up+' ')
                print("2")
            else:
                textout.write(j+' ')
                print("3")
            
  
        textout.write('('+str(total)+')'+'.\n ')
textout.close()
textin.close()

