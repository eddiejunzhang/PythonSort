def BubbleSort_1(x):
   j = len(x) - 1
   while j > 0 :
       flag = False
       i = 0
       while i < j:
           if x[i] > x[i + 1]:
               swap(x,i,i+1)
               flag = True
           i += 1
       if not flag:
           return x
       j -= 1
   return x
