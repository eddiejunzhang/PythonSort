def BidirectionalBubbleSort(x):
   j = 0
   while j <= len(x)//2:
       flag = False
       for i in range(j ,len(x) - j - 1):
           if x[i]>x[i+1]:
               swap(x,i,i+1)
               flag=True
       for i in range(len(x)- 1 - j,j,-1):
           if x[i]<x[i-1]:
               swap(x,i,i-1)
               flag=True
       if not flag:
           return x
       j += 1
     
   return x
