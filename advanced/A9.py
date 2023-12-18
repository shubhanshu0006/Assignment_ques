#Given an input string, write a function that returns the run length encoded string for
#the input string.
#Eg:
#Input: wwwwaaadebbbbbw
#Output: w4a3d1e1b5w1

strr = "shhhaaak k"
l2 = []
newstr = ""
count = 1
for i in range(len(strr)-1):
   
    if strr[i] == strr[i+1]:
        count+=1
    else:
        newstr = newstr + strr[i] + str(count)
        count = 1
newstr = newstr + strr[-1] + str(count)


print(newstr)



    

