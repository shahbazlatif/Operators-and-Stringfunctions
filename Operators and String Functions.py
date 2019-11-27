#!/usr/bin/env python
# coding: utf-8

# In[2]:


# No1 Arithmetic Operator
2%4


# In[3]:


# No2 Assignment Operator 
x=10
x+=5
print(x)


# In[5]:


#No3 Assignment operator
x=16
x-=4
print(x)


# In[6]:


#No4 Assigment Operator
x=10
x*=12
print (x)


# In[7]:


#No5 Assignment operator
x=4
x/=4
print(x)


# In[8]:


#No6 Assignment operator
x=2
x%=4
x


# In[10]:


#No7 Assignment Operator
x=2
x//=2
x


# In[11]:


#No8 Assignment Operator
x=2
x**=2
x


# In[12]:


#No9 Arithmetic Operator
2+2


# In[13]:


#No10 Arithmetic Operator
2-2


# In[14]:


#No11 Arithmetic Operator
2**2


# In[15]:


#No12 Arithmetic Operator
2/2


# In[16]:


#No13 Arithmetic Operator
4//4


# In[17]:


#No14 Comparison Operator
x=3
y=3
print (x==y)


# In[18]:


#No15 Comparison Operator
x=4
y=4
print (x!=y)


# In[19]:


#No16 Comparison Operator
x=3
y=4
print (x>y)


# In[20]:


#No17 Comparison Operator
x=3
y=4
print (x<y)


# In[21]:


#No18 Comparison Operator
x=10
y=222
print (y>=x)


# In[22]:


#No19 Comparison Operator
x=10
y=222
print (y<=x)


# In[23]:


#No20 Assignment Operator
x=10
x&=10
x


# In[25]:


# String 
dir(a)


# In[26]:


a=" Hello, My Name is shahbaz Latif   "
print (a.strip())


# In[27]:


a=" Hello, My Name is shahbaz Latif   "
print (a.lower())


# In[28]:


a="hello, hy name is shahbaz Latif"
print (a.upper())


# In[29]:


a="Hello, My Name is Shahbaz Latif"
print (a.replace("H","M"))


# In[31]:


a="hello, hy name is shahbaz Latif"
print (a.split(" "))


# In[36]:


Name="Shahbaz Latif"
text = "My name is {}"
print(text.format(Name))


# In[37]:


a = "my name is shahbaz" #capital 1st letter
x = a.capitalize()
print (x)


# In[38]:


a = "My Name Is shahbaz" # lowercase  letter
x = a.casefold()
print (x)


# In[44]:


a = "shahbaz" 
x = a.center(25)
print (x)


# In[46]:


a = "My Name Is shahbaz shahbaz"
x = a.count("shahbaz")
print (x)


# In[48]:


a = "My Name Is shahbaz "
x = a.encode()
print (x)


# In[51]:


a = "My Name Is shahbaz. "
x = a.endswith(" ")
print (x)


# In[55]:


a = "s\th\ta\th\tb\ta\tz\t"
x = a.expandtabs(3)
print (x)


# In[57]:


a = "My Name Is shahbaz. "
x = a.find("shahbaz")
print (x)


# In[60]:


a = "My Name Is shahbaz. "
x = a.index("shahbaz")
print (x)


# In[62]:


a = "My Name Is shahbaz. "
x = a.isalnum()
print (x)


# In[66]:


a = "M"
x = a.isalpha()
print (x)


# In[67]:


a = "34 "
x = a.isascii()
print (x)


# In[74]:


a = "10"
x = a.isdecimal()
print (x)


# In[75]:


a = "10"
x = a.isdigit()
print (x)


# In[ ]:


a = "10"
x = a.isdecimal()
print (x)


# In[77]:


a = "yes"
x = a.isidentifier()
print (x)


# In[78]:


a = "yes"
x = a.islower()
print (x)


# In[79]:


a = "yes"
x = a.isnumeric()
print (x)


# In[87]:


a = "yes"
x = a.isprintable()
print (x)


# In[86]:


a = " "
x = a.isspace()
print (x)


# In[89]:


a = "Operands"
x = a.istitle()
print (x)


# In[1]:


a = "O"
x = a.isupper()
print (x)


# In[2]:


a = ("shahbaz", "khan")
x = ".".join(a)

print(x)


# In[3]:


a="shahbaz"
x=a.ljust(10)
print(x,"khan")


# In[6]:


a="  Shahbaz"
x=a.lstrip()
print ("My name is",x,"My father name is latifullah")


# In[10]:


a="shahbaz"
b="latiful"
c="khan"
d="no One"
x=d.maketrans(a,b,c)
print(x)


# In[11]:


a="My name is shahbaz khan "
x=a.partition("shahbaz")
print (x)


# In[12]:


a="My name is shahbaz khan "
x=a.rfind("shahbaz")
print (x)


# In[13]:


a="My name is shahbaz khan "
x=a.rindex("shahbaz")
print (x)


# In[25]:


a="shahbaz khan "
x=a.rjust(50)
print (x,"is my name")


# In[27]:


a="My name is shahbaz khan and my father name is latifullah"
x=a.rpartition("name")
print (x)


# In[34]:


a="shahbazlatif,latifullah"
x=a.rpartition(",")
print (x)


# In[36]:


a="hello    "
x=a.rsplit()
print (x)


# In[37]:


a="hello! My name is shahbaz latif\nmyfather name is latifullah"
x=a.splitlines()
print (x)


# In[39]:


a="hello! My name is shahbaz latif\nmyfather name is latifullah"
x=a.startswith("hello")
print (x)


# In[40]:


a="hello! My name is shahbaz latif\nmyfather name is latifullah"
x=a.swapcase()
print (x)


# In[41]:


a="shahbazLatif"
x=a.title()
print(x)


# In[44]:


a="shahbazLatif"
x=a.zfill(50)
print(x)


# In[ ]:




