class calculator:
    #__init__의 역할은 클래스 객체 생성시 호출되는 함수
    #self 객체를 가리키는 표현
    def __init__(self):
        self.result=0
        self.op1=0
        self.op2=0
        #self.operation='+'
    
    
    #클래스의 멤버함수의 첫번째 인수는 무조건 self 받을게없어도
    #클래스 안의 멤버 변수는 직접 변수값을 설정할 수 없으므로 멤버 함수를 통해 값을 설정해야함 보안적인 부분
    def inputValue(self,op1,op2):
        self.op1 = op1
        self.op2 = op2
        
    def add(self):
        self.result=self.op1 + self.op2
        print(self.result)
        
    def directadd(self, op1, op2):
        self.op1=op1
        self.op2=op2
        self.result=self.op1+self.op2
        print(self.result)
         
    def sub(self):
        self.result=self.op1-self.op2
        print(self.result)
         
#클래스의 객체 cal1을 생성
#객체 생성시 __init__함수를 호출
cal1=calculator()
#cal2=calculator()

cal1.inputValue(2,3)
cal1.add()