# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:44:15 2021

@author: inbar
"""

def revword(str):
    l=len(str)
    new_word=''
    while l>0:
        new_word+=str[l-1]
        l-=1
    new_word=new_word.lower()
    return new_word

def countword():
    new_text=''
    word=''
    first_line=True
    count=0
    text = open('text.txt')
    for line in text:
        line=line.split()
        new_line=''
        if first_line:
            word=line[0]
            first_line=False
            new_line=word
        else:
            for w in line:
                reversed_word = revword(w)
                if word == reversed_word:
                    count+=1
                new_line+=' '+reversed_word
        new_text+= new_line + ' /n ' 
    count+=1
    return(count)
    
       



    
    
