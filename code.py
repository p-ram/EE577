# -*- coding: utf-8 -*-
"""
input text_in.txt, if the word ‘THE’ (case-insensitive) occurs even number of times you should rewrite the words in the paragraph with all the words staring with – ‘a,e,i,o,u’ in UPPER CASE. All other words should be in lower case. If the word ‘THE’ does not occur in a sentence, then you should still rewrite the words in the paragraph with all the words staring with – ‘a,e,i,o,u’ in UPPER CASE. All other words should be in lower case.
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
    
    # count 'the' and 'The'    
    print(i)
    y=len(re.findall('the\s',i))
    z=len(re.findall('The\s',i))
    
    #if odd no of the, write to textout 
    if (z+y)%2!=0:
        textout.write(i+'. ')
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
            
  
        textout.write('. ')
textout.close()
textin.close()

