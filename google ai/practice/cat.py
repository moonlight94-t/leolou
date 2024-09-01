import sys

name=sys.argv[1]

try:
    f=open(name,'r', encoding="UTF-8-sig")
except FileNotFoundError:
    print('파일이 없습니다')
    sys.exit()
    
f=open(name,'r',encoding="UTF-8-sig")
text=f.read()
f.close()
print(text)