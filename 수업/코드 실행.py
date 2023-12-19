"""
print(type(123))# <class 'int'>
print(type(12.3))# <class 'float'>
print(type(True))# <class 'bool'>
print(type('abc'))# <class 'str'>
print(type([1,2,3]))# <class 'list'>
print(type((1,2,3)))# <class 'tuple'>
print(type({1,2,3}))# <class 'set'>
print(type({"a":1, "b":2, "c":3}))# <class 'dict'>


list = [1, 2, 3, 4, 5] # 인덱스는 0부터 시작
print(list[1:3]) #2, 3출력
print(*list[0:3]) #1, 2, 3출력
print(list[:3])#1,2,3 출력
print(list[1:])#2,3,4,5 출력
print(list[0:])#1,2,3,4,5 출력

print(5/2)#2.5
print(5//2)#2
print(5%2)#1
a = 0
a += 3
print(a)#3
b = 4
b -= 3
print(b)#1
b = 0
#b++ 이건 안 됨


a = input()
reverse_a = ''

for i in a:
  reverse_a = i+reverse_a 

print(reverse_a)

# if elif else 의 조건 파악하는 것 중요!
a = int(input())
if a >= 50:
	print("50")
if a >= 40:
	print("40")
else:
	print("I don't know!")
# 50 입력
# >> 50
# >> 40
#if는 본인의 조건만 만족하면 발동
	
if a >= 60:
  print("60")
elif a >= 40:
	print("40")
else:
	print("I don't know!")

#60 입력 
# >> 60
#elif는 앞 if조건이 거짓이어야만 발동됨

a = input()
print(len(a))

# 클래스 정의
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

# 클래스 상속
class Aespa(Stu):
    def __init__(self, num, name):
        super().__init__(num, name)
    
    def Hi(self):
        super().Hi()
        print("안녕하세요! 저는 에스파 {} {}입니다!".format(self.num, self.name))

c = Aespa(3333, "Karina")
c.Hi() 
# >> Hi, 3333 Karina!
# >> 안녕하세요! 저는 에스파 3333 Karina입니다!

a = input()*5
print(a)
print("hello"+"world")
print(3**3)

a1 = [6, 3, 9]
a2 = []

# sort() : 리스트 원본을 정렬
a1.sort()
print(a1, a2, sep=", ") # >> [3, 6, 9], []
"""


a = [1, 2, 3]
a.reverse()
print(a)

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)
