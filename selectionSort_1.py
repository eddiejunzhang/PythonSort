def selectionSort_1(x):
   i = 0
   while i <= len(x) // 2:
       minindex = i
       maxindex = i
       j = i + 1
       while j < len(x) - i  :
           if x[minindex] > x[j]:
               minindex = j
           if x[maxindex] < x[j]:
               maxindex = j
           j+= 1
       if x[minindex] == x[maxindex]:
           return x 
       if minindex != i:
           swap(x,i,minindex)
       if maxindex != len(x) - 1 - i :
           if maxindex != i:
               swap(x,len(x) - 1 - i,maxindex)
           else:
               swap(x,len(x) - 1 - i, minindex)
       i+= 1 
   return x
