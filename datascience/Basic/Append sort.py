w =int(input())
e = int(input())
r =int(input())

K=[]
K.append(w)
K.append(e)
K.append(r)
i=0
while i< len(K):
      
      K.sort(reverse=True)
      print(f"Smallest to Greatest:,{K[i]}")
    
      break