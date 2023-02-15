# 메모리관리.py 

class MyClass:
    #초기화 메서드(생성자)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소멸자 메서드(소멸자)    
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
# 자동으로 GC가 일어남으로 아래코드는 필요없음(del d)
del d 

print("전체 코드 실행 종료")