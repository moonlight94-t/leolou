import sys

option=sys.argv[1]

if option =='-a':
    memo=sys.argv[2]
    f=open('memo.txt','a')
    f.write(memo+'\n')
    f.close()
elif option=='-v':
    f=open('memo.txt','r')
    memo=f.read()
    f.close()
    print(memo)