#!/usr/bin/env python
# coding: utf-8

# In[7]:


a= int(input("Enter the number: "))
b= a+3
print("After Adding 3 =",b)
c= b*2
print("After Multiplying by 2 =",c)
d= c-4
print("Afer Subtracting 4 =",d)
e= d+3
print("Again Adding 3 =",e)


# In[8]:


Celsius= int(input("Enter the number in Celsius: "))
Fahrenheit= ((Celsius*1.8)+32)
print("The value of Fahrenhiet is",(Fahrenheit))


# In[9]:


Radius= int(input("Enter the value: "))
Area= (3.142*Radius**2)
print("The area of circle is =",Area)


# In[10]:


color= input("What is your favourite color? ")
print(color*10)
print(color + ("   ")*8 + color)
print(color*10)


# In[13]:


a= "\tHello\tWorld\t"
print(a)
b= "\nHello\nWorld\n"
print(b)

str= "Hello World"
print(str.lstrip('H'))
print(str.rstrip('l d'))
print(str.strip('H e l'))


# In[ ]:




