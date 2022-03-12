#doc31

n = int(input("Enter number of terms  : "))
s = 0
pr = 1
i = 1
while(i<=n) :
    pr = i * pr
    print(pr, end = " + ")
    s = s + pr
    i = i + 1
print(" total sum=", s)
