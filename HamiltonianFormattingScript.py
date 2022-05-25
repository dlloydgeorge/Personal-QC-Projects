#!/usr/bin/env python
# coding: utf-8

# In[56]:


#modify the file path as needed
file = open(r"C:\Users\DLG\Desktop\HamiltonianCopy.txt")
#replace with whatever file name you want it to be
newfile = open("FormattedHamiltonian.txt", "w+")
print(z.read())
for x in file:
    line = x.split()
    if len(line) > 0:
        a = line[-1]
        b = '('
        for i in range(len(a)-1):
            b += a[i] + "^"
        b+= a[-1] + ")"
        line[-1] = b
        #print(c)
        d = ""
        for i in line:
            d += " " + i
          
        newfile.write(d+ "\n")
file.close()
newfile.close()
#replaced with the same file name/path that you want
e = open("FormattedHamiltonian.txt")
print(e.read()) 
            
            
        
    
        
    



# In[ ]:





# In[ ]:




