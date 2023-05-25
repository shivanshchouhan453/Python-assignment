n=int(input("enter number"))

count=0

i=1

while(i<=n):

    if(n%i==0):

        count=count+1

    i=i+1

if(count==2):

    print("number is prime")

else:

    print ("number is not prime")
