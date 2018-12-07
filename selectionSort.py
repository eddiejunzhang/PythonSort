def selectionSort(x):
   i = 0
   while i < len(x) - 1:
       minindex = i
       j = i + 1
       while j < len(x) :        
           if x[minindex] > x[j]:
               minindex = j
           j+= 1
       if minindex != i:
           swap(x,i,minindex)    
       i+= 1
   return x
