def BubbleSort(x):
   j = len(x) - 1
   while j > 0:
       i = 0
       while i < j:
           if x[i] > x[i + 1]:
               swap(x,i,i+1)
           i += 1
       j -= 1
   return x
