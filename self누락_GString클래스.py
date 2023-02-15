# 전역변수(이름충돌)
# 파이썬은 모호한 것 보다는 명시적인것이 좋다
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)
#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
