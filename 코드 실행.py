# print(type(bool))
# print(type(list))
# print(type(tuple))
# print(type(dict))
# print(type(set))
# list = [1, 2, 3, 4, 5] # 인덱스는 0부터 시작
# print(list[1:3]) #2, 3출력
# print(list[:3])#1,2,3 출력
# print(list[1:])#2,3,4,5 출력

# a = input()
# reverse_a = ''

# for i in a:
#   reverse_a = i+reverse_a 

# print(reverse_a)

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