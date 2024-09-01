import math
import time

plus_ten=lambda x : x+10
result=0
#시간측정
start=time.time()
#for i in range(1000000):
    #result+=plus_ten(i)
term=[i+10 for i in range(1,1000000)]
ans = sum(term)# lambda 뒤의 x 조건식을 x=~~ 라고 쓸수 없다.
print(ans)


end=time.time()
print(end-start)