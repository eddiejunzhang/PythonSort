def HashSort(x):
   gap = round(len(x)*2/3)
   while gap > 0 :    
       print('gap =  ',gap )
       i = gap
       while i < len(x):
           j = i - gap
           item = x[i]
           while j >= 0 and item < x[j]:
               x[j + gap] = x[j]
               j -= gap
           x[j + gap] = item
           i += 1
       gap = round(gap/3)
   return x
