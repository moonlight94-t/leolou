import sys

a=int(sys.argv[1])
b=int(sys.argv[2])
result=0

for i in range(a,b+1):
    result+=i
    
print(result)