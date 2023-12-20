# 클래스 정의
class Stu:
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def Hi(self):
        print("Hi, {} {}!".format(self.num, self.name))

# 객체 생성
a = Stu(1111, "Jake")
b = Stu(1411, "Maki")

# 메소드 호출
a.Hi() # >> Hi, 1111 Jake!
b.Hi() # >> Hi, 2222 Maki!

# Stu클래스 상속
class Aespa(Stu):
    def __init__(self, num, name):
        super().__init__(num, name)
    
    def Hi(self):
        super().Hi()
        print("안녕하세요! 저는 에스파 {} {}입니다!".format(self.num, self.name))

c = Aespa(3333, "Karina")#객체 생성
c.Hi() #메소드 호출
# >> Hi, 3333 Karina!
# >> 안녕하세요! 저는 에스파 3333 Karina입니다!