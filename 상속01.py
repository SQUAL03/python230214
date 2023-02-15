#부모 클래스 정의
class Person(object):
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재 작업중...")
    def eating(self):
        print("현재 식사중...")

#자식 클래스 정의
class Student(Person):
    # 재정의(덮어쓰기, 오버라이딩)
    def __init__(self, name, phoneNumber, subject, studentID):
#        self.name = name
#        self.phoneNumber = phoneNumber
#       위의 코딩 대신 상속받아 사용
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
        #재정의(상속받아서 로직에 덮어쓰기)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number:{1})".format(self.name,self.phoneNumber))
        print("Info(Subject:{0}, StudentID:{1})".format(self.subject,self.studentID))
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")
p.printInfo()
s.printInfo()
print(p.__dict__)
print(s.__dict__)
s.working()
s.eating()


