
# coding: utf-8

# In[91]:

def prime_num_detect(x):
    import sys
    lists = []
    
    try:
        x = int(x)
    except ValueError:
        print('Argument must be integer')
        sys.exit(1)
        
    if x > 0:
        for y in range(1,x+1):
            for i in range(2,y):
                if y % i == 0:
                    break
            else:
                lists.append(y)
        print(lists)
    else:
        print('input number must be more than 0')


# In[94]:

prime_num_detect(input())


# In[ ]:



