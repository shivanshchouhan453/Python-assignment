#Python Program for Sum of squares of first n natural numbers

sum=0
i=1
n=int(input("enter value"))
while(i<=n):
    sum+=i*i
    i+=1
print("sum of squares of ",n,"natural number is:",sum)
