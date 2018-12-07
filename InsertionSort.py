def InsertionSort(x):
   i = 1
   while i < len(x):
       j = i - 1
       item = x[i]
       while j >= 0 and item < x[j]:
           x[j + 1] = x[j]
           j -= 1
       x[j + 1] = item
       i += 1   
   return x
