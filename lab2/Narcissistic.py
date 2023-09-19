#!/usr/bin/env python
# coding: utf-8

# In[46]:


def narcissistic(value:int)->bool:
    length = len(str(value))
    value2 = str(value)
    every=[]
    sub1=0
    for number1 in range(0,length,1):
        every.append(value2[number1])
    for number2 in range(0,length,1):
        sub=int(every[number2])**3
        sub1=sub1+sub
    if sub1==value:
        return sub1




