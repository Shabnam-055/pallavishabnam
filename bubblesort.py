import time 
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
def bubble_sort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(n-2-i):
            if a[j]>a[j+1]:
             temp=a[j]  
             a[j]=a[j+1]
             a[j+1]=temp
x=[34,46,43,27,57,41,45,21,70]
print("before sorting",x)
bubble_sort(x)
print("after sorting",x)
elements=list()
times=list()
for i in range(1,10):
    a=randint(0,1000*i,1000*i)
    start=time.time()
    bubble_sort(a)
    end=time.time()
    print(len(a),"elements sorted by bubble sort is",end-start)
    elements.append(len(a))
    times.append(end-start)
plt.xlabel("list length")
plt.ylabel("time complexity")
plt.plot(elements,times,label="bubble sort")
plt.grid()
plt.legend()
plt.show()


                
        

